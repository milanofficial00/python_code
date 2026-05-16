import os
import re

# Folder path
folder_path = r"C:\Users\pantb\OneDrive\Desktop\final\train\labels" #source path
folder_path2 = r"C:\Users\pantb\OneDrive\Desktop\final\labels" #destination path

# Get all label files in text document
label_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.txt')]

# Function to extract number from filename
def extract_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

# Sort files numerically based on the number in filename
label_files = sorted(label_files, key=extract_number)

# (Optional) Show sorted order before renaming
print(" Files in ascending numeric order:")
for f in label_files:
    print(f)
print("\nStarting renaming...\n")

# Rename files in the sorted order
for i, filename in enumerate(label_files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"img_{i}{ext}"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path2, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

print("\n Renaming completed successfully in correct ascending order!")
