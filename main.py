import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/") #stream de conexão
mydb = myclient["Aula5DB"]
mycol = mydb["customers"]

mydict = { "nome" : "andre", "email": "andre@teste.com", "telefone" : "16 8888 7777"}

x = mycol.insert_one(mydict)

print(x.inserted_id)

