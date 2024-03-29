
from pymongo import MongoClient
from flask import json, jsonify
from bson import json_util
from werkzeug.security import check_password_hash
import jwt
import os
from dotenv import load_dotenv
from datetime import datetime,timedelta
from flask_jwt_extended import create_access_token,create_refresh_token
from werkzeug.exceptions import BadRequest
from bson.objectid import ObjectId

load_dotenv()

secret_key=os.getenv("SECRET_KEY")

database=MongoClient("mongodb://localhost:27017").Registration
collection_records=database.customers

class collection_record_selection:
    def __init__(self,collection):
        self.collection_record=collection

manual_entered_collection_records=collection_record_selection("employee").collection_record
manual_enter_database=database.manual_entered_collection_records


class UserRegistration():
    def insert_user_into_database(self,data):
        insert_record=collection_records.insert_one(data)
        data.pop("password")
        data.pop("_id")
        payload={"data":data,"exp":datetime.utcnow()+timedelta(minutes=10)}
        
        access_token=jwt.encode(payload,secret_key,algorithm="HS256")
        
        refresh_token=create_refresh_token(identity=data)
            
        message="Registered successfully"
        return {"access_token":access_token,"message":message,"refresh_token":refresh_token}
    
    def update_password_by_mail(self,data,password):
        update_password=collection_records.update_one({"email":data["email"]},{"$set":{"password":password}})
        return {"msg":"Password updated successfully"}
        
    
    def get_all_records(self):
        records=list(collection_records.find({},{"$toString":"$_id"}))
        return json.loads(json_util.dumps(list(records)))
    
    def login_with_credientials(self,email,password):
        records=collection_records.find({"email":email})
        pass1=[record.get("password") for record in records][0]
        hash_match=check_password_hash(pass1,password)
        if hash_match:
            records=collection_records.find({"email":email})
            record=list(records)[0]
            record.pop("_id")
            record.pop("password")
            created_access_token=create_access_token(identity=record,fresh=True)
            refresh_token=create_refresh_token(identity=record)
            return {
                "access_token":created_access_token,
                "refresh_token":refresh_token,
                "message":"Loggined successfully"
            }
        else:
            raise BadRequest("Invalid password")
    def update_data_by_id(self,id,data):
        data["updated_at"]=str(datetime.now())
        records=collection_records.update_one({"_id":ObjectId(id)},{"$set":data})
        return f"{list(data.keys())} updated successfully"
    
    def matching_accounts(self,id,mail):
        record=collection_records.find({"_id":ObjectId(id)})
        if record[0].get("email")==mail:
            return {"msg":"user verified"}
        else:
            return {"msg":f"token is not belongs to {record[0].get('email')} user"}