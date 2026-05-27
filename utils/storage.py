from passlib.context import CryptContext
import json
import os
import streamlit as st

USER_FILE = "linguistix_users.json"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_storage_path(username=None):
    """Return the path for user-specific storage or default storage."""
    if username:
        return f"data_user_{username}.json"
    return "linguistix_temp_data.json"

@st.cache_data(show_spinner=False)
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
    st.cache_data.clear()
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

@st.cache_data(show_spinner=False)
def load_users():
    """Load users from a local JSON file and ensure new format."""
    if os.path.exists(USER_FILE):
        try:
            with open(USER_FILE, "r", encoding="utf-8") as f:
                users = json.load(f)
                # Migration: Convert old format {"user": "hash"} to {"user": {"password": "hash", "email": ""}}
                updated = False
                for username, data in users.items():
                    if isinstance(data, str):
                        users[username] = {"password": data, "email": ""}
                        updated = True
                if updated:
                    save_users(users)
                return users
        except Exception as e:
            print(f"User Load Error: {e}")
    return {}

def find_user(identifier, users):
    """Find a user by username or email."""
    # Check username first
    if identifier in users:
        return identifier, users[identifier]
    # Check email
    for username, data in users.items():
        if data.get("email") == identifier:
            return username, data
    return None, None

def save_users(users):
    """Save users to a local JSON file."""
    st.cache_data.clear()
    try:
        with open(USER_FILE, "w", encoding="utf-8") as f:
            json.dump(users, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"User Save Error: {e}")

def get_remembered_user():
    """Check if a user is remembered on this machine."""
    if os.path.exists(".remember_me"):
        try:
            with open(".remember_me", "r") as f:
                return f.read().strip()
        except: pass
    return None

def set_remember_me(username, state=True):
    """Set or clear the remember me flag."""
    if state and username:
        with open(".remember_me", "w") as f:
            f.write(username)
    elif os.path.exists(".remember_me"):
        os.remove(".remember_me")

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)
