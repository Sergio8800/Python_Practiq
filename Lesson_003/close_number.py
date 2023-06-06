# 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
# Если в списке несколько чисел "равноблизких" к заданному числу X, то выводим первое встретившееся.
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
list_2 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
list_3 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]

def close_number(arr,a):
    list_start = arr
    list_start.append(a)
    list_start.sort()
    # print(list_2)
    # print(list_2.index(a))
    num1 =list_2.index(a)+1
    num2 = list_start.index(a)-1
    if num1-a == a-num2:
        return print(num2, num1)
    if num1-a>a-num2:
        print(num2)
    else:
        print(num1)

close_number(list_2,9)

# Во 2 задаче, учитывая тему занятия, проще всего было пройтись по списку циклом и посмотреть модуль разницы числа и введенного числа:
# from teacher:
list_2 = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = 6
min_diff = list_2[0]
el = None
for num in list_2:
    if abs(num - x) < min_diff:
        print(min_diff)
        min_diff = abs(num - x)
        el = num
print(min_diff, el)