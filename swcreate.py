import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["246033"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "246033" in dblist:
  print("The database exists.")

mycol = mydb["software"]

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "software" in collist:
  print("The collection exists.")
