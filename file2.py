# Function to write user input to a file
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)

# Function to append data to the file
def append_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data)

# Function to read and display the content of the file
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

# Main program
if __name__ == "__main__":
    filename = 'output.txt'
    
    # Step 1: Take user input and write it to the file
    user_input = input("Enter some text to write to the file: ")
    write_to_file(filename, user_input + '\n')  # Adding a newline for better formatting

    # Step 2: Append additional data to the same file
    additional_data = input("Enter additional text to append to the file: ")
    append_to_file(filename, additional_data + '\n')  # Adding a newline for better formatting

    # Step 3: Read and display the final content of the file
    final_content = read_file(filename)
    print("\nFinal content of the file:")
    print(final_content)
