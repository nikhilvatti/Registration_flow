
from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv

def create_app():
    
    app=Flask(__name__)
    
    api=Api(app,doc="/swagger")

    app.config["JWT_SECRET_KEY"]=os.getenv("JWT_SECRET_KEY")
    
    jwt=JWTManager(app)
    
    from Registration.user_controller import registration_namespace
    api.add_namespace(registration_namespace)

    return app