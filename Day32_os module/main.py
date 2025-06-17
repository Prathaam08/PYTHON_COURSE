import os

# Your main folder path
parent_dir = r"C:\Users\prath\PYTHON COURSE"

# Folder(s) to exclude from renaming
exclude = {"EXERCISE"}

# Get all subfolders except excluded ones
folders = [
    os.path.join(parent_dir, d)
    for d in os.listdir(parent_dir)
    if os.path.isdir(os.path.join(parent_dir, d)) and d not in exclude
]

# Sort by creation time (oldest first)
folders.sort(key=os.path.getctime)

# Rename all except the excluded ones
for i, folder_path in enumerate(folders, start=1):
    folder_name = os.path.basename(folder_path)
    new_name = f"Day{i}_{folder_name}"
    new_path = os.path.join(parent_dir, new_name)

    os.rename(folder_path, new_path)
    print(f"Renamed: {folder_name} → {new_name}")
