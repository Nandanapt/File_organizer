
import os
import shutil

# Step 1: Define file categories with common file extensions for each
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
}

# Step 2: Prompt the user to input the directory path
directory_path = input("Enter the path of the directory to organize: ")

# Check if the specified directory exists
if not os.path.isdir(directory_path):
    print("The specified directory does not exist.")
    exit()

# Step 3: Organize files by type
def organize_files(directory):
    # Loop through each file in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Identify the file type and move to corresponding folder
        file_moved = False
        for category, extensions in FILE_CATEGORIES.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                category_folder = os.path.join(directory, category)
                os.makedirs(category_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(category_folder, filename))
                file_moved = True
                break

        # Move to 'Others' if file type does not match any category
        if not file_moved:
            others_folder = os.path.join(directory, "Others")
            os.makedirs(others_folder, exist_ok=True)
            shutil.move(file_path, os.path.join(others_folder, filename))

# Run the file organization function
organize_files(directory_path)

print("Files organized successfully.")
