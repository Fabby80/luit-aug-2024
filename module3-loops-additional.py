answer_a = int(input('Try to guess the first number: '))
 
if answer_a == 8:
    answer_b = int(input('Correct! Now, guess the second number: '))
    if answer_b == 5:
        print('You won!')
    else:
        print('You only got one number right. So close!')
else:
    print('Wrong!')