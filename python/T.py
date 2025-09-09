import os
import merge_mif_files
def main():
        script_dir = os.path.dirname(os.path.abspath(__file__))
    
        name0 = "ROM"
    
        mif_dir = os.path.join(script_dir,"mif")
    
        rom_file0 = os.path.join(mif_dir, f"{name0}.mif")
    
        with open(rom_file0, 'w') as f:
    
            f.write("")
        print('111')
        merge_mif_files.SA()
        print('222')

if __name__ == "__main__":
      main()