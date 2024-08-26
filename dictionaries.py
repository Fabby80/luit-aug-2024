# A dictionary containing English words as keys and their German translations as values
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

# Start an infinite loop to continuously prompt the user for input
while True:
    # Prompt the user to enter a word in English or type 'EXIT' to quit
    user_input = input('Enter a word in English or EXIT: ')
    
    # Check if the user wants to exit the loop
    if user_input == 'EXIT':
        break  # Exit the loop if the user types 'EXIT'
    
    # Check if the user input is in the dictionary
    if user_input in sample_dict:
        # If the word is found in the dictionary, print its translation
        print('Translation:', sample_dict[user_input])
    else:
        # If the word is not found, inform the user that there's no match
        print('No match!')

# Print a farewell message after the loop ends
print('Bye!')
