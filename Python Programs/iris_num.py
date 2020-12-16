import pandas as pd 
data = pd.read_csv("D:\iris.csv")
print(data.groupby('col5').size())

