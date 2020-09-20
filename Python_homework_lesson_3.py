# 1. В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел. Если компьютер угадал число, игрок выбирает
# “победа”. Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.
# Примечание: Знаки “=”, “>” и “<” пользователь вводит с клавиатуры для общения с компьютером. Вы можете использовать
# этот способ или придумать свой.

import random

a = 0
b = 100
answer = input(f'Загадайте число от {a} до {b}: ')
while True:
    number = random.randint(a,b)
    answer = input(f'{number}? Напишите >, < или =')
    if answer == '=':
        print('Победа!')
        break
    elif answer == '>':
        a = number + 1
    elif answer == '<':
        b = number - 1
    else:
        print('Неизвестная команда')