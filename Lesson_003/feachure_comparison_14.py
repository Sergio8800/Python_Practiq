# Задача 14
# Ваша решение в рекомендации элегантное, я усложнил своё решение.
n = int(input())
i = 0
while 2 ** i <= n:
    print(2 ** i)
    i += 1

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