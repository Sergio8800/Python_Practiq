# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте. Не обязательно вводить их с клавиатуры,
# можно задать непосредственно в коде программы
# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7
# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1
list1 = [11, 92, 1, 42, 15, 12, 11, 81]
list2 = [111, 192, 291, 142, 155, 212, 211, 181]

def blueberry(arr):
    maximum = dict()
    for index, val in enumerate(arr):
        if index == 0:
            maximum[index] = arr[0] + arr[index + 1] + arr[-1]
            continue
        if index == len(arr) - 1:
            maximum[index] = arr[len(arr) - 1] + arr[len(arr) - 2] + arr[0]
            continue
        maximum[index] = arr[index] + arr[index - 1] + arr[index + 1]

    max_el = max(maximum.values())
    inx_max_el = {f"index of maximum element = {inx}": f"quantity generale = {val}"
                  for inx, val in maximum.items() if val == max_el}
    res_max = inx_max_el
    return print(res_max)


blueberry(list1)
blueberry(list2)
