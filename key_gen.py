import string
import secrets
from firebase_config import get_db

db = get_db()
users_ref = db.child("users")
users = users_ref.get()

key_ids_list = []

def key_generator(key_range=50):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    while True:
        key = ''.join(secrets.choice(caracteres) for _ in range(key_range))
        print(f"Tentando chave: {key}")  

        if users.val():
            for user_id, user_info in users.val().items():
                key_colum = user_info.get('key')
                key_id = key_colum.get('key_id') if key_colum else None

                print(f"Verificando {user_id} - Key ID: {key_id}") 

                if key_id == key:   
                    print(f"Chave duplicada encontrada! {key_id} == {key}")
                    break
            else:
                print(f"Chave única encontrada: {key}")
                return key
