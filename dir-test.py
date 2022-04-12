import os

parent_directory = "dataset/"
userName = "cam"
path = os.path.join(parent_directory, userName)

isdir = os.path.isdir(path)

print(isdir)
# os.mkdir(path)
# print("Directory {} has been created.\n".format(path))