import jwt
from itsdangerous import TimedJSONWebSignatureSerializer


class JWTParser:
    def __init__(self, jwt_token):
        self._jwt_token = jwt_token
        self._public_key = "CLIENTSECRET"
        self._decoded_json = ""

    def decode_access_token(self):
        try:
            decoded_jwt = jwt.decode(self._jwt_token, key=self._public_key, algorithms=['HS256', ])
            decoded_dict = {"username": decoded_jwt['username'],
                            "password": decoded_jwt['password'],
                            "firstname": decoded_jwt['firstname']}
            return None, decoded_dict
        except Exception as ex:
            return str(ex), ""
