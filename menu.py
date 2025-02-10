import rich as rc

def menu():
  return rc.print('''
    [b]BOT CONFIG DATABASE 🤖[b]
    
    1. Register User
    2. Register Key
    3. Key Logs
    4. [red]Exit[red]''')

def response_menu():
    response = input('''
    Response: ''')
    response = int(response)
    return response