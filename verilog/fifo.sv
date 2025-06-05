// 异步FIFO模块
module async_fifo #(
    parameter DATA_WIDTH = 7,       // 数据宽度
    parameter FIFO_DEPTH = 128      // FIFO深度
)(
    input logic wr_clk,             // 写时钟 300MHz
    input logic rd_clk,             // 读时钟 200MHz
    input logic rst_n,              // 复位信号
    input logic wr_en,              // 写使能
    input logic rd_en,              // 读使能
    input logic [DATA_WIDTH-1:0] data_in, // 写数据
    output logic [DATA_WIDTH-1:0] data_out, // 读数据
    output logic full,              // FIFO满标志
    output logic empty              // FIFO空标志
);

localparam PTR_WIDTH = $clog2(FIFO_DEPTH) + 1; // 格雷码指针宽度

logic [PTR_WIDTH-1:0] wr_ptr, rd_ptr;
logic [PTR_WIDTH-1:0] wr_ptr_gray, rd_ptr_gray;
logic [PTR_WIDTH-1:0] rd_ptr_sync, wr_ptr_sync;

// RAM存储
logic [DATA_WIDTH-1:0] ram [0:FIFO_DEPTH-1];

// 格雷码转换函数
function automatic [PTR_WIDTH-1:0] bin_to_gray(input [PTR_WIDTH-1:0] bin);
    return bin ^ (bin >> 1);
endfunction

// 写逻辑
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        wr_ptr <= '0;
        wr_ptr_gray <= '0;
    end else if (wr_en && !full) begin
        wr_ptr <= wr_ptr + 1;
        wr_ptr_gray <= bin_to_gray(wr_ptr);
    end
end

// 读逻辑
always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        rd_ptr <= '0;
        rd_ptr_gray <= '0;
    end else if (rd_en && !empty) begin
        rd_ptr <= rd_ptr + 1;
        rd_ptr_gray <= bin_to_gray(rd_ptr);
    end
end

// 指针同步
// 写指针同步到读时钟域
always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        wr_ptr_sync <= '0;
    end else begin
        wr_ptr_sync <= {wr_ptr_sync[PTR_WIDTH-2:0], wr_ptr_gray[PTR_WIDTH-1]};
    end
end

// 读指针同步到写时钟域
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        rd_ptr_sync <= '0;
    end else begin
        rd_ptr_sync <= {rd_ptr_sync[PTR_WIDTH-2:0], rd_ptr_gray[PTR_WIDTH-1]};
    end
end

// 空/满标志生成
assign full = (wr_ptr_gray == rd_ptr_sync) && (wr_en && !full);
assign empty = (rd_ptr_gray == wr_ptr_sync) && (rd_en && !empty);

// 数据写入RAM
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        for (int i=0; i<FIFO_DEPTH; i++) ram[i] <= '0;
    end else if (wr_en && !full) begin
        ram[wr_ptr] <= data_in;
    end
end

// 数据输出
always_comb begin
    data_out = ram[rd_ptr];
end

endmodule
