#define CDMA0_BASE_ADDR   0xC0000800  // AXI CDMA0 基地址
#define CDMA1_BASE_ADDR   0xC0000840  // AXI CDMA1 基地址
#define DMA0_BASE_ADDR    0xC0000000  // AXI DMA0 基地址
#define DMA1_BASE_ADDR    0xC0000400  // AXI DMA1 基地址


#define Global_Men_0    0x04000000
#define Global_Men_01   0x24000000
#define Global_Men_1    0x48000000
#define Global_Men_11   0x68000000
#define Shared_Men_0    0x80000000
#define Shared_Men_01   0x84000000
#define Shared_Men_1    0x88000000
#define Shared_Men_11   0x8C000000
#define Shared_Men_2    0x90000000
#define Shared_Men_21   0x94000000
#define Shared_Men_3    0x98000000
#define Shared_Men_31   0x9C000000
#define Local_Men       0xA0000000
#define ROM             0xB0000000
#define Ins_Men         0xB0100000

#define CTRL_OFFSET       0x00  // 控制寄存器偏移
#define STATUS_OFFSET     0x04  // 控制寄存器偏移
#define SRC_ADDR_OFFSET   0x18  // 源地址寄存器偏移
#define DST_ADDR_OFFSET   0x20  // 目的地址寄存器偏移
#define BTT_OFFSET        0x28  // Bytes to Transfer (BTT) 寄存器偏移


#define MATRIX_SIZE       (4096 * 20480 * 4)  // 每个矩阵大小（字节）

void write_register(volatile unsigned int *base, unsigned int offset, unsigned int value) {
    base[offset / 4] = value;  // offset 是字节，需要除以 4 转换为字偏移
}

void wait_for_interrupt(){

};

void matrix_multiply_ping_pong_optimized() {
    volatile unsigned int *cdma0 = (unsigned int *)CDMA0_BASE_ADDR;
    volatile unsigned int *cdma1 = (unsigned int *)CDMA1_BASE_ADDR;
    volatile unsigned int *dma0 = (unsigned int *)DMA0_BASE_ADDR;
    volatile unsigned int *dma1 = (unsigned int *)DMA1_BASE_ADDR;

    unsigned int ping_pong_flag = 0;  // 0 表示使用 Shared Mem0/1，1 表示使用 Shared Mem2/3
    unsigned int A_rows = 4096, A_cols = 20480;
    unsigned int B_rows = 20480, B_cols = 4096;
    unsigned int block_size = 16;

    unsigned int A_global_addr = Global_Men_01;
    unsigned int B_global_addr = Global_Men_11;
 

    // 外层循环遍历所有分块
    for (unsigned int i = 0; i < A_rows; i += block_size) {


        for (unsigned int j = 0; j < B_cols; j += block_size) {


            // **Step 1: 使用 AXI CDMA 将当前分块搬移到 Shared Memory**
            unsigned int A_block_addr = Global_Men_0 + i * A_cols * 4;          // A 的当前分块基地址
            unsigned int B_block_addr = Global_Men_1 + j * B_rows * 4;          // B 的当前分块基地址（按列存储）


            if (i == 0 && j == 0) {
                // 初始阶段，向Shared Mem0 和 Shared Mem1 搬移第一个分块
                write_register(cdma0, SRC_ADDR_OFFSET, A_block_addr);
                write_register(cdma0, DST_ADDR_OFFSET, Shared_Men_2);  // Shared Mem0 地址
                write_register(cdma0, BTT_OFFSET, block_size * A_cols * 4);
                write_register(cdma0, CTRL_OFFSET, 0x1);  // 启动 CDMA0

                // 将 B 的分块搬移到 Shared Mem3
                write_register(cdma1, SRC_ADDR_OFFSET, B_block_addr);
                write_register(cdma1, DST_ADDR_OFFSET, Shared_Men_3);  // Shared Mem1 地址
                write_register(cdma1, BTT_OFFSET, block_size * B_rows * 4);
                write_register(cdma1, CTRL_OFFSET, 0x1);  // 启动 CDMA1
            }

            if (ping_pong_flag == 0) {
                // 将 A 的分块搬移到 Shared Mem2
                write_register(cdma0, SRC_ADDR_OFFSET, A_block_addr);
                write_register(cdma0, DST_ADDR_OFFSET, Shared_Men_2);  // Shared Mem2 地址
                write_register(cdma0, BTT_OFFSET, block_size * A_cols * 4);
                write_register(cdma0, CTRL_OFFSET, 0x1);  // 启动 CDMA0

                // 将 B 的分块搬移到 Shared Mem3
                write_register(cdma1, SRC_ADDR_OFFSET, B_block_addr);
                write_register(cdma1, DST_ADDR_OFFSET, Shared_Men_3);  // Shared Mem3 地址
                write_register(cdma1, BTT_OFFSET, block_size * B_rows * 4);
                write_register(cdma1, CTRL_OFFSET, 0x1);  // 启动 CDMA1

                write_register(dma0, SRC_ADDR_OFFSET, Shared_Men_0);   // Shared Mem0 源地址
                write_register(dma0, DST_ADDR_OFFSET, Shared_Men_01);  // Shared Mem0 目的地址
                write_register(dma0, BTT_OFFSET, block_size * A_cols * 4);
                write_register(dma0, CTRL_OFFSET, 0x1);  // 启动 DMA0

                write_register(dma1, SRC_ADDR_OFFSET, Shared_Men_1);   // Shared Mem1 源地址
                write_register(dma1, DST_ADDR_OFFSET, Shared_Men_11);  // Shared Mem1 目的地址
                write_register(dma1, BTT_OFFSET, block_size * B_rows * 4);
                write_register(dma1, CTRL_OFFSET, 0x1);  // 启动 DMA1


                // 循环等待 数据搬移与计算完成
                wait_for_interrupt();

                //将计算结果搬至global_mem
                write_register(cdma0, SRC_ADDR_OFFSET, Shared_Men_01);
                write_register(cdma0, DST_ADDR_OFFSET, A_global_addr);  
                write_register(cdma0, BTT_OFFSET, block_size * block_size * 4);
                write_register(cdma0, CTRL_OFFSET, 0x1);  // 启动 CDMA0

                write_register(cdma1, SRC_ADDR_OFFSET, Shared_Men_11);
                write_register(cdma1, DST_ADDR_OFFSET, B_global_addr);  
                write_register(cdma1, BTT_OFFSET, block_size * block_size * 4);
                write_register(cdma1, CTRL_OFFSET, 0x1);  // 启动 CDMA1

                // 循环等待 数据搬移与计算完成
                wait_for_interrupt();
                A_global_addr = A_global_addr + block_size* block_size * 4;
                B_global_addr = B_global_addr + block_size * block_size * 4;

                ping_pong_flag = 1;
            } else {
                // 将 A 的分块搬移到 Shared Mem0
                write_register(cdma0, SRC_ADDR_OFFSET, A_block_addr);
                write_register(cdma0, DST_ADDR_OFFSET, Shared_Men_0);  // Shared Mem0 地址
                write_register(cdma0, BTT_OFFSET, block_size * A_cols * 4);
                write_register(cdma0, CTRL_OFFSET, 0x1);  // 启动 CDMA0

                // 将 B 的分块搬移到 Shared Mem1
                write_register(cdma1, SRC_ADDR_OFFSET, B_block_addr);
                write_register(cdma1, DST_ADDR_OFFSET, Shared_Men_1);  // Shared Mem1 地址
                write_register(cdma1, BTT_OFFSET, block_size * B_rows * 4);
                write_register(cdma1, CTRL_OFFSET, 0x1);  // 启动 CDMA1

                write_register(dma0, SRC_ADDR_OFFSET, Shared_Men_2);     // Shared Mem2 源地址
                write_register(dma0, DST_ADDR_OFFSET, Shared_Men_21);     // Shared Mem2 目的地址
                write_register(dma0, BTT_OFFSET, block_size * A_cols * 4);
                write_register(dma0, CTRL_OFFSET, 0x1);  // 启动 DMA0

                write_register(dma1, SRC_ADDR_OFFSET, Shared_Men_3);     // Shared Mem3 源地址
                write_register(dma1, DST_ADDR_OFFSET, Shared_Men_21);     // Shared Mem3 目的地址 
                write_register(dma1, BTT_OFFSET, block_size * B_rows * 4);
                write_register(dma1, CTRL_OFFSET, 0x1);  // 启动 DMA1


                // 循环等待 数据搬移与计算完成
                wait_for_interrupt();

                //将计算结果搬至global_mem
                write_register(cdma0, SRC_ADDR_OFFSET, Shared_Men_21);
                write_register(cdma0, DST_ADDR_OFFSET, Global_Men_01);  
                write_register(cdma0, BTT_OFFSET, block_size * block_size * 4);
                write_register(cdma0, CTRL_OFFSET, 0x1);  // 启动 CDMA0

                write_register(cdma1, SRC_ADDR_OFFSET, Shared_Men_31);
                write_register(cdma1, DST_ADDR_OFFSET, Global_Men_11);  
                write_register(cdma1, BTT_OFFSET, block_size * block_size * 4);
                write_register(cdma1, CTRL_OFFSET, 0x1);  // 启动 CDMA1

                // 循环等待 数据搬移与计算完成
                wait_for_interrupt();
                A_global_addr = A_global_addr + block_size * block_size * 4;
                B_global_addr = B_global_addr + block_size * block_size * 4;

                ping_pong_flag = 0;
            }
        }
    }

    unsigned int current_block_A = A_rows % 12;
    unsigned int current_block_B = B_cols % 12;

    write_register(dma0, SRC_ADDR_OFFSET, Shared_Men_2);     // Shared Mem2 源地址
    write_register(dma0, DST_ADDR_OFFSET, Shared_Men_21);     // Shared Mem2 目的地址
    write_register(dma0, BTT_OFFSET, current_block_A * A_cols * 4);
    write_register(dma0, CTRL_OFFSET, 0x1);  // 启动 DMA0

    write_register(dma1, SRC_ADDR_OFFSET, Shared_Men_3);     // Shared Mem3 源地址
    write_register(dma1, DST_ADDR_OFFSET, Shared_Men_21);     // Shared Mem3 目的地址 
    write_register(dma1, BTT_OFFSET, current_block_B * B_rows * 4);
    write_register(dma1, CTRL_OFFSET, 0x1);  // 启动 DMA1


    // 循环等待 数据搬移与计算完成
    wait_for_interrupt();


}


        
    

