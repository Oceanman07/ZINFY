import os

# folder path
dir_path = "background/"

# list to store files
list_background = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        if path == ".DS_Store":
            continue
        else:
            pass
        # print(path)
        list_background.append(path)



