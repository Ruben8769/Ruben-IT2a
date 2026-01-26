# Importing
import uuid
import firebase_admin
from firebase_admin import credentials, firestore

# Connecting to Firebase
cred = credentials.Certificate("Python/School/Database-Lagerstyring/firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Making seperate variables
imp_users = db.collection("lager-brukere").get()
imp_storage = db.collection("lager-lager").get()

# Creating classes
class User:
    def __init__(self, name, password, userid):
        self.name = name
        self.password = password
        self.id = userid

class Storage_item:
    def __init__(self, name, amount, itemid):
        self.name = name
        self.amount = amount
        self.itemid = itemid

# Creating functions
def user_data(option, in_name, in_password):
    """
    Different options

    Option 1 -> Checking if name, password is maching
        Returns 'True' -> Data is maching
        Returns 'False' -> Data isn't maching
    """
    def maching():
        for user in imp_users:
            user = User(imp_users.to_dict()["name"], imp_users.to_dict()["password"])