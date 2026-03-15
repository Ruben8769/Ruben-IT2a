import sys
import firebase_admin
from firebase_admin import credentials
from google.cloud import firestore

print("Python:", sys.version)
print("Executable:", sys.executable)

cred = credentials.Certificate("Python/School/Database-Lagerstyring/firebase_nokel.json")
app = firebase_admin.initialize_app(cred)
print("Initialized")

db = firestore.Client.from_service_account_json(
    "Python/School/Database-Lagerstyring/firebase_nokel.json",
    project=app.project_id,
    transport="rest",
)
print("REST client created")

docs = db.collection("lagerstyring-lager").get()
print("Fetched:", len(docs))

for doc in docs:
    print(doc.id, doc.to_dict())