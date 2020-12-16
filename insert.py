import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Lakshmi"]
mycol = mydb["employee"]

mylist = [
  { "_id": 1, "name": "John", "salary": "90000"},
  { "_id": 2, "name": "Peter", "salary": "50000"},
  { "_id": 3, "name": "Amy", "salary": "45000"},
  { "_id": 4, "name": "Hannah", "salary": "25000"},
  { "_id": 5, "name": "Michael", "salary": "60000"},
  { "_id": 6, "name": "Sandy", "salary": "50000"},
  { "_id": 7, "name": "Betty", "salary": "72000"},
  { "_id": 8, "name": "Richard", "salary": "30000"},
  { "_id": 9, "name": "Susan", "salary": "55000"},
  { "_id": 10, "name": "Vicky", "salary": "75000"},
  { "_id": 11, "name": "Ben", "salary": "65000"},
  { "_id": 12, "name": "William", "salary": "90000"},
  { "_id": 13, "name": "Chuck", "salary": "50000"},
  { "_id": 14, "name": "Viola", "salary": "40000"}
]

x = mycol.insert_many(mylist)

