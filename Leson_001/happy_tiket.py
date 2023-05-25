# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу,
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
from datetime import datetime
from threading import Thread # просто использую, что бы не забыть, т.к. для этой задачи не актуально

def Happy_tiket(a):
    string_data = str(a)
    quantity_start = quantity_finish = 0
    slice_start = string_data[:len(string_data) // 2]
    slice_finish = string_data[len(string_data) // 2:len(string_data)]
    for i in slice_start:
        quantity_start += int(i)
    for i in slice_finish:
        quantity_finish += int(i)
    if quantity_finish == quantity_start:
        print("Bingo! You are Winner!")
    print(f" первая половина {quantity_start}")
    print(f" вторая половина {quantity_finish}")

thread = Thread(target=Happy_tiket, args=(385916,))
thread.start()




# thread = Thread(target=Happy_tiket, args=(222222222222222222222222555555555555555555555555555555555555555555555555,))
# startTime = datetime.now()
# thread.start()
# thread.join()
#
# endTime = datetime.now()
# print ("Время выполнения: ", endTime - startTime)
#
# startTime = datetime.now()
# Happy_tiket(222222222222222222222222555555555555555555555555555555555555555555555555)
#
# endTime = datetime.now()
# print ("Время выполнения: ", endTime - startTime)

