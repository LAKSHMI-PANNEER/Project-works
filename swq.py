import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["246033"]
mycol = mydb["software"]

myquery = { "Year": { "$lt": "2020" } }

#myquery = { "name": { "$regex": "^C" } }

mydoc = mycol.find(myquery)

for x in mydoc:
  print(x)










