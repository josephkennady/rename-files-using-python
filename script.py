import os

folder_path = "path/to/folder"
prefix = "prefix_"

for filename in os.listdir(folder_path):
    if not filename.startswith(prefix):
        new_filename = prefix + filename
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
