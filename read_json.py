import json

def read_json_file(filename):
    """Read JSON file and return its contents."""
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

def main():
    filename = 'data.json'  # Change this to your JSON file's name
    json_data = read_json_file(filename)
    print("Contents of JSON file:")
    print(json.dumps(json_data, indent=4))  # Pretty print JSON data

if __name__ == "__main__":
    main()
