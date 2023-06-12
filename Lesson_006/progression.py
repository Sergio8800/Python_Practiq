# 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :
#   Первый элемент прогрессии, Разность (шаг) и Количество элементов
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Напишите функцию
# - Аргументы: три указанных параметра
# - Возвращает: список элементов арифмитической прогрессии.
# Примеры/Тесты:
# Ввод: 7 2 5
# Вывод: [7 9 11 13 15]  Comprehension  -   understanding, insight, conception, realization, grasp
#
# def increase(a, b):
#     a = a+b
#     return a
def progres(a,b,c)->list:
    list_result = [a]
    for i in range(c-1):
        a = a+b
        list_result.append(a)
    return list_result

def progres2(a,b,c)->list:
    list_result = [a+b*i for i in range(c)]
    return list_result
print(progres(1,2,11))
print(progres2(1,2,11))

a,b,c = list(map(int, input("input tree numbers using backspace:").split()))
print([a+b*i for i in range(c)])

