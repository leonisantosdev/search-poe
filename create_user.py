import string
import random

def create_random_username():
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + 'poe'
    return username

def create_random_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return password