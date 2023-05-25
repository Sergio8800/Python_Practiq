# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

def Summa(a=123):
    summa = 0
    print(type(a))
    if a == int(a) and a != bool(a):
        print(f"сумма цифр в числе {a}:")
        while a >= 1:
            summa += a % 10
            a = a // 10
    else:
        return print(f"number {a} is not integer, it is {type(a)}")
    return print(summa)


Summa()
Summa(257)
Summa(34.5)
Summa('345')
Summa(True)
