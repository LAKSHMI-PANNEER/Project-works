import pandas as pd 
data = pd.read_csv("D:\iris_new.csv") 
data['col5'] = data['col5'].replace(['Iris-setosa'],'1')
data['col5'] = data['col5'].replace(['Iris-versicolor'],'-1')
data['col5'] = data['col5'].replace(['Iris-virginica'],'-1')
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(data)
