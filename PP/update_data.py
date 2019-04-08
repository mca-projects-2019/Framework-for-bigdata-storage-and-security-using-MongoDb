from pymongo import MongoClient
from pprint import pprint


client = MongoClient()
db=client.test


student = db.student

db.student.update_one(
        {"Age":'24'},
        {
        "$set": {
            "Name":"Srinidhi",
            "Age":'25',
            "Address":"CCVB Home, House No:45"
        }
        }
    )

Queryresult = student.find_one({'Age':'35'})

print(Queryresult)