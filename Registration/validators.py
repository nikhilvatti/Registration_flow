

from flask import request
from marshmallow import validates,ValidationError,validates_schema
from Registration.user_repository import collection_records


@validates("first_name")
def validate_first_name(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces enter a valid first_name")

@validates("email")
def email_checking(value):
    mail_finding_in_records=collection_records.find({"email":value})
    if len(list(mail_finding_in_records))!=0:
        raise ValidationError("Mail already exists in the database records")

@validates("email")
def email_required(value):
    mail_finding_in_records=collection_records.find({"email":value})
    if len(list(mail_finding_in_records))==0:
        raise ValidationError("Mail not exists in the database records")


@validates("last_name")
def validate_last_name(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces enter a valid last_name")

@validates("company_name")
def validate_company_name(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces enter a valid company_name")
    
@validates("industry_name")
def validate_industry_name(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces enter a valid industry_name")
    
@validates("incentive_type")
def validate_incentive_type(value):
    if value.isspace():
        raise ValidationError("Dont enter spaces enter a valid incentive_type")

@validates("confirm_password")
def validate_match_password(value):
    if value!=request.json["password"]:
        raise ValidationError("password not matched")

