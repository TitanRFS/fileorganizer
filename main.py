import os
import shutil

def organize_files(folder_path):
    file = [ f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path,f)) ]
    for f in file:
        file_extension = os.path.splittext[1][1:]
        folder_name = file_extension.upper() + "_Files"

        #Create a folder if not exist
        if not os.path.exists(os.path.join(folder_path,folder_name)):
            os.makedirs(os.path.join(folder_path,folder_name))

        #Move the file to the folder
        shutil.move(os.path.join(folder_path,f),os.path.join(folder_path,folder_name,f))

        print("File moved successfully")

        #prodiving the path of the folder

        folder_path = input("Enter the folder path: ")
