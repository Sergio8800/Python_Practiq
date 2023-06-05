# Задача 10
# в моем решении не дочитал условие задачи, поэтому ввод нуля и еденицы произодится с клавиатуры бесконечно, пока человек
# введет другую циру. Добавил перехват ошибки ввода, если человек введет буквы. Использовал встроенную функцию Пайтон,
# как вы рекомендовали на практике. Скопировал функцию - вставил после вашей рекомендации.

# ваша рекомендация
n = int(input())
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input())
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


# моя функция
def Pieces():
    massiv_of_pieces = []
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
