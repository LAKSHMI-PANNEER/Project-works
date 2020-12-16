import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

myquery = { "salary": "90000" }
newvalues = { "$set": { "salary": "95000" } }

mycol.update_one(myquery, newvalues)

for x in mycol.find():
  print(x)
