from pymongo import MongoClient

client = MongoClient()
db = client.uds  
collection = db.DF
f = open('check.txt')
text = f.read()

#text_file_doc = {"file_name": "check.txt", "contents" : text }

DF_ins = { 
        "fname":"check.txt",  
        "content":text
        } 

if(collection.insert(DF_ins)):
    print("insertion successful")


