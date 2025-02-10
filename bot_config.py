import rich as rc
from firebase_config import get_db
import os
from datetime import datetime, timedelta
from menu import menu, response_menu
import time
from create_user import create_random_username, create_random_password
from register_user import register_user, copy_user
from key_gen import key_generator
from key_log import key_log
from time import sleep
from rich.progress import Progress, BarColumn, TextColumn

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

    if response != '1' or '2' or '3' or '4':
        clean_sys()
        rc.print('''
    [red blink]Choose a valid option between 1 and 4![/red blink]''')

    if response == '1':
        clean_sys()
        username = create_random_username()
        password = create_random_password()

        try:
            user_id = register_user(username=username, password=password)

            rc.print('''
    [green b blink]User registered successfully![/green b blink] ✅

    Do you want to copy the data of the created user?
    
    1. [green]Yes[/green]
    2. [red]No[/red]''')
        
            response_copy = input('''
    Response: ''')

            if response_copy == '1':
                clean_sys()
                copy_user(id=user_id, username=username)
                rc.print('''
    [green b blink]User copy.[/green b blink]''')
            if response_copy == '2':
                clean_sys()
                continue
        except:
            rc.print('''
    [red b blink]User not found![/red b blink] ❌''')

    elif response == '2':
        def search_user(tabel, username):
            users = db.child(tabel).get()
            
            for user in users.each():
                if user.val()['username'] == username:
                    user_id = user.key()
                    return user_id
                
        key = key_generator()
        
        clean_sys()
        rc.print(f''' 
    [green b blink]Key generated successfully![/green b blink] 🔑 ✅

    KEY: [white]{key}[/white]

    1. Cancel''')

        username = input('''
    Enter the username to assign the KEY: ''')

        if username == '1':
            clean_sys()
            continue
        elif username != '1':
            
            clean_sys()
            available_times = {
                "1": timedelta(days=1),
                "7": timedelta(days=7),
                "2": timedelta(minutes=2),
                "30": timedelta(days=30)
            }

            rc.print('''
    [1] - Day
    [7] - Days
    [2] - Minutes (Test)
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
                
                rc.print(f'''
    Key assigned successfully for {chosen_time} days! 🔑 ✅''')
            else:
                clean_sys()
                rc.print('''
    [red b blink]User not found![/red b blink] ❌''')
                

    elif response == '3':
        while True:
            clean_sys()
            key_log()
            rc.print(
'''
1. [red b]Back[/red b]
2. Update''')
            
            response_keylog = input('''
Response: ''')
            rc.print('''''')
            
            if response_keylog == '1':
                clean_sys()
                break
            elif response_keylog == '2':
                with Progress(
                    TextColumn('Loading...'),
                    BarColumn(pulse_style="white", finished_style="green", style="white", complete_style="yellow"),
                    TextColumn('[white]{task.percentage:>3.0f}%')
                ) as progress:
                        task = progress.add_task("", total=100)

                        for i in range(100):  
                            progress.update(task, advance=(100 / 100))
                            sleep(0.02)
                clean_sys()
                continue

    elif response == '4':
        clean_sys()
        break
