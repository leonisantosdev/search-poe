import os
from dotenv import load_dotenv

load_dotenv()

print('apiKey: ', os.getenv("API_KEY")),
print('authDomain: ', os.getenv("AUTH_DOMAIN")),
print('databaseURL: ', os.getenv("DATABASE_URL")),
print('projectId: ', os.getenv("PROJECT_ID")),
print('storageBucket: ', os.getenv("STORAGE_BUCKET")),
print('messagingSenderId: ', os.getenv("MESSAGING_SENDER_ID")),
print('appId: ', os.getenv("APP_ID")),
print('measurementId: ', os.getenv("MEASUREMENT_ID"))