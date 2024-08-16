#avalable logical operators
#
#  <  less than
#  >  greater than
# <= less than or equal
# >= greater than of equal
# == equals
# != not equals

password = input('Do you know the secret password? ')
if password != '--secret':
  print('not correct')
else:
  print('correct password')