from datetime import datetime
import rich as rc
from rich.console import Console
from rich.table import Table
from firebase_config import get_db
from rich import print

db = get_db()

def collect_user_data():
    users_ref = db.child("users")
    users = users_ref.get()

    user_data = []

    if users.val():
        for user_id, user_info in users.val().items():
            username = user_info.get("username", "N/A")  
            key = user_info.get("key", {})
            key_id = key.get("key_id", "No Key")
            valid = key.get("valid", False)
            expires_at = key.get("expires_at", "Unknown")
            created_at = key.get("created_at", "Unknown")

            user_data.append({
                "user_id": str(user_id),
                "username": str(username),
                "key_id": str(key_id),
                "valid": valid,
                "expires_at": str(expires_at),
                "created_at": str(created_at),
            })
    else:
        print("[red]No users found![/red]")

    return user_data

def key_log():
    user_data = collect_user_data()

    console = Console()
    table = Table()

    table.add_column("ID", justify="left", no_wrap=True)
    table.add_column("USERNAME")
    table.add_column("KEY")
    table.add_column("EXPIRATION DATE")
    table.add_column("STATUS")

    for user in user_data:
        user_id = user["user_id"]
        username = user["username"]
        key_id = user["key_id"]
        expires_at = user["expires_at"]
        status = ""

        if expires_at == "":
            expires_at = "-------------------"

        if key_id == "":
            status = "[#FFA500 bold]No key registered[/#FFA500 bold]"
            key_id = "--------------------------------------------------"
        else:
            date_now = datetime.now()

            if expires_at == "" or expires_at == "Unknown":
                status = "[yellow bold]No expiration date[/yellow bold]"
            else:
                try:
                    expiration_date = datetime.strptime(expires_at, "%Y-%m-%d %H:%M:%S")

                    if date_now > expiration_date:
                        db.child("users").child(user_id).child("key").update({"valid": False})
                        status = "[red bold]Expired[/red bold]"
                    else:
                        status = "[green bold]Active[/green bold]"
                except ValueError:
                    status = "[red bold]Invalid expiration date[/red bold]"

        table.add_row(user_id, username, key_id, expires_at, status)

    console.print(table)
