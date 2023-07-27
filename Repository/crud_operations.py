
from Registration.user_repository import manual_enter_database
from bson.objectid import ObjectId

collection_records=manual_enter_database

def insert_one_record(data):
    records=collection_records.find({})
    if len(list(records))==0:
        record=collection_records.insert_one(data)
        return {"msg":"data inserted successfully"}
    else:
        return {"msg":"same record already exists in the database"}

def insert_many_records(data):
    records=collection_records.insert_many(data)
    return {"msg":"Records are inserted successfully"}

def update_one_record(id,data):
    record=collection_records.find({"_id":ObjectId(id)})
    if len(list(record))!=0:
        record=collection_records.update_one({"_id":ObjectId("_id")},{data})
        return {"msg":"record updated successfully"}
    else:
        return {"msg":"Record not exists in the database"}

def update_multi_record(update_query):
    records=collection_records.count_documents({})
    if records!=0:
        records=collection_records.find({},{"$set":{update_query}})
        return {"msg":"Doumnents updated successfully"}

def delete_many_records():
    records=collection_records.count_documents({})
    if records==0:
        records=collection_records.delete_many({})
        return {"msg":"Records deleted successfully"}
    else:
        return {"msg":"No Records are found in the database"}
    

def delete_one_record(id):
    records=collection_records.find({"_id":ObjectId(id)})
    if len(list(records))!=0:
        record=collection_records.delete_one({"_id":ObjectId(id)})
        return {"msg","Record deleted successfully"}
    else:
        return {"msg":"Record not exists in the database"}

