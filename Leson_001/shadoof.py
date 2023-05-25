# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок,
# если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4

def Shadoof(a=96):
    if a == int(a):
        one_part = a/6
        Katy_quantity_of_shadoof = one_part*4
        Pety = Serg = one_part
    else:
        return print("used natural number")
    return print(f"Katy done {Katy_quantity_of_shadoof} shadoofs, Pety done {one_part} Serg done{one_part} ")
Shadoof()
Shadoof(33.3)