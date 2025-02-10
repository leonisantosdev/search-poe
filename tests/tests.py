from firebase_config import get_db

db = get_db()

users_ref = db.child("users")
users = users_ref.get()

key_ids_list = [] 

if users.val():
    for user_id, user_info in users.val().items():
        key = user_info.get('key')  
        key_id = key.get('key_id') if key else None 
        
        if key_id: 
            key_ids_list.append(key_id) 



