import zipfile
import os

def delete_non_mp4_files(zip_file_path):
    # Check if the file exists
    if not os.path.exists(zip_file_path):
        print("Error: The specified ZIP file does not exist.")
        return

    # Create a new ZIP file to copy the valid files
    new_zip_file_path = zip_file_path.replace('.zip', '_filtered.zip')

    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        with zipfile.ZipFile(new_zip_file_path, 'w') as new_zip_ref:
            # Get list of files in the ZIP archive
            file_list = zip_ref.namelist()

            # Iterate over each file in the ZIP archive
            for file_name in file_list:
                # Check if the file is an MP4 file
                if file_name.lower().endswith('.mp4'):
                    # Read the file content
                    file_content = zip_ref.read(file_name)
                    # Write the file to the new ZIP archive
                    new_zip_ref.writestr(file_name, file_content)

    print("Deletion completed. Filtered ZIP file created:", new_zip_file_path)

if __name__ == "__main__":
    # Input the path of the ZIP file
    zip_file_path = input("Enter the path of the ZIP file: ")

    # Delete non-MP4 files from the ZIP file
    delete_non_mp4_files(zip_file_path)