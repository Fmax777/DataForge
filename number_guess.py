print('Игра "Угадай число"')

in_number = int(input("Введите число от 1 до 10: "))
secret = 7

while True:
    if in_number == secret:
        print("Верно! Вы выиграли!")
        break
    elif in_number < secret:
        print("Загаданное число больше.")
    else:
        print("Загаданное число меньше.")
    in_number = int(input("Введите число от 1 до 10: "))