import rich as rc    

def menu():
  return rc.print('''
    [b]CREATE USERS DATABASE[b]
    
    1. Register User
    2. Register Key
    3. Exit''')


def response_menu():
    response = input('''
    Response: ''')
    response = int(response)
    return response