
from flask_restx import Namespace,Resource
from flask import request
from flask_accepts import accepts,responds
from Registration.user_schema import *
from werkzeug.security import generate_password_hash,check_password_hash
from Registration.user_repository import UserRegistration
from flask_jwt_extended import jwt_required,get_jwt_identity
from datetime import datetime
from werkzeug.exceptions import BadGateway

registration_namespace=Namespace("registration",description="namsepace for registration")

@registration_namespace.route("/register")
class Registration(Resource):
    @accepts(schema=UserSignup,api=registration_namespace)
    @responds(schema=registration_compeleted,api=registration_namespace)
    def post(self):
        data=request.json        
        hash_password=generate_password_hash(data["password"])
        data["password"]=hash_password
        data.pop("confirm_password")
        data["created_at"]=str(datetime.now())
        data["created_by"]=str(data["email"])

        result=UserRegistration.insert_user_into_database(self,data)        
        return result
    
    def get(self):
        result=UserRegistration.get_all_records(self)
        return result
    
    @accepts(schema=ForgetPassword,api=registration_namespace)
    def put(self):
        data=request.json
        hash_password=generate_password_hash(data["email"])
        result=UserRegistration.update_password_by_mail(self,data,hash_password)
        return result    

@registration_namespace.route("/login")
class Login(Resource):
    @accepts(schema=LoginWithCredientials,api=registration_namespace)
    @responds(schema=loginResponds,api=registration_namespace)
    def get(self):
        data=request.json
        result=UserRegistration.login_with_credientials(self,data["email"],data["password"])
        return result

@registration_namespace.route("/login/update")
class Update(Resource):
    @jwt_required()
    @accepts(schema=UpdateUserData,api=registration_namespace)
    def put(self):
        data=request.json
        id=data.pop("id")
        token_user=get_jwt_identity()
        user_verifiy=UserRegistration.matching_accounts(self,id,token_user.get("email"))
        if user_verifiy=="user verified":
            result=UserRegistration.update_data_by_id(self,id,data)
            return result
        else:
            raise BadGateway("token is not belong to the current user")        