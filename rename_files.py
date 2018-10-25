import os
def rename_files ():
    file_list = os.listdir("/Users/Sunym/Downloads/prank")
    saved_path = os.getcwd ()
    os.chdir("/Users/Sunym/Downloads/prank")
    #print (file_list)
    for file_name in file_list:
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)
rename_files ()
