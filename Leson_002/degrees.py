# 2.3[14]: Требуется вывести все целые степени двойки (т.е. числа вида 2^k), не превосходящие числа N.

def Degrees(a=10):
    numb=1
    while True:
        degrees = pow(2,numb)
        if degrees>a:
            break
        else:
            print(degrees, end=', ')
        numb+=1
    print("")

Degrees()
Degrees(1000)




# [print(i, end=' ') for i, j in enumerate(' ' * 10, 1)]
# [print(i[0], end=' ') for i in enumerate(' ' * 10, 1)]
# print(' '.join(str(i) for i in range(1, 101)))

# i = 1
# while i < 102:
#     print(i, end=', ')
#     i += 1

