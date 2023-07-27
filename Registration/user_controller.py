
from flask_restx import Namespace,Resource
from flask import request
from flask_accepts import accepts,responds
from Registration.user_schema import *
from flask import jsonify
from werkzeug.security import generate_password_hash,check_password_hash
from Registration.user_repository import user_registration
import os

registration_namespace=Namespace("registration",description="namsepace for registration")


@registration_namespace.route("/register")
class user_registration_operations(Resource):
    @accepts(schema=user_signup,api=registration_namespace)
    @responds(schema=registration_compeleted,api=registration_namespace)
    def post(self):
        data=request.json        
        hash_password=generate_password_hash(data["password"])
        data["password"]=hash_password
        data.pop("confirm_password")
        res=user_registration.uploading_data_into_database(self,data)        
        return res
    
    def get(self):
        res=user_registration.get_all_records(self)
        return res
    
    @accepts(schema=forget_password,api=registration_namespace)
    def put(self):
        data=request.json
        hash_password=generate_password_hash(data["email"])
        res=user_registration.update_password_by_mail(self,data,hash_password)
        return res    

@registration_namespace.route("/login")
class login_operation(Resource):
    @accepts(schema=login_credientials,api=registration_namespace)
    @responds(schema=loginResponds,api=registration_namespace)
    def get(self):
        data=request.json
        res=user_registration.login_with_credientials(self,data["email"],data["password"])
        return res