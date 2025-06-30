`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2025/06/09 15:08:23
// Design Name: 
// Module Name: performence_counter
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


module performance_counter #(
    parameter SAMPLE_PERIOD = 100,
    parameter REG_DATA_WIDTH = 32,
    parameter FIFO_DATA_DEPTH = 7,
    parameter FIFO_DEPTH = 128
)(
    wr_clk_i ,  //300HZ
    rd_clk_i ,  //200HZ
    rst      ,
    busy_i   ,
    p_ctrl_reg_data_o ,
    p_ctrl_reg_data_valid_o ,
    ctrl_p_reg_data_i ,
    ctrl_p_reg_data_valid_i

);
    input    wr_clk_i ;
    input    rd_clk_i ;
    input    rst      ;
    input    busy_i   ;
    output   [REG_DATA_WIDTH - 1 : 0] p_ctrl_reg_data_o ;
    output   p_ctrl_reg_data_valid_o ;
    input    [REG_DATA_WIDTH - 1 : 0] ctrl_p_reg_data_i ;
    input    ctrl_p_reg_data_valid_i ;


    logic wr_en;
    logic rd_en;
    logic [FIFO_DATA_DEPTH - 1 : 0]din;
    logic [FIFO_DATA_DEPTH - 1 : 0]dout;
    reg   [FIFO_DATA_DEPTH - 1 : 0]data_in_reg;
    reg   [FIFO_DATA_DEPTH - 1 : 0]data_out_reg;
    logic [FIFO_DATA_DEPTH - 1 : 0] reg_courter;
    logic [REG_DATA_WIDTH  - 1 : 0] reg_perf;
    logic buzy_clear;
    logic full;
    logic empty;
    logic valid;
    logic wr_ack;

    

    asyn_fifo u_asyn_fifo (
        .rst(~rst),                     // input wire rst
        .wr_clk(wr_clk),                // input wire wr_clk
        .rd_clk(rd_clk),                // input wire rd_clk
        .din(din),                      // input wire [6 : 0] din
        .wr_en(wr_en),                  // input wire wr_en
        .rd_en(rd_en),                  // input wire rd_en
        .dout(dout),                    // output wire [6 : 0] dout
        .full(full),                    // output wire full
        .almost_full(almost_full),      // output wire almost_full
        .wr_ack(wr_ack),                // output wire wr_ack
        .overflow(overflow),            // output wire overflow
        .empty(empty),                  // output wire empty
        .almost_empty(almost_empty),    // output wire almost_empty
        .valid(valid),                  // output wire valid
        .underflow(underflow),          // output wire underflow
        .rd_data_count(),  // output wire [6 : 0] rd_data_count
        .wr_data_count(),  // output wire [6 : 0] wr_data_count
        .wr_rst_busy(wr_rst_busy),      // output wire wr_rst_busy
        .rd_rst_busy(rd_rst_busy)      // output wire rd_rst_busy
    );

    assign wr_clk = wr_clk_i;
    assign rd_clk = rd_clk_i;
    assign wr_ack =1'b1;


    always_ff @(posedge wr_clk_i or negedge rst)begin 
        if(!rst || buzy_clear)begin
            reg_courter <= 0;
        end else if(busy_i)begin
            reg_courter <= reg_courter + 1;
        end

    end

    always_comb begin 
        if(reg_courter == 99 && busy_i)begin
            buzy_clear = 1'b1;
            wr_en = 1'b1;
            data_in_reg    = 7'b000_0001;
        end
        else begin
            buzy_clear = 1'b0;
            wr_en = 1'b0;
            data_in_reg    = 7'b0;
        end
    end

    always_comb begin 
        if(!empty)begin
            rd_en = 1'b1;
        end
        else begin
            rd_en = 1'b0;
        end
    end



    always_ff @(posedge rd_clk_i or negedge rst)begin
        if(!rst)  begin
            reg_perf <= 'b0;
        end
        else if(ctrl_p_reg_data_valid_i) begin
            reg_perf <= ctrl_p_reg_data_i;
        end
        else if(!empty)begin
            reg_perf <= reg_perf + dout; 
        end
    end
    
    assign din = data_in_reg;
    assign data_out_reg = dout;
    assign p_ctrl_reg_data_valid_o = 'b1;
    assign p_ctrl_reg_data_o = reg_perf;

endmodule
