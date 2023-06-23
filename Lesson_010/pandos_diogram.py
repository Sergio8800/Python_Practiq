# #10.1[44]: Дан код, генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Статья про one hot вид https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing
#     Сделайте one hot вид с использованием get_dummies
#     Сделайте one hot вид с использованием изученных методов группировки данных. Обратите внимание, что Nan это не ноль.

import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
df = pd.read_csv("Pokemon.csv")
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
# data_ar = ['robot', 'human', np.nan]
print(data.head())
df_2 = pd.get_dummies(data)
print(df_2)
onehot_encoder = OneHotEncoder(sparse_output=False)
new_data = onehot_encoder.fit_transform(df_2)
print(new_data)



