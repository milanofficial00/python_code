import os
import re

# Folder path
folder_path = r"C:\Users\pantb\OneDrive\Desktop\final\train\images" # source path
folder_path2 = r"C:\Users\pantb\OneDrive\Desktop\final\images" # destinatioon path

# Get all image files (you can add more extensions if needed)
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

# Function to extract number from filename
def extract_number(filename):
    match = re.search(r'(\d+)', filename)
    return int(match.group(1)) if match else float('inf')

# Sort files numerically based on the number in filename
image_files = sorted(image_files, key=extract_number)

# (Optional) Show sorted order before renaming
print(" Files in ascending numeric order:")
for f in image_files:
    print(f)
print("\nStarting renaming...\n")

# Rename files in the sorted order
for i, filename in enumerate(image_files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"img_{i}{ext}"
    old_path = os.path.join(folder_path, filename)
    new_path = os.path.join(folder_path2, new_name)

    os.rename(old_path, new_path)
    print(f"Renamed: {filename} -> {new_name}")

print("\n Renaming completed successfully in correct ascending order!")
