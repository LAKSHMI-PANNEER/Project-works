import pandas as pd

data=pd.read_csv("D:\iris_new.csv")

data=data.drop([data.columns[1],data.columns[2],data.columns[3],data.columns[4]],axis='columns')

print("Minimum value in column 1:",data["col1"].min())
print("Maximum value in column 1:",data["col1"].max())
print("\n")
data.sort_values("col1", axis = 0, ascending = True, inplace = True, na_position ='last') 

print("Column 1 is divided into 4 ranges:")
print("Range 1 (contains values less than/equal to 5.0):")
r1 = data[data['col1'] <= 5.0]
print(r1.to_string(index=False))
print("Number of values in range 1:\n",r1.count())
print("\n")

print("Range 2 (contains values from 5.0 to 6.0):")
r2 = data[(data['col1'] > 5.0) & (data['col1'] < 6.0)]
print(r2.to_string(index=False))
print("Number of values in range 2:\n",r2.count())
print("\n")

print("Range 3 (contains values from 6.0 to 7.0):")
r3 = data[(data['col1'] >= 6.0) & (data['col1'] < 7.0)]
print(r3.to_string(index=False))
print("Number of values in range 3:\n",r3.count())
print("\n")

print("Range 4 (contains values greater than/equal to 7.0):")
r4 = data[data['col1'] >= 7.0]
print(r4.to_string(index=False))
print("Number of values in range 4:\n",r4.count())
