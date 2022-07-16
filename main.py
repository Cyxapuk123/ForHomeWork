talon = ''
nom = 1
while talon != '1':
    talon = input('Введите 0 — получить талон, 1 — выключить аппарат-->')
    if talon == '0':
        print(nom)
        nom += 1

