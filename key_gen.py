import string
import secrets

def key_generator(key_range=50):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    key = ''.join(secrets.choice(caracteres) for _ in range(key_range))
    return key