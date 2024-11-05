import os
import sys

def list_files(directory):
    """Return a set of file names in the given directory."""
    try:
        return set(os.listdir(directory))
    except FileNotFoundError:
        print(f"Error: The directory '{directory}' does not exist.")
        sys.exit(1)

def compare_files(dir1, dir2):
    """Prints the files that are different between two directories."""
    files1 = list_files(dir1)
    files2 = list_files(dir2)

    # Find files unique to each directory
    unique_to_dir1 = files1 - files2
    unique_to_dir2 = files2 - files1

    if unique_to_dir1:
        print(f"Files unique to {dir1}:")
        for file in unique_to_dir1:
            print(file)

    if unique_to_dir2:
        print(f"Files unique to {dir2}:")
        for file in unique_to_dir2:
            print(file)

    if not unique_to_dir1 and not unique_to_dir2:
        print("Both directories have the same files.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <path_to_directory1> <path_to_directory2>")
        sys.exit(1)

    dir1, dir2 = sys.argv[1], sys.argv[2]
    compare_files(dir1, dir2)