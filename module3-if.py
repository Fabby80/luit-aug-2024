user_age = int(input('What is your age: '))
if user_age > 30:
  print('you are over 30 years of age')
  print ('sorry, you do not qualify')
elif user_age == 30:
  print('You are exactly 30 years old')
  print('you will need to meet additional conditions to qualify')
else:
  print('you are 30 years old or younger')
  print('Congratulations, you qualify')