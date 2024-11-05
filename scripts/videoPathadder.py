def append_filename_to_path(file_path):
    # Split the file path by '/'
    parts = file_path.split('/')

    # Get the last part which is the filename
    filename = parts[-1]

    # Define the new path string
    new_path = "/your/new/path/{}".format(filename)

    return new_path

