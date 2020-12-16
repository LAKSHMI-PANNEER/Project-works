import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["246033"]
mycol = mydb["software"]

mylist = [
    
  { "_id": 1, "name": "CODEC", "type": "Programming", "Recent_Version": "1.0.1", "Basic_Distribution": "DEEP Sky Technologies",
    "OS": "MAC", "Year": "2001", "Users": "Public", "Link": "https://download.cnet.com/CODEC/3000-2247_4-7324.html"},
  
  {"_id": 2, "name": "Dev C++", "type": "Programming", "Recent_Version": "5.11", "Basic_Distribution": "Bloodshed",
   "OS": "Windows", "Year": "2015", "Users": "Public", "Link": "https://bloodshed-dev-c.en.softonic.com/"},

  {"_id": 3, "name": "Matlab", "type": "Educational", "Recent_Version": "R2020a", "Basic_Distribution": "MathWorks",
   "OS": "Windows", "Year": "2020", "Users": "Public", "Link": "https://download.cnet.com/Matlab/3000-2053_4-43768.html"}  ]

x = mycol.insert_many(mylist)
