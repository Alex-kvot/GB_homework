n = int(input("Введите количество журавликов: "))

if n % 6 == 0:
    print('Петя =', int(n/6), 'Катя =', int(n/3)*2, 'Сережа =', int(n/6))
else:
    print('Данные для решения задачи не корректны')