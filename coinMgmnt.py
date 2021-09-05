import pymongo, easygui

adminKeys = ["daAdmin"]
adminKey = easygui.enterbox("Before you can modify database record you need to enter your MangoCoin Administration Key")

if adminKey not in adminKeys:
    easygui.msgbox("lol, trying to hack the system? back off, its not gonna happen")
if adminKey in adminKeys:
    client = pymongo.MongoClient("mongodb+srv://user:daPassword@cluster0.zkpln.mongodb.net/mangoCoin?retryWrites=true&w=majority")
    db = client.mangoCoin
    user = easygui.enterbox("What account would you like to modify?")
    user = int(user)
    coins = easygui.enterbox("How many MangoCoins should this account have?")
    coins = float(coins)
    db.accounts.update_one({"accountID":user},{"$set": {"coins":coins}})