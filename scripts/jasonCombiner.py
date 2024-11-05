import json

def combine_json():
    """
    This functiosn combines my json files in case I want to add new data
    """
    # Ask user for JSON file paths
    json_file1_path = input("Enter the path of the first JSON file: ")
    json_file2_path = input("Enter the path of the second JSON file: ")
    output_json_path = input("Enter the path for the combined JSON file: ")

    # Load first JSON file
    with open(json_file1_path, 'r') as file1:
        json_data1 = json.load(file1)

    # Load second JSON file
    with open(json_file2_path, 'r') as file2:
        json_data2 = json.load(file2)

    # Combine JSON data
    combined_json = {**json_data1, **json_data2}

    # Write combined JSON to output file
    with open(output_json_path, 'w') as outfile:
        json.dump(combined_json, outfile, indent=4)

if __name__ == "__main__":
    combine_json()