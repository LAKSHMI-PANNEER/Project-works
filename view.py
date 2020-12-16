import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["Things"]

for x in mycol.find():
    print(x)
