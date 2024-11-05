import os
import shutil

def get_files_in_directory(directory):
    # Get list of files in the directory
    files = []
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(os.path.join(dirpath, filename))
    return files

def copy_matching_files(source_dir, target_dir, files_to_match):
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Copy matching files to the target directory
    for filename in files_to_match:
        source_file = os.path.join(source_dir, os.path.basename(filename))
        if os.path.exists(source_file):
            shutil.copy(source_file, target_dir)

if __name__ == "__main__":
    # Input directories
    source_directory = input("Enter the path of the source directory: ")
    target_directory = input("Enter the path of the target directory: ")

    # Get list of files in source directory
    source_files = get_files_in_directory(source_directory)

    # Get list of files in target directory
    target_files = get_files_in_directory(target_directory)

    # Find matching files and copy them to a new directory
    matching_files = [file for file in source_files if os.path.basename(file) in [os.path.basename(target_file) for target_file in target_files]]

    # Directory to copy matching files
    new_directory = input("Enter the path of the directory to copy matching files: ")

    # Copy matching files to new directory
    copy_matching_files(source_directory, new_directory, matching_files)

    print("Matching files copied successfully.")