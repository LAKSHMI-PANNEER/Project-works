import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

myquery = { "name": "Ben" }

mycol.delete_one(myquery)
