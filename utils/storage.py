from passlib.context import CryptContext
import json
import os

USER_FILE = "linguistix_users.json"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_storage_path(username=None):
    """Return the path for user-specific storage or default storage."""
    if username:
        return f"data_user_{username}.json"
    return "linguistix_temp_data.json"

def load_data(username=None):
    """Load history, favorites, and phrasebook from a user-specific JSON file."""
    path = get_storage_path(username)
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"Storage Load Error for {username if username else 'guest'}: {e}")
    return {"history": [], "favorites": [], "phrasebook": []}

def save_data(history, favorites, phrasebook=[], username=None):
    """Save history, favorites, and phrasebook to a user-specific JSON file."""
    path = get_storage_path(username)
    try:
        data = {
            "history": history[-50:], # Limit history to last 50
            "favorites": favorites,
            "phrasebook": phrasebook
        }
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Storage Save Error for {username if username else 'guest'}: {e}")

def load_users():
    """Load users from a local JSON file."""
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"User Load Error: {e}")
    return {}

def save_users(users):
    """Save users to a local JSON file."""
    try:
        with open(USER_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"User Save Error: {e}")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)
