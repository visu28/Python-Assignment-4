# Python-Assignment-4
# File Handling Examples in Python

This repository contains two Python programs that demonstrate basic file handling operations.

## Files

### file1.py

This is a simple Python script that demonstrates basic file reading operations.

**Functionality:**
- Opens a file named "sample.txt" in read mode
- Reads the entire content of the file
- Prints the content to the console
- Closes the file

**Usage:**
1. Ensure "sample.txt" exists in the same directory
2. Run the script: `python file1.py`

### file2.py

This is a more comprehensive Python script that demonstrates various file operations including writing, appending, and reading.

**Functions:**
1. `write_to_file(filename, data)`:
   - Writes data to a specified file (overwrites existing content)
   - Uses 'w' mode to open the file

2. `append_to_file(filename, data)`:
   - Appends data to a specified file (preserves existing content)
   - Uses 'a' mode to open the file

3. `read_file(filename)`:
   - Reads and returns the content of a specified file
   - Uses 'r' mode to open the file

**Main Program Flow:**
1. Takes user input and writes it to "output.txt"
2. Takes additional user input and appends it to the same file
3. Reads and displays the final content of the file

**Usage:**
1. Run the script: `python file2.py`
2. Follow the prompts to enter text

### Sample Files

- **sample.txt**: Contains sample text used by file1.py
- **output.txt**: Example output file created by file2.py

## Requirements

- Python 3.x
- No additional libraries required

## Notes

- All files are expected to be in the same directory as the scripts
- The scripts handle basic file operations but don't include extensive error handling
