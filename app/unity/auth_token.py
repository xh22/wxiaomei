from main import app

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, SignatureExpired, BadSignature

class Auth_token():

    @staticmethod
    def generate_auth_token(info, expiration = 6000):
        s = Serializer(app.config['SECRET_KEY'], expires_in = expiration)
        return s.dumps(info)

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None # valid token, but expired
        except BadSignature:
            return None # invalid token
        return data 
