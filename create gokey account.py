import pymongo, easygui
client = pymongo.MongoClient("mongodb+srv://user:daPassword@cluster0.zkpln.mongodb.net/mangoCoin?retryWrites=true&w=majority")
db = client.mangoCoin
db.accounts.insert_one({"accountID":0,"coins":1})