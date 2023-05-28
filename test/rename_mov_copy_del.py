folder_path = "C:\\Users\\ACER\\Desktop\\Practice"

############# Creating New Files #################################
# for i in range(1, 6):
#     fp = open(f"{folder_path}\\file{i}.py", 'w')
#     fp.close()

import os
import shutil

###### This changes the current working tree to the provided location ###############
os.chdir(folder_path)


############# Renaming the files inside in the current working tree ############
# for count, file in enumerate(os.listdir(), start=1):
#     name, ext = os.path.splitext(file)
#     new_name = f"test{count}{ext}"
#     os.rename(file, new_name)


############### Creating a new folder 'data' if it does not exist ###################
if not os.path.exists("data"):
    os.mkdir("data")

################ Copying and moving the files #############################
# for file in os.listdir():
#     if file == "data":
#         continue
#     # shutil.move(file, "data")
#     shutil.copy2(file, "data")


################## Removing files and folders ######################
# os.remove("test1.py")
# os.rmdir("data")
shutil.rmtree("data")
