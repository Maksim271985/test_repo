

i=input()
s = len(str(i))
while s>8 and i.isupper()==False and i.islower()==False:
  print('Пароль допустимый')
  break
else:
  print('Пароль не допустимый')
  
  