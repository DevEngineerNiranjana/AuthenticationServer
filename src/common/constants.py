from pymongo import MongoClient
from cryptography.fernet import Fernet

client = MongoClient('localhost', 27017)

key = Fernet.generate_key()
fernet = Fernet(key)

# database and collection
USER_DATABASE = "user_database"
USER_COLLECTION = "user_details"
