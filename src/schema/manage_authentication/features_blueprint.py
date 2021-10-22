import json
import jwt
from flask import Blueprint, request
from src.common.jwt_parser import JWTParser
from src.schema.manage_authentication.functions.manage_user import UserDetails

authentication_blueprint = Blueprint("authentication", __name__)


@authentication_blueprint.route('/generate_token', methods=['GET'])
def token():
    if request.method == 'GET':
        request_data = request.form
        payloads = {
            "username": request_data["username"],
            "password": request_data["password"],
            "firstname": request_data["firstname"]
        }
        secret_key = "CLIENTSECRET"
        token_data = jwt.encode(
            payload=payloads,
            key=secret_key
        )
        return json.dumps({"status": "True", "msg": "success", "data": token_data}), 200
    else:
        return json.dumps({"status": "False", "msg": "Invalid request", "data": ""}), 404


@authentication_blueprint.route('/login', methods=['GET'])
def user_login():
    if request.method == 'GET':
        access_token = str(request.headers['Authorization']).replace('Bearer ', '')
        jwt_parser = JWTParser(jwt_token=access_token)
        err, decoded_dict = jwt_parser.decode_access_token()
        if err:
            return json.dumps({"status": "False", "msg": err}), 404

        user_obj = UserDetails()
        err, user_name = user_obj.verify_user(decoded_dict)
        if err:
            return json.dumps({"status": "False", "msg": err}), 404

        msg = "Hi, {0} welcome".format(user_name)
        return json.dumps({"status": "True", "msg": msg}), 200
    else:
        return json.dumps({"status": "False", "msg": "Invalid request"}), 404


@authentication_blueprint.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        json_data = request.json
        user_obj = UserDetails()
        err = user_obj.register_user(json_data)
        if err:
            return json.dumps({"status": "False", "msg": err}), 404
        return json.dumps({"status": "True", "msg": "User registered successfully"}), 200
    else:
        return json.dumps({"status": "False", "msg": "Invalid request"}), 404

