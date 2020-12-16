import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["Lakshmi"]

print(myclient.list_database_names())

dblist = myclient.list_database_names()
if "Lakshmi" in dblist:
  print("The database exists.")

mycol = mydb["employee"]

print(mydb.list_collection_names())

collist = mydb.list_collection_names()
if "employee" in collist:
  print("The collection exists.")
