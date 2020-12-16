import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

myquery = { "salary": "40000" }
newvalues = { "$set": { "salary": "45000" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)
