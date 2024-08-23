# List of names of invited guests
invited_guest = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']

# Prompt the user to enter their name and store it in the variable 'name'
name = input('What is your name? ')

# Check if the entered name is in the list of invited guests
if name in invited_guest:
    # If the name is found in the list, print a welcome message
    print('Welcome!')
else:
    # If the name is not found in the list, print a message indicating they are not invited
    print('You are not invited!')