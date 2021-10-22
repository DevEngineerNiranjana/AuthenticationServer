from pymongo import MongoClient
from cryptography.fernet import Fernet

client = MongoClient('localhost', 27017)

# key = Fernet.generate_key()
key = b'kmR7JeiewgL3sBFaqg_wKv17CJ3fzIkd5lVT4_EAjrU='
fernet = Fernet(key)

# database and collection
USER_DATABASE = "user_database"
USER_COLLECTION = "user_details"
