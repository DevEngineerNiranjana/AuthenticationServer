import re
from src.common.constants import *


class UserDetails:
    def __init__(self):
        try:
            self.col = client[USER_DATABASE][USER_COLLECTION]
        except Exception as err:
            print("Error String : ", str(err))

    def verify_user(self, user_data):
        try:
            query = {"$or": [{"_id": user_data["username"]},
                             {"email": user_data["username"]}]}
            projection = {"_id": 1, "password": 1}
            record_list = self.col.find(query, projection)

            if record_list.count() > 0:
                for record in record_list:
                    decode_pass = fernet.decrypt(record["password"]).decode()
                    if decode_pass == user_data["password"]:
                        return None, record["_id"]
                    else:
                        return "Incorrect Password", {}
            else:
                error = "Invalid Username or Email"
                return str(error), {}
        except Exception as error:
            return str(error), {}

    def register_user(self, input_json):
        try:
            username = str(input_json["username"])
            email_id = str(input_json["email"])
            if not username:
                return "Username required"
            if not email_id:
                return "Email ID required"

            query = {"$or": [{"_id": username},
                             {"email": email_id}]}
            record_list = self.col.find(query)
            if record_list.count() > 0:
                return "User Already Exists"

            password = input_json["password"]
            if not password:
                return "Password required"
            pattern = "^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
            if not re.match(pattern, password):
                return "Password must be Minimum eight characters, at least one letter and one number"

            enc_pass = fernet.encrypt(password.encode())
            insert_dict = {"_id": username,
                           "password": enc_pass,
                           "email": email_id,
                           "first_name": str(input_json["first_name"]),
                           "last_name": str(input_json["last_name"]),
                           "phone": str(input_json["phone"]),
                           "city": str(input_json["city"]),
                           "address": str(input_json["address"])
                           }
            self.col.insert_one(insert_dict)
            return None
        except Exception as error:
            return str(error), {}
