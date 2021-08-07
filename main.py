import pandas as pd
import numpy as np

df = pd.read_csv("~\\GITHUB\\pandas_car_data\\Automobile_data.csv", na_values={
'price':["?","n.a"],
'stroke':["?","n.a"],
'horsepower':["?","n.a"],
'peak-rpm':["?","n.a"],
'average-mileage':["?","n.a"]})

print (df)

df.to_csv("~\\GITHUB\\pandas_car_data\\Automobile_data.csv")

df['average-mileage'].isnull().values.any()