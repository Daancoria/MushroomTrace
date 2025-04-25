# Import necessary modules for date handling, subprocess execution, and file operations
import datetime
import subprocess
import os

# Function to validate the format of a date string
def validate_date_format(date_str):
    try:
        # Attempt to parse the date string in the format YYYY-MM-DD
        return datetime.datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        # Raise an error if the format is incorrect
        raise ValueError("Incorrect date format. Expected format: YYYY-MM-DD")

# Function to open a file in Microsoft Word
def open_with_word(file_path):
    # Use subprocess to open the file with Word
    subprocess.run(['start', 'winword', file_path], shell=True)

# Function to print a document
def print_document(file_path):
    # Use the os module to send the file to the default printer
    os.startfile(file_path, "print")

# Function to save traceability logs to a text file
def save_traceability_logs(traceability_logs, filename="traceability_logs.txt"):
    # Open the specified file in write mode
    with open(filename, "w") as file:
        # Write each log entry to the file
        for log in traceability_logs:
            file.write(log + "\n")
    # Automatically open the saved file for the user
    os.startfile(filename)
