module async_fifo #(
        parameter DATA_WIDTH = 7,       
        parameter FIFO_DEPTH = 128      
    )(
        input logic wr_clk,            //300HZ 
        input logic rd_clk,            //200HZ
        input logic rst_n,              
        input logic wr_en,              
        input logic rd_en,              
        input logic [DATA_WIDTH-1:0] data_in, 
        output logic [DATA_WIDTH-1:0] data_out,
        output logic full,              
        output logic empty              
    );
    
    localparam PTR_WIDTH = $clog2(FIFO_DEPTH) + 1; 
    
    logic [PTR_WIDTH-1:0] wr_ptr, rd_ptr;
    logic [PTR_WIDTH-1:0] wr_ptr_gray, rd_ptr_gray;
    logic [PTR_WIDTH-1:0] rd_ptr_sync, wr_ptr_sync;
    
    
    logic [DATA_WIDTH-1:0] ram [0:FIFO_DEPTH-1];
    
    
    function automatic [PTR_WIDTH-1:0] bin_to_gray(input [PTR_WIDTH-1:0] bin);
        return bin ^ (bin >> 1);
    endfunction
    
    // write
    always_ff @(posedge wr_clk or negedge rst_n) begin
        if (!rst_n) begin
            wr_ptr <= '0;
            wr_ptr_gray <= '0;
        end else if (wr_en && !full) begin
            wr_ptr <= wr_ptr + 1;
            wr_ptr_gray <= bin_to_gray(wr_ptr);
        end
    end
    
    // read
    always_ff @(posedge rd_clk or negedge rst_n) begin
        if (!rst_n) begin
            rd_ptr <= '0;
            rd_ptr_gray <= '0;
        end else if (rd_en && !empty) begin
            rd_ptr <= rd_ptr + 1;
            rd_ptr_gray <= bin_to_gray(rd_ptr);
        end
    end
    
    
    always_ff @(posedge rd_clk or negedge rst_n) begin
        if (!rst_n) begin
            wr_ptr_sync <= '0;
        end else begin
            wr_ptr_sync <= {wr_ptr_sync[PTR_WIDTH-2:0], wr_ptr_gray[PTR_WIDTH-1]};
        end
    end
    

    always_ff @(posedge wr_clk or negedge rst_n) begin
        if (!rst_n) begin
            rd_ptr_sync <= '0;
        end else begin
            rd_ptr_sync <= {rd_ptr_sync[PTR_WIDTH-2:0], rd_ptr_gray[PTR_WIDTH-1]};
        end
    end
    
    // empty/full
    assign full = (wr_ptr_gray == rd_ptr_sync) && (wr_en && !full);
    assign empty = (rd_ptr_gray == wr_ptr_sync) && (rd_en && !empty);
    
    // write_reg
    always_ff @(posedge wr_clk or negedge rst_n) begin
        if (!rst_n) begin
            for (int i=0; i<FIFO_DEPTH; i++) ram[i] <= '0;
        end else if (wr_en && !full) begin
            ram[wr_ptr] <= data_in;
        end
    end
    
    
    always_comb begin
        data_out = ram[rd_ptr];
    end

endmodule
