a = int(input('-->'))
b = int(input('-->'))
c = int(input('-->'))
if a > b and a > c:
  print(a)
elif b > a and b > c:
  print(b)
elif c > a and c > b:
  print(c)
else:
  if a == b and a > c:
    print('Числа a, b максимальные')
  elif a == c and a > b:
    print('Числа a, c максимальные')
  elif b == c and b > a:
    print('Числа b, c максимальные')
  else:
    print('Числа равны')