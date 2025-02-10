from firebase_config import get_db
from datetime import datetime
import rich as rc

db = get_db()

def get_expires():
    users_ref = db.child("users")
    users = users_ref.get()

    expires_list = []
    user_ids = []  #
    
    if users.val():
        for user_id, user_info in users.val().items():
            expires_at = user_info.get('key').get('expires_at')
            username = user_info.get('username')
            expires_list.append(expires_at)
            user_ids.append(user_id) 
            
    else:
        print("Users not found!")

    return expires_list, user_ids  

def check_valid(expires_list, user_ids):
    for expires_at, user_id in zip(expires_list, user_ids):
        if expires_at == '':
            rc.print(f'''User: {user_id}
KEY: [red b]No key registered[/red b].
''')
        else:
            date_now = datetime.now()

            if date_now > datetime.strptime(expires_at, "%Y-%m-%d %H:%M:%S"):  
                db.child("users").child(user_id).child("key").update({
                    "valid": False
                })
                rc.print(f'''User: {user_id} 
ID: [red b]Expired[/red b].
''')
            else:
                rc.print(f'''User: {user_id} 
ID: [green b]Active[/green b].
''')

expires_list, user_ids = get_expires()
check_valid(expires_list, user_ids)
