import os

# Get the list of files in the current working directory
files = os.listdir()

# Create a list to store file information
file_info_list = []

# Loop through each file and get its details
for file in files:
    if os.path.isfile(file):  # Ensure it's a file, not a directory
        file_info = {
            'path': os.path.join(os.getcwd(), file),
            'size': os.path.getsize(file)
        }
        file_info_list.append(file_info)

# Print the list of dictionaries
print(file_info_list)