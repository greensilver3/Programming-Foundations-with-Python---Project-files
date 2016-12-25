import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"/Users/Mac/Documents/prank/")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is "+saved_path)
    os.chdir("/Users/Mac/Documents/prank/")
    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old File Name:", file_name)
        remap = {ord('1') : '', ord('2') : '',ord('3') : '',ord('4') : '',ord('5') : '', ord('6') : '',ord('7') : '',ord('8') : '',ord('9') : '',ord('0') : ''}
        file_name = file_name.translate(remap)
        print("new file name:",file_name)
        #os.rename(file_name, file_name.translate("0123456789",""))
    os.chdir(saved_path)
rename_files()
