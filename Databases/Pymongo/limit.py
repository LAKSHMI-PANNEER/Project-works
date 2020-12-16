import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

myresult = mycol.find().limit(5)

for x in myresult:
  print(x)
