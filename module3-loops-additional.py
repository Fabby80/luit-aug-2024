while True:
  answer = int(input('When was python 1.0 released' ))
  if answer > 1994:
    print('it was earlier than that!')
  elif answer < 1994:
    print('it was later than that!')
  else:
    print('Correct')
    break