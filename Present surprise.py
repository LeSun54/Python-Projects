import os

def rename_files ():
    file_list = os.listdir("/Users/Sunym/Downloads/alphabet")
    save_path = os.getcwd ()
    os.chdir ("/Users/Sunym/Downloads/alphabet")
    #print (file_list)
    for file_name in file_list:
        print ("Old name", file_name)
        print ("New name", file_name.strip("0123456789"))
        os.rename(file_name, file_name.strip("0123456789"))
    os.chdir(saved_path)
rename_files ()
