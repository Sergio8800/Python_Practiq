# 2.2[12]: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# Примеры/Тесты:
# 4 4 -> 2 2
# 5 6 -> 2 3

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


Mystery(10, 25)
Mystery(12, 25)
Mystery()
