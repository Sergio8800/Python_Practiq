# Написать функцию, которая принимает строку текста и проверяет ее ритм (по Винни-Пуху)
# Если ритм есть, функция возвращает True, иначе возвращает False
#
# Примеры/Тесты:
#     <function_name>("пара-ра-рам рам-пам-папам па-ра-па-дам") -> True
#     <function_name>("пара-ра-рам рам-пум-пупам па-ре-по-дам") -> True
#     <function_name>("пара-ра-рам рам-пуум-пупам па-ре-по-дам") -> False
#     <function_name>("Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па") -> False
#     <function_name>("Пам-парам-пурум Пум-пурум-карам") -> True

s1 = "пара-ра-рам рам-пам-папам па-ра-па-дам"
s2 = "Трам-пара-папам-парам-па-пам-пам-па Пум-пурум-пу-пурум-трам-пам-па"
s3 = "Пам-парам-пурум Пум-пурум-карам"


def vini(st: str):
    data = 'аоуе'
    arr = []
    result = st.split(' ')
    for i in result:
        count = 0
        for j in i:
            if j in data:
                count += 1
        arr.append(count)
    if max(arr) != min(arr):
        return False
    return True


def vini2(string: str, bol=True):
    string_new = string.split(' ')
    data = 'аоуе'
    result_comm = list()
    for i in string_new:
        result = []
        for j in range(len(data)):
            count = 0
            for k in range(len(i)):
                if data[j] == i[k]:
                    count += 1
            if count > 0:
                result.append((data[j], count))
        result_comm.append(result)
    result_false = vini(string)
    if bol == True:
        return print(result_comm)
    return print(result_false)


vini2(s1)
vini2(s2)
vini2(s1, False)
vini2(s2, False)
vini2(s3)


def vini3(string: str, bol=True):
    list_comm = []
    str1 = string.split(' ')
    bool = True
    for i in str1:
        dict = {"а": 0, "о": 0, "у": 0, "е": 0}
        for j in i:
            if j in dict.keys():
                dict[j] += 1
        for key, val in dict.items():
            if val != 0:
                list_comm.append((key, val))
    for i in range(len(list_comm) - 1):
        if list_comm[i] != list_comm[i + 1]:
            bool = False
    if bol == False:
        return bool
    return list_comm, bool


print(vini3(s1))
print(vini3(s2))
print(vini3(s3, False))
