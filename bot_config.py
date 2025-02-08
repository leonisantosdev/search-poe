import random
import string
import hashlib
import rich as rc
import secrets
from firebase_config import get_db
import os
from datetime import datetime, timedelta
from menu import menu, response_menu
import time
from create_user import create_random_username, create_random_password
from register_user import register_user

db = get_db()

def clean_sys():
    return os.system("cls")

def clean_sys_time(seconds):
    time.sleep(seconds)
    return os.system("cls")

clean_sys()

while True:
    menu()
    response = response_menu()
    clean_sys()

    if response == 1:
        username = create_random_username()
        password = create_random_password()

        try:
            register_user(username=username, password=password)
            rc.print('''
    [green b]User registered successfully![/green b] ✅''')
        except:
            rc.print('''
    [red b]User not found![/red b] ❌''')

    elif response == 2:
        def key_generator(tamanho=50):
            caracteres = string.ascii_letters + string.digits + string.punctuation
            key = ''.join(secrets.choice(caracteres) for _ in range(tamanho))
            return key
        
        def search_user(tabel, username):
            users = db.child(tabel).get()
            
            for user in users.each():
                if user.val()['username'] == username:
                    user_id = user.key()
                    return user_id
                
        clean_sys()
        key = key_generator()
        rc.print(f'''
    [green b]Key generated successfully![/green b] 🔑 ✅
        
    KEY: [white]{key}[/white]
    
    1. Cancelar''')

        username = input('''
    Insira o username para atribuir a KEY: ''')


        if username == '1':
            clean_sys()
            continue
        else:
            clean_sys()
            available_times = {
                "1": timedelta(days=1),
                "7": timedelta(days=7),
                "30": timedelta(days=30)
            }

            rc.print('''
    [1] - Day
    [7] - Days
    [30] - Days
    ''')

            chosen_time = input('''
    How long is the KEY? ''')
        
            time_now = datetime.now()
            expiration = time_now + available_times[chosen_time]


            user_id = search_user('users', username)
            if user_id:
                clean_sys()
                db.child("users").child(user_id).child("key").update({
                    "key_id": key,
                    "valid": True,
                    "created_at": time_now.strftime("%Y-%m-%d %H:%M:%S"),
                    "expires_at": expiration.strftime("%Y-%m-%d %H:%M:%S")
                })

                rc.print('''
    Key assigned successfully! 🔑 ✅''')
            else:
                rc.print('''
    User not found! ❌''')
            
    elif response == 3:
        break
