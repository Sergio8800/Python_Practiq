# 5.1[26]: Напишите рекурсивную функцию для возведения числа a в степень b. Разрешается
# использовать только операцию умножения. Циклы использовать нельзя
# Примеры/Тесты:
# <function_name>(2,0) -> 1
# <function_name>(2,1) -> 2
# <function_name>(2,3) -> 8
# <function_name>(2,4) -> 16



def recur_degree(num, degree):
    if degree == 1:
        return num
    if degree == 0:
        return 1
    return num*recur_degree(num, degree - 1)

print(recur_degree(2,10))
print(recur_degree(2,0))