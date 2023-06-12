# 5.2[28]: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(0,0) -> 0
# <function_name>(0,2) -> 2
# <function_name>(3,0) -> 3


def recur_sum(a: int, b: int) -> int:
    if a <= 0 and b <= 0:
        return 0
    return 1 + recur_sum(a - 1, b - 1)

print("======работает только если одно из чисел == 0 ==========")
print(recur_sum(5, 0))
print(recur_sum(0, 10))


def recur_one_number(a: int):
    if a == 0:
        return 0
    return 1 + recur_one_number(a - 1)


def recur_function(a, b):
    num1 = recur_one_number(a)
    num2 = recur_one_number(b)
    return print(f"summa = {num2 + num1}")

print("только так смог решить сумму двух любых чисел")
recur_function(5, 15)


def sum(a, b):
    return (sum(a + 1, b - 1) if b else a)

print(sum(5,2))


def summa(a, b):
    a += 1
    b -= 1
    print(a,b)
    if b > 0:
        return summa(a, b)
    else:
        return a

print(summa(3, 5))

