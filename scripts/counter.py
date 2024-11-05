import os

def count_files_in_directory(directory_path):
    # Check if the directory exists
    if not os.path.isdir(directory_path):
        return "Error: The specified path is not a directory."

    # Initialize a count variable
    file_count = 0

    # Iterate through all the files in the directory
    for _, _, files in os.walk(directory_path):
        file_count += len(files)

    return file_count

if __name__ == "__main__":
    directory_path = input("Enter the path of the directory: ")
    files_count = count_files_in_directory(directory_path)
    print("Number of files in the directory:", files_count)