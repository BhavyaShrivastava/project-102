import os
import shutil

from_dir="C:/Users/CHH/Downloads"
to_dir="C:/Users/CHH/Documents/Document_Files project102"

list_of_files = os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

    if extension == '':
        continue
    if extension in ['.txt', '.pdf', '.doc', '.docx']:

        path_1 = from_dir + '/' + file_name                               
        path_2 = to_dir + '/' + "Document_Files"                           
        path_3 = to_dir + '/' + "Document_Files" + '/' + file_name   
        

        if os.path.exists(path_2):
          print("Moving " + file_name + ".....")
         
          shutil.move(path_1, path_3)

        else:
          os.makedirs(path_2)
          print("Moving " + file_name + ".....")
          shutil.move(path_1, path_3)

