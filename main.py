for i in range(3):
  prom = input('Введите промокод -->')
  if prom != 'fresh':
    print('Неверный промокод')
  else:
    print('Верный промокод')
    print(i + 1)
    break

