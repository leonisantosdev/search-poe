import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

firebaseConfig = {
    'apiKey': os.getenv("API_KEY"),
    'authDomain': os.getenv("AUTH_DOMAIN"),
    'databaseURL': os.getenv("DATABASE_URL"),
    'projectId': os.getenv("PROJECT_ID"),
    'storageBucket': os.getenv("STORAGE_BUCKET"),
    'messagingSenderId': os.getenv("MESSAGING_SENDER_ID"),
    'appId': os.getenv("APP_ID"),
    'measurementId': os.getenv("MEASUREMENT_ID")
}

missing_keys = [key for key, value in firebaseConfig.items() if value is None]
if missing_keys:
    raise ValueError(f"Erro: As seguintes variáveis de ambiente estão faltando ou são inválidas: {', '.join(missing_keys)}")

try:
    firebase = pyrebase.initialize_app(firebaseConfig)
    db = firebase.database()
    print("Firebase inicializado com sucesso!")
except Exception as e:
    print(f"Erro ao inicializar o Firebase: {e}")
    raise

def get_db():
    return db

if __name__ == "__main__":
    db = get_db()
    print("Conexão com o banco de dados estabelecida.")