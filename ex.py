number = int(input('ввести последнюю версию:'))
i = 1
x = '1'
while True:
  len_str = len(str(abs(number)))
  y = len_str * x
  y = int(y)
  if number < y:
    len_str = len_str - 1
    y = len_str * x
    y = int(y)
    print('Y:', y)
  number = number - y
  print('Это number:', number)
  if number >= y:
    i += 1
  else:
    print('I:', i)
    break