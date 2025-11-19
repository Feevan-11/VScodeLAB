import sg_add         
import asm_generate   
import translator     
import sparse_matrix
import hex_to_bin     
import merge_mif_files
import sparse_sg         
import tablemd        
import loop           


if __name__ == "__main__":
    matrix_size = 64
    sparsity = 0.9
    descriptors = 0x002000
    random = False
    block_width = 32
    element_size = 2
    APP0 = 0
 

    sparse_matrix.main(matrix_size,sparsity)

    sparse_sg.main(descriptors)

    hex_to_bin.main()

    merge_mif_files.SPARSE_main()

    tablemd.main()