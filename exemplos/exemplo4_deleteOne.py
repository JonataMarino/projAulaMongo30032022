import pymongo
#test git
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Aula5DB"]
mycol = mydb["customers"]

myquery = {"address": "Mountain 21"}

mycol.delete_one(myquery)