import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

#myquery = { "name": { "$regex": "^V" } }

myquery = { "salary": { "$lt": "50000" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)










