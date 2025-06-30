`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2025/06/09 16:11:06
// Design Name: 
// Module Name: tb_performance_counter
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module tb_performance_counter;

    // Parameters
    parameter SAMPLE_PERIOD      = 100;
    parameter REG_DATA_WIDTH     = 32;
    parameter FIFO_DATA_DEPTH    = 7;
    parameter FIFO_DEPTH         = 128;

    // Signals
    logic        wr_clk_i;
    logic        rd_clk_i;
    logic        rst;
    logic        busy_i;
    logic [REG_DATA_WIDTH-1:0] p_ctrl_reg_data_o;
    logic                      p_ctrl_reg_data_valid_o;
    logic [REG_DATA_WIDTH-1:0] ctrl_p_reg_data_i;
    logic                      ctrl_p_reg_data_valid_i;

    // DUT Instance
    performance_counter #(
        .SAMPLE_PERIOD     (SAMPLE_PERIOD),
        .REG_DATA_WIDTH    (REG_DATA_WIDTH),
        .FIFO_DATA_DEPTH   (FIFO_DATA_DEPTH),
        .FIFO_DEPTH        (FIFO_DEPTH)
    ) u_performance_counter (
        .wr_clk_i                  (wr_clk_i),
        .rd_clk_i                  (rd_clk_i),
        .rst                       (rst),
        .busy_i                    (busy_i),
        .p_ctrl_reg_data_o         (p_ctrl_reg_data_o),
        .p_ctrl_reg_data_valid_o   (p_ctrl_reg_data_valid_o),
        .ctrl_p_reg_data_i         (ctrl_p_reg_data_i),
        .ctrl_p_reg_data_valid_i   (ctrl_p_reg_data_valid_i)
    );

    // Clock Generation
    always begin
        #1.667 wr_clk_i = ~wr_clk_i;  // 300 MHz (3.333 ns period / 2)
    end

    always begin
        #2.5 rd_clk_i = ~rd_clk_i;    // 200 MHz (5 ns period / 2)
    end

    // Test Sequence
    initial begin
        // Initialize signals
        wr_clk_i = 0;
        rd_clk_i = 0;
        rst      = 1'b1;
        busy_i   = 1'b0;              // Keep busy_i high
        ctrl_p_reg_data_i       = '0;
        ctrl_p_reg_data_valid_i = '0;
        
        #12 rst   = 1'b0;
        // Apply reset
        #502 rst   = 1'b1;
        // Run for 5000 clock cycles of rd_clk (approx. 25,000 ns)
        #100 busy_i = 1'b1;
        #25000 $finish;
    end

    // Optional Monitor
    initial begin
        $monitor("Time: %0t | reg_perf = %0d", $time, p_ctrl_reg_data_o);
    end

endmodule
