

from marshmallow import fields,Schema,validate
from Registration.validators import *
checking_spaces
class user_signup(Schema):
    first_name=fields.String(validate=[checking_spaces,validate.Length(min=3,max=50),
                                       validate.Regexp(r'[A-Za-z0-9]',error=("the string will take only alphabetics and digits"))],required=True)
    last_name=fields.String(validate=[checking_spaces,validate.Length(min=3,max=50),
                                      validate.Regexp(r'[A-Za-z0-9]',error=("the string will take only alphabetics and digits"))],required=True)
    email=fields.Email(validate=email_checking,required=True)
    company_name=fields.String(validate=[checking_spaces,validate.Length(min=3,max=50)],required=True)
    account_type=fields.String(validate=[validate_account_type,validate.Length(min=3,max=50)],required=True)
    industry_name=fields.String(validate=[checking_spaces,validate.Length(min=3,max=50)],required=True)
    password = fields.String(
        required=True,
        validate=[
            validate.Length(min=8, max=50),
            validate.Regexp(r'^(?=.*[A-Z])(?=.*[@#$%^&+=])(?=.*[0-9]).*$')
        ],
        load_only=True
    )
    confirm_password=fields.String(validate=validate_match_password,required=True,load_only=True)



class forget_password(Schema):
    email=fields.Email(validate=email_required,required=True)
    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=8, max=50),
            validate.Regexp(r'^(?=.*[A-Z])(?=.*[@#$%^&+=])(?=.*[0-9]).*$')
        ],
        load_only=True
    )
    confirm_password=fields.String(validate=validate_match_password,required=True,load_only=True)

class login_credientials(Schema):
    email=fields.Email(validate=email_required,required=True)
    password = fields.Str(
        required=True,
        validate=[
            validate.Length(min=8, max=50),
            validate.Regexp(r'^(?=.*[A-Z])(?=.*[@#$%^&+=])(?=.*[0-9]).*$')
        ],
        load_only=True
    )
    

class loginResponds(Schema):
    access_token=fields.String(required=True)
    message=fields.String(required=True)
    refresh_token=fields.String(required=True)


class registration_compeleted(Schema):
    access_token=fields.String()
    message=fields.String()
    refresh_token=fields.String()