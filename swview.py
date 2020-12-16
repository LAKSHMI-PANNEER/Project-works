import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["246033"]
mycol = mydb["software"]

for x in mycol.find():
  print(x)
