import requests
response = requests.get('https://api.github.com')
print(response.json())
print("\n Код requests завершён \n")

 

import pandas as pd


data = [{'name': 'Денис', 'age': 30}, {'name': 'Макс', 'age': 25}]
df = pd.DataFrame(data)

print(df)
print()


older_than_25 = df[df['age'] > 25]
print(older_than_25)
print()


grouped_by_age = df.groupby('age')
print(grouped_by_age)
print()


sorted_df = df.sort_values(['age'], ascending=False)
print(sorted_df)
print()


total_ages = df['age'].sum()
print(f"Сумма возрастов: {total_ages}")
print("\n Код pandas завершён \n")


import numpy as np

a = np.arange(10)
print(a)
print()

b = np.random.rand(5, 5)
print(b)
print()


a = np.arange(10)
b = np.ones(10) * 3
c = a + b
print(c)
print()


d = np.arange(9).reshape(3, 3)
e = np.ones((3, 3))
f = d * e
print(f)
print("\n Код NumPy завершён \n")

 