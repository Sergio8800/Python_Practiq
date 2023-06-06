# 4.1[22]: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Если таких чисел нет - выдать внятное диагностическое сообщение
# Наборы (списки) чисел можно считать заданными и не вводить с клавиатуры
# Примеры/Тесты:
# Input1: 2 4 6 8 10 12 10 8 6 4 2
# Input2: 3 6 9 12 15 18
# Output: 6 12     Обратите внимание: Без скобочек, в одну строку
# Input1: 2 4 6 8 10 10 8 6 4 2
# Input2: 3 9 12 15 18
# Output: Повторяющихся чисел нет

list1 = [2, 4, 5, 10, 12, 10, 8, 6, 4, 2, 1]
list2 = [3, 6, 9, 12, 15, 18, 1]


def ordered(li1, li2):
    result = []
    for i in li1:
        if i not in result and i in li2:
            result.append(i)
    return print(f"кол-во повторяющихся элементов - {sorted(result)}")


ordered(list2, list1)