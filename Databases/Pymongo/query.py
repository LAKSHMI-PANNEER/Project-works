import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

#myquery = { "salary": { "$lt": "50000" } }

myquery = { "name": { "$regex": "^V" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)










