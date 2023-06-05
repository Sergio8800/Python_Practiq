from datetime import datetime
# Задача 12
# Моя функция, с моей точки зрения, более простая и требует меньше операционных ресурсов.
#я написал простой декоратор, который замеряет время выполнения фукции, разница существенная.

def handler_time(fun):
    def time_count(*args, **kwargs):
        start_time = datetime.now()
        result = fun(*args, **kwargs)
        finish_time = datetime.now()
        print(f"function execution time = {finish_time - start_time} ")
        return result

    return time_count


@handler_time
def Mystery(a=5, b=6):
    num1 = 2
    flag = False
    while num1 < b / 2:
        num2 = int(b / num1)
        if num2 * num1 == b and num1 + num2 == a:
            flag = True
            break
        num1 += 1
    print(f"those numbers are {num2} and {num1}") if flag else print("it is impossible")


@handler_time
def Mystery_ver2(x=5, y=6):
    # x = int(input())
    # y = int(input())
    for i in range(x):
        for j in range(y):
            if x == i + j and y == i * j:
                print(i, j)


if __name__ == "__main__":
    Mystery(1055, 277500)
    Mystery_ver2(1055, 277500)
