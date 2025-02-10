import hashlib
from firebase_config import get_db
import json
import os

db = get_db()

def register_user(username, password):
    hash_password = hashlib.sha256(password.encode()).hexdigest()
    
    new_user_ref = db.child("users").push({
        "username": username,
        "password": hash_password,
        "key": {
            "key_id": "",
            "created_at": "",
            "expires_at": "",
            "valid": False,
        }
    })

    user_id = new_user_ref['name']
    return user_id

def copy_user(id, username):
    folder_path = '../json/'
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, 'last_user.json')

    last_user_created = {
        "id": id,
        "username": username,
    }

    with open(file_path, 'w') as json_file:
        json.dump(last_user_created, json_file, indent=4)