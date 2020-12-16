import pandas as pd 
data = pd.read_csv("D:\iris_csv.csv")
print(data.groupby('Species').size())

