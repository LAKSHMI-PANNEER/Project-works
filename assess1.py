import pandas as pd

data=pd.read_csv("D:\input.csv")

#print("Minimum CO1",data["CO1"].min())
m1=data["CO1"].idxmin(axis=1)
#print("Index containing min CO1",m1)
#print(data["CO2"].min())
m2=data["CO2"].idxmin(axis=1)
#print(m2)
#print(data["CO3"].min())
m3=data["CO3"].idxmin(axis=1)
#print(m3)
#print(data["CO4"].min())
m4=data["CO4"].idxmin(axis=1)
#print(m4)
#print(data["CO5"].min())
m5=data["CO5"].idxmin(axis=1)
#print(m5)
#print(data["CO6"].min())
m6=data["CO6"].idxmin(axis=1)
#print(m6)

print("List of semesters and subjects with low COs:\n")
r1=data.loc[ [m1] , ['Semester','Course','CO1'] ]
print(r1)
r2=data.loc[ [m2] , ['Semester','Course','CO2'] ]
print(r2)
r3=data.loc[ [m3] , ['Semester','Course','CO3'] ]
print(r3)
r4=data.loc[ [m4] , ['Semester','Course','CO4'] ]
print(r4)
r5=data.loc[ [m5] , ['Semester','Course','CO5'] ]
print(r5)
r6=data.loc[ [m6] , ['Semester','Course','CO6'] ]
print(r6)

a=data["CO1"].min()
b=data["CO2"].min()
c=data["CO3"].min()
d=data["CO4"].min()
e=data["CO5"].min()
f=data["CO6"].min()

dict = {
  "CO1": a,
  "CO2": b,
  "CO3": c,
  "CO4": d,
  "CO5": e,
  "CO6": f,
}
#print(dict)

print("\nCOs in sorted order\n")

for key, value in sorted(dict.items(), key=lambda item: item[1]):
    print("%s: %s" % (key, value))
    
