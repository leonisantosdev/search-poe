import hashlib
from firebase_config import get_db

db = get_db()

def register_user(username, password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    
    db.child("users").push({
        "username": username,
        "password": hash_password,
        "key": {
            "key_id": "",
            "valid": False,
            "created_at": "",
            "expires_at": "",
            
        }
    })