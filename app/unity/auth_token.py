from main import app

import jwt

class Auth_token():

    @staticmethod
    def generate_auth_token(info):
        print info
        print type(info)
        info = dict(info)
        token = jwt.encode(info, app.config['SECRET_KEY'], algorithm='HS256')
        return token 

    @staticmethod
    def verify_auth_token(token):
        data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return data 
