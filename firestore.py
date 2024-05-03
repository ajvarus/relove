from utils.env_handler import get_firebase_key_path
import firebase_admin
from firebase_admin import credentials, initialize_app, firestore

cred = credentials.Certificate(get_firebase_key_path())
firebase_app = initialize_app(cred)

db = firestore.client()

def add_product():
    
    data = {
        "brand": "Nike",
        "category": "Men"
    }
    products_ref = db.collection("productsV2")
    data_ref = products_ref.add(data)
    return data_ref
