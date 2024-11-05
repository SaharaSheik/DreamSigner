import tarfile
import os

def extract_mp4_files(tar_gz_file, destination_dir):
    # Check if the file exists
    if not os.path.exists(tar_gz_file):
        print("Error: The specified file does not exist.")
        return

    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Open the tar.gz file in read mode
    with tarfile.open(tar_gz_file, 'r:gz') as tar:
        # Get list of members (files and directories) in the tar.gz archive
        members = tar.getmembers()

        # Extract mp4 files from the tar.gz archive
        for member in members:
            if member.name.endswith('.mp4'):
                tar.extract(member, destination_dir)

    print("Extraction of .mp4 files completed.")

if __name__ == "__main__":
    # Input the path of the tar.gz file
    tar_gz_file = input("Enter the path of the tar.gz file: ")

    # Input the destination directory
    destination_dir = input("Enter the destination directoryyyyy: ")

    # Extract .mp4 files from the tar.gz file
    extract_mp4_files(tar_gz_file, destination_dir)