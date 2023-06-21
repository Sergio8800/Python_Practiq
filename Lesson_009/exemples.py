import pandas as pd

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})


def square(x):
    return x * x
# df1 = df.apply(lambda x: x * x)

df1 = df.apply(square)

print(df)
print(df1)


import numpy as np

df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

df1 = df.apply(np.sum, axis=0)
print(df1)

df1 = df.apply(np.sum, axis=1)
print(df1)

#принимает более одного параметра
def sum(x, y, z):
    return x + y + z


df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

df1 = df.apply(sum, args=(1, 2))
print(df1)

def sum(x, y, z, m):
    return (x + y + z) * m


df = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

df1 = df.apply(sum, args=(1, 2), m=10)
print(df1)
# ApplyMap (). Эта функция не имеет дополнительных аргументов.
# Функция применяется к каждому из элементов, и возвращаемое значение используется для создания объекта DataFrame результата.
import pandas as pd
import math

df = pd.DataFrame({'A': [1, 4], 'B': [100, 400]})
df1 = df.applymap(math.sqrt)

print(df)
print(df1)