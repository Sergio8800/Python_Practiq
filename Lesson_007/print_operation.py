# 6.2[32]: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию,
# вычисляющую элемент по номеру строки и столбца, т.е. функцию двух аргументов. Аргументы num_rows и num_columns указывают число строк
# и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы.
# Примеры/Тесты:
# print_operation_table(lambda x,y: x**y,4,4)
# 1   1   1   1
# 2   4   8  16
# 3   9  27  81
# 4  16  64 256
# print_operation_table(lambda x,y: x*y)
# 1   2   3   4   5   6
# 2   4   6   8  10  12
# 3   6   9  12  15  18
# 4   8  12  16  20  24
# 5  10  15  20  25  30
# 6  12  18  24  30  36

def print_operation_table(operation, num_rows=6, num_columns=6):
    return operation(num_rows, num_columns)


def print_table(a, b):
    for i in range(1, a + 1):
        for j in range(i, i * b + 1, i):
            print(j, end=' \t')
        print()


print_operation_table(print_table)
print_operation_table(print_table, 2, 4)


def indend():  # делаем передний отступ
    return print("\t", end='')


def print_beauty(a=6, b=6):
    indend()
    for i in range(1, b + 1):
        st = ''.join(str(i))
        print(st, end='\t')
    print()
    indend()
    print("--" * 2 * b)
    for i in range(1, a + 1):
        print(f"{i}|", end='\t')
        for j in range(1, b + 1):
            print(i * j, end='\t')
        print()


print_operation_table(print_beauty, 5, 5)
