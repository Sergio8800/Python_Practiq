# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

def Chocolate(a,b,k):
    metod_1 = bool(k%a)
    metod_2 = bool(k%b)
    if metod_1 == False or metod_2 == False:
        print("it is possibility ")
    else:
        print("Unfortunately this is not possible ")
print("-----------Start---------")
Chocolate(3,2,1)
Chocolate(3,2,4)