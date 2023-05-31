# 2.1[10]: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть. Количество монет и их положение (0 или 1) пользователь вводит с клавиатуры.
# Примеры/Тесты:
# Введите кол-во монет>? 5
# Положение монеты 0: 0 или 1>? 1
# 1 0 1 1 0
# Кол-во монет, чтобы перевернуть: 2


# import random
# massiv_of_pieces = [random.randint(0,1) for i in range(25)]
def Pieces():
    massiv_of_pieces =[]
    while True:
        try:
            i = int(input("input numb 1 or 0: "))
        except ValueError:
            print("you wrote not number")
            # continue
        if i == 1 or i == 0:
            massiv_of_pieces.append(i)
        else:
            break
    print(massiv_of_pieces)
    zerro = massiv_of_pieces.count(0)
    one = massiv_of_pieces.count(1)
    if zerro < one:
        print(f"quantity of flips = {zerro}")
    else:
        print(f"quantity of flips = {one}")


Pieces()