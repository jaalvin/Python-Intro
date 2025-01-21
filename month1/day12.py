#A script that reads a JSON file and prints out specific values based on user input.
import json

def read_json_file(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("The file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None

def print_specific_value(data, key):
    if key in data:
        print(f"The value for '{key}' is: {data[key]}")
    else:
        print(f"Key '{key}' not found in the JSON data.")

if __name__ == "__main__":
    # Get the filename from the user
    filename = input("Enter the filename of the JSON file: ")
    
    # Read the JSON file
    data = read_json_file(filename)
    
    if data:
        # Get the key from the user
        key = input("Enter the key to find in the JSON data: ")
        
        # Print the specific value
        print_specific_value(data, key)
