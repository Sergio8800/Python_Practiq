# 3.1[16]: Дан список целых чисел. Требуется вычислить, сколько раз встречается некоторое число X в этом списке.
# Пользователь вводит число X с клавиатуры. Список можно считать заданным.
# Если такого числа в списке нет - вывести -1.
# Примеры/Тесты:
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 3
# Output:  2
# Input:   [10, 5, 7, 3, 3, 0, 5, 7, 2, 8], x = 20
# Output:  -1
list_1 = [10, 5, 7, 3, 3, 0, 5, 7, 2, 8]


def list_data(arr, a):
    count = 0
    for i in range(len(arr)):
        if a == arr[i]:
            count += 1
    return count


print(list_data(list_1, 3))
# или методами списка:
print(list_1.count(3))
# тернальный оператор
summ = len([i for i in range(len(list_1)) if list_1[i] == 3])
print(summ)
