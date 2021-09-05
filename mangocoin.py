from typing import final
from easygui.boxes.derived_boxes import ynbox
import pymongo, easygui, time
from random import randint
keepGoing = True
client = pymongo.MongoClient("mongodb+srv://user:daPassword@cluster0.zkpln.mongodb.net/mangoCoin?retryWrites=true&w=majority")
db = client.mangoCoin
daOptions = ["Create account","Manage account","Check balance", "Mine some MangoCoin"]
response = easygui.buttonbox(choices=daOptions,msg="Welcome to MangoCoin! Select an option to get started")


if response == daOptions[0]:
    # Create account
    acctID = randint(111111,999999)
    db.accounts.insert_one({"accountID":acctID,"coins":0})
    easygui.msgbox("Account created! Your account ID is "+str(acctID)+" If you lose your account ID there is no way to recover your account! Do not share your account ID with anyone!")


if response == daOptions[1]:
    # Manage account
    easygui.msgbox("UNDER CONSTRUCTION!!!")


if response == daOptions[2]:
    # Balance
    name = easygui.enterbox("Enter your account ID to check your balance")
    try:
        name = int(name)
    except:
        easygui.msgbox("Account ID must be a number!")
        keepGoing = False
    if keepGoing == True:
        info = db.accounts.find_one({"accountID":name})
        try:
            bal = info["coins"]
        except(TypeError):
            easygui.msgbox("Account not found!")
        easygui.msgbox(str(bal))


if response == daOptions[3]:
    # Mine mangocoin
    finalAmnt = 0
    yesOrNo = easygui.ynbox("How it works: Once you start mining, this program will disappear and the MangoCoin Miner will run in the background until it has mined some MangoCoin, once some MangoCoin has been mined you will be shown the amount and asked if you want to continue mining or stop mining. When you stop mining, the MangoCoin you have mined will be deposited to your account. Would you like to start mining now?")
    if yesOrNo == True:
        acctID = easygui.enterbox("Enter your account ID to begin mining")
        try:
            acctID = int(acctID)
        except:
            easygui.msgbox("Account ID must be a number!")
            keepGoing = False
        if keepGoing == True:
            while True:
                time.sleep(randint(10,60))
                amntMined = randint(0,3)
                if amntMined == 0:
                    amntMined = 0.5

                if amntMined == 1:
                    amntMined = 1

                if amntMined == 2:
                    amntMined = 1.5

                if amntMined == 3:
                    amntMined = 2
                yesOrNo = easygui.ynbox(str(amntMined)+" has been mined! Would you like to keep mining?")
                finalAmnt = finalAmnt + amntMined
                if yesOrNo == False:
                    break
            info = db.accounts.find_one({"accountID":acctID})
            try:
                bal = info["coins"]
            except(TypeError):
                easygui.msgbox("Account not found!")
            db.accounts.update_one({"accountID":acctID},{"$set": {"coins":bal+finalAmnt}})
            easygui.msgbox(str(finalAmnt)+" has been deposited to your account!")