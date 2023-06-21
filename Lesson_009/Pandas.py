# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
# Задача 42: Узнать какая максимальная households в зоне минимального значения population
import pandas as pd

file_name = "https://storage.googleapis.com/mledu-datasets/california_housing_train.csv"
df = pd.read_csv(file_name, on_bad_lines='skip')
tt = df.head()
task1 = df['median_house_value'][df["population"] < 500].mean()
task2 = df[df["households"] == df["households"].max()]["population"].min()
print(f" ответ к первой задаче: {task1} ")
print(f" ответ ко второй задаче: {task2}")

