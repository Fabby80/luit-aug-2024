import os  # Importing the os module to interact with the operating system

# Create a list of dictionaries containing file paths and their sizes
file_info = [
    {
        'path': f,                    # Store the file name as the path
        'size': os.path.getsize(f)    # Get and store the file size in bytes
    }
    for f in os.listdir()             # Iterate over all items in the current directory
    if os.path.isfile(f)              # Filter out directories, keeping only files
]

# Iterate through the list of file information dictionaries
for element in file_info:
    # Print each file's information in a readable format
    print(element)