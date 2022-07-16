rek = ''
aok = ''
roz = ''
while rek != 'off':
    rek = input('1-рекомендации, 2-розыгрыш, off-выключение-->')
    if rek == '1':
        aok = input('Введите предпочтения-->')
        if aok == 'Спорт':
            print('FIFA 2018 Матч Россия/Испания')
        elif aok == 'Музыка':
            print('саундтреки DOOM')
    elif rek == '2':
         for i in range(3):
             roz = input('За 3 попытки нужно отгадать название музыкальной группы («Queen»).')
             if roz == 'Queen':
                 print('Вы выиграли билет на концерт!')
                 break