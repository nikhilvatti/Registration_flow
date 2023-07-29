

from flask import request
from marshmallow import validates,ValidationError
from Registration.user_repository import collection_records


@validates(["first_name","last_name","email","company_name","industry_name"])
def checking_spaces(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces in the place of field values")

@validates("email")
def email_checking(value):
    find_user=collection_records.find({"email":value})
    if len(list(find_user))!=0:
        raise ValidationError("user already exists in the database records")
    if value[0].isalpha()==False:
        raise ValidationError("mail startswith only alphabet")

@validates("email")
def email_required(value):
    find_user=collection_records.find({"email":value})
    if len(list(find_user))==0:
        raise ValidationError("user not exists in the database records")
    
@validates("account_type")
def validate_account_type(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces enter a valid account_type")
    if value.lower() not in ["scale_with","give_with"]:
        raise ValidationError("please enter a valid name")

@validates("confirm_password")
def validate_match_password(value):
    if value!=request.json["password"]:
        raise ValidationError("password not matched")

