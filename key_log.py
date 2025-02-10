from rich.console import Console
from rich.table import Table
from firebase_config import get_db
from rich import print 

def collect_user_data():
    db = get_db()
    users_ref = db.child("users")
    users = users_ref.get()

    user_data = []

    if users.val():
        for user_id, user_info in users.val().items():
            username = user_info.get('username')
            key = user_info.get('key')  
            key_id = key.get('key_id')
            valid = user_info.get('key').get('valid') 
            expires_at = user_info.get('key').get('expires_at') 
            created_at = user_info.get('key').get('created_at')  

            user_data.append({
                'user_id': user_id,
                'username': username,
                'key_id': key_id,
                'valid': valid,
                'expires_at': expires_at,
                'created_at': created_at
            })
    else:
        print("No users found!")

    return user_data

def key_log(user_data):
    console = Console()
    table = Table()

    table.add_column("ID", justify="left", no_wrap=True)
    table.add_column("USERNAME")
    table.add_column("KEY")
    table.add_column("VALIDITY")
    table.add_column("STATUS")

    for user in user_data:
        user_id = user['user_id']
        username = user['username']
        key_id = user['key_id']
        valid = user['valid']
        expires_at = user['expires_at']
        status = "[green b]Active[/green b]" if valid else "[red b]Expired[/red b]"

        table.add_row(user_id, username, key_id, expires_at, status)

    console.print(table)

user_data = collect_user_data()