import os

# folder path
dir_path = "audio/"

# list to store files
list_music = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
      if path == ".DS_Store":
            continue
      else:
            pass
      list_music.append(path)



