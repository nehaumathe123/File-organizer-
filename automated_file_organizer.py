import os
import shutil

# Folder path to organize
source_folder = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".doc", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Programs": [".py", ".java", ".cpp", ".c"]
}

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        file_ext = os.path.splitext(file)[1].lower()

        moved = False
        for folder_name, extensions in file_types.items():
            if file_ext in extensions:
                folder_path = os.path.join(source_folder, folder_name)

                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)

                shutil.move(file_path, os.path.join(folder_path, file))
                print(f"Moved {file} to {folder_name}")
                moved = True
                break

        # For unknown file types
        if not moved:
            other_folder = os.path.join(source_folder, "Others")

            if not os.path.exists(other_folder):
                os.makedirs(other_folder)

            shutil.move(file_path, os.path.join(other_folder, file))
            print(f"Moved {file} to Others")

print("File organization completed!")
