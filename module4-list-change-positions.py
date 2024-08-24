# Prompt the user to enter the first number and store it in the variable 'first'
first = input('Enter first number: ')

# Prompt the user to enter the second number and store it in the variable 'second'
second = input('Enter second number: ')

# Print the values of 'first' and 'second' before swapping
print('Before swapping:', first, second)

# Swap the values of 'first' and 'second' using tuple unpacking
first, second = second, first

# Print the values of 'first' and 'second' after swapping
print('After swapping:', first, second)
