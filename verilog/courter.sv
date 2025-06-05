// 性能统计主模块
module performance_monitor #(
    parameter WR_CLK_FREQ = 300_000_000, // 300MHz
    parameter RD_CLK_FREQ = 200_000_000, // 200MHz
    parameter SAMPLE_PERIOD = 100        // 采样周期
)(
    input logic wr_clk,                  // 300MHz
    input logic rd_clk,                  // 200MHz
    input logic rst_n,                   // 复位
    input logic busy,                    // 脉动阵列busy信号
    output logic [31:0] perf_register,   // 性能寄存器输出
    input logic reg_read                 // 寄存器读取使能
);

// FIFO参数配置
localparam FIFO_DATA_WIDTH = 7;
localparam FIFO_DEPTH = 128;

// 内部信号
logic wr_en;
logic rd_en;
logic [FIFO_DATA_WIDTH-1:0] data_in, data_out;
logic full, empty;

// FIFO实例化
async_fifo #(
    .DATA_WIDTH(FIFO_DATA_WIDTH),
    .FIFO_DEPTH(FIFO_DEPTH)
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

// 写侧逻辑（300MHz）
logic [FIFO_DATA_WIDTH-1:0] busy_counter;
logic sync_busy;

// busy信号同步器
logic [1:0] busy_sync;
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) 
        busy_sync <= '0;
    else 
        busy_sync <= {busy_sync[0], busy};
end
assign sync_busy = busy_sync[1];

// 计数器逻辑
always_ff @(posedge wr_clk or negedge rst_n) begin
    if (!rst_n) begin
        busy_counter <= '0;
        wr_en <= 1'b0;
    end else if (sync_busy) begin
        if (busy_counter == SAMPLE_PERIOD - 1) begin
            data_in <= busy_counter;
            wr_en <= 1'b1;
            busy_counter <= '0;
        end else begin
            busy_counter <= busy_counter + 1;
            wr_en <= 1'b0;
        end
    end else begin
        busy_counter <= '0;
        wr_en <= 1'b0;
    end
end

// 读侧逻辑（200MHz）
logic [31:0] total_cycles;
logic [FIFO_DATA_WIDTH-1:0] fifo_data;

always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) begin
        total_cycles <= '0;
        rd_en <= 1'b0;
    end else if (!empty) begin
        total_cycles <= total_cycles + data_out;
        rd_en <= 1'b1;
    end else begin
        rd_en <= 1'b0;
    end
end

// 寄存器清零逻辑
always_ff @(posedge rd_clk or negedge rst_n) begin
    if (!rst_n) 
        perf_register <= '0;
    else if (reg_read) 
        perf_register <= '0;
    else 
        perf_register <= total_cycles;
end

endmodule