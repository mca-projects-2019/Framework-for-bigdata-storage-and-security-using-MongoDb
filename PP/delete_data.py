from pymongo import MongoClient
from pprint import pprint


client = MongoClient()
db=client.test


student = db.student

db.student.delete_one({"Age":'21'})

Queryresult = student.find_one({'Age':'25'})

print(Queryresult)