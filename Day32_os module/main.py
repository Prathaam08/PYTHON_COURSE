# import os

# # Your main folder path
# parent_dir = r"C:\Users\prath\PYTHON COURSE"

# # Folder(s) to exclude from renaming
# exclude = {"EXERCISE"}

# # Get all subfolders except excluded ones
# folders = [
#     os.path.join(parent_dir, d)
#     for d in os.listdir(parent_dir)
#     if os.path.isdir(os.path.join(parent_dir, d)) and d not in exclude
# ]

# # Sort by creation time (oldest first)
# folders.sort(key=os.path.getctime)

# # Rename all except the excluded ones
# for i, folder_path in enumerate(folders, start=1):
#     folder_name = os.path.basename(folder_path)
#     new_name = f"Day{i}_{folder_name}"
#     new_path = os.path.join(parent_dir, new_name)

#     os.rename(folder_path, new_path)
#     print(f"Renamed: {folder_name} → {new_name}")





# TO remove prefix

# import os
# import re

# parent_dir = r"C:\Users\prath\PYTHON COURSE"

# for folder in os.listdir(parent_dir):
#     folder_path = os.path.join(parent_dir, folder)
#     if os.path.isdir(folder_path) and re.match(r"Day\d+_", folder):
#         new_name = re.sub(r"^Day\d+_", "", folder)
#         new_path = os.path.join(parent_dir, new_name)
#         os.rename(folder_path, new_path)
#         print(f"Reverted: {folder} → {new_name}")


# To give the prefix to new folder 
import os
import re

# Your main folder path
parent_dir = r"C:\Users\prath\PYTHON-COURSE"

# Folder(s) to exclude
exclude = {"EXERCISES" , ".git"}

# Get all folders in the directory
all_folders = [
    d for d in os.listdir(parent_dir)
    if os.path.isdir(os.path.join(parent_dir, d)) and d not in exclude
]

# Separate already-prefixed and unprefixed folders
prefixed = [f for f in all_folders if re.match(r"Day\d+_", f)]
unprefixed = [f for f in all_folders if f not in prefixed]

# Find the next day number
if prefixed:
    last_day = max([int(re.match(r"Day(\d+)_", f).group(1)) for f in prefixed])
else:
    last_day = 0

# Sort unprefixed folders by creation time
unprefixed_full_paths = [
    os.path.join(parent_dir, f) for f in unprefixed
]
unprefixed_full_paths.sort(key=os.path.getctime)

# Rename the new folders
for i, folder_path in enumerate(unprefixed_full_paths, start=1):
    folder_name = os.path.basename(folder_path)
    new_day = last_day + i
    new_name = f"Day{new_day}_{folder_name}"
    new_path = os.path.join(parent_dir, new_name)
    os.rename(folder_path, new_path)
    print(f"Renamed: {folder_name} → {new_name}")
