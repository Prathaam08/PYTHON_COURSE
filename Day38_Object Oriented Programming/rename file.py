import os
import re

# Path to your Day38 folder
parent_dir = r"C:\Users\prath\PYTHON-COURSE\Day38_Object Oriented Programming"

# Get all subfolders (full paths)
folders = [
    os.path.join(parent_dir, d)
    for d in os.listdir(parent_dir)
    if os.path.isdir(os.path.join(parent_dir, d))
]

# Sort by creation time (oldest first)
folders.sort(key=os.path.getctime)

# Rename folders with 01_, 02_, etc.
for i, folder_path in enumerate(folders, start=1):
    folder_name = os.path.basename(folder_path)

    # Skip if already prefixed (optional safety)
    if re.match(r"^\d{2}_", folder_name):
        continue

    new_name = f"{i:02d}_{folder_name}"
    new_path = os.path.join(parent_dir, new_name)
    os.rename(folder_path, new_path)
    print(f"Renamed: {folder_name} → {new_name}")
