// 异步FIFO模块
module async_fifo #(
    parameter DATA_WIDTH = 7,
    parameter FIFO_DEPTH = 128
)(
    input logic wr_clk,
    input logic rd_clk,
    input logic rst_n,
    input logic wr_en,
    input logic rd_en,
    input logic [DATA_WIDTH-1:0] data_in,
    output logic [DATA_WIDTH-1:0] data_out,
    output logic full,
    output logic empty
);

localparam LOG_DEPTH = $clog2(FIFO_DEPTH);
localparam PTR_WIDTH = LOG_DEPTH + 1;

logic [PTR_WIDTH-1:0] wr_ptr, rd_ptr;
logic [PTR_WIDTH-1:0] wr_ptr_gray, rd_ptr_gray;
logic [PTR_WIDTH-1:0] rd_ptr_sync, wr_ptr_sync;

logic [DATA_WIDTH-1:0] fifo_ram [0:FIFO_DEPTH-1];


function automatic [PTR_WIDTH-1:0] bin_to_gray(input [PTR_WIDTH-1:0] bin);
    return bin ^ (bin >> 1);
endfunction

// 写指针同步到读时钟域
always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        rd_ptr_sync <= '0;
        wr_ptr_sync <= '0;
    end else begin
        rd_ptr_sync <= {rd_ptr_sync[PTR_WIDTH-2:0], rd_ptr_gray[PTR_WIDTH-1]};
        wr_ptr_sync <= {wr_ptr_sync[PTR_WIDTH-2:0], wr_ptr_gray[PTR_WIDTH-1]};
    end
end

// 读指针同步到写时钟域
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        rd_ptr_sync <= '0;
        wr_ptr_sync <= '0;
    end else begin
        rd_ptr_sync <= {rd_ptr_sync[PTR_WIDTH-2:0], rd_ptr_gray[PTR_WIDTH-1]};
        wr_ptr_sync <= {wr_ptr_sync[PTR_WIDTH-2:0], wr_ptr_gray[PTR_WIDTH-1]};
    end
end

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

// FIFO写入
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        full <= 1'b0;
    end else if (wr_en) begin
        if (full) begin
            full <= 1'b1; // 保持full状态
        end else begin
            full <= (wr_ptr == FIFO_DEPTH - 1) && (wr_ptr_sync == wr_ptr);
        end
    end
end

// FIFO读出
always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        empty <= 1'b1;
    end else if (rd_en) begin
        if (empty) begin
            empty <= 1'b1; // 保持empty状态
        end else begin
            empty <= (rd_ptr == 0) && (rd_ptr_sync == rd_ptr);
        end
    end
end

// 数据输出
always_comb begin
    data_out = fifo_ram[rd_ptr];
end

// RAM写入
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        for (int i = 0; i < FIFO_DEPTH; i++) begin
            fifo_ram[i] <= '0;
        end
    end else if (wr_en && !full) begin
        fifo_ram[wr_ptr] <= data_in;
    end
end

endmodule

// 性能统计主模块
module performance_counter #(
    parameter WR_COUNTER_MAX = 100
)(
    input logic wr_clk,
    input logic rd_clk,
    input logic rst_n,
    input logic busy,
    output logic [31:0] reg1,
    input logic reg1_read
);

// 写侧参数
localparam WR_DATA_WIDTH = 7;
localparam WR_FIFO_DEPTH = 256;

// FIFO实例
logic wr_en, rd_en;
logic [WR_DATA_WIDTH-1:0] data_in, data_out;
logic full, empty;

async_fifo #(
    .DATA_WIDTH(WR_DATA_WIDTH),
    .FIFO_DEPTH(WR_FIFO_DEPTH)
) u_fifo (
    .wr_clk(wr_clk),
    .rd_clk(rd_clk),
    .rst_n(rst_n),
    .wr_en(wr_en),
    .rd_en(rd_en),
    .data_in(data_in),
    .data_out(data_out),
    .full(full),
    .empty(empty)
);

// 写侧逻辑
logic [WR_DATA_WIDTH-1:0] cnt_wr;
logic sync_busy;

// 同步busy信号
logic [1:0] busy_sync;

always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        busy_sync <= 2'b0;
        sync_busy <= 1'b0;
    end else begin
        busy_sync <= {busy_sync[0], busy};
        sync_busy <= busy_sync[1];
    end
end

always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        cnt_wr <= '0;
        wr_en <= 1'b0;
        data_in <= '0;
    end else if (sync_busy) begin
        if (cnt_wr == WR_COUNTER_MAX - 1) begin
            data_in <= cnt_wr;
            wr_en <= 1'b1;
            cnt_wr <= '0;
        end else begin
            cnt_wr <= cnt_wr + 1;
            wr_en <= 1'b0;
        end
    end else begin
        cnt_wr <= '0;
        wr_en <= 1'b0;
    end
end

// 读侧逻辑
logic [31:0] cnt_rd;

always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        cnt_rd <= '0;
        rd_en <= 1'b0;
    end else if (!empty) begin
        cnt_rd <= cnt_rd + data_out;
        rd_en <= 1'b1;
    end else begin
        rd_en <= 1'b0;
    end
end

// 通用寄存器清零逻辑
always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        cnt_rd <= '0;
    end else if (reg1_read) begin
        cnt_rd <= '0;
    end
end

// 将计数器连接到寄存器
assign reg1 = cnt_rd;

endmodule