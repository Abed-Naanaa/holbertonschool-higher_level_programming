#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Converts the data from a CSV file into a JSON format and saves it to data.json.

    Args:
        csv_filename (str): The name of the CSV file to be converted.

    Returns:
        bool: True if conversion is successful, False if an error occurs.
    """
    try:
        # Open the CSV file for reading
        with open(csv_filename, mode='r') as csv_file:
            # Create a CSV DictReader object to read the CSV file
            csv_reader = csv.DictReader(csv_file)

            # Convert the CSV data into a list of dictionaries
            data = [row for row in csv_reader]

        # Serialize the data to JSON format and write it to data.json
        with open('data.json', mode='w') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except FileNotFoundError:
        # Return False if the CSV file is not found
        print(f"Error: The file '{csv_filename}' was not found.")
        return False
    except Exception as e:
        # Catch other exceptions and print the error
        print(f"An error occurred: {e}")
        return False
