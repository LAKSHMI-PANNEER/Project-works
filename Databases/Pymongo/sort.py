import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

mydoc = mycol.find().sort("name",1)

for x in mydoc:
  print(x)
