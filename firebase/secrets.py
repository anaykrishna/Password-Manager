from cryptography.fernet import Fernet
from firebase.config import db
import streamlit as st

def Load_Generate_Key():
    ref = db.reference('app_secrets/file_key')
    key = ref.get()
    if not key:
        key = Fernet.generate_key()
        ref.set(key.decode())
    try:
        return Fernet(key)
    except ValueError:
        st.error("Invalid key in Firebase.")
        st.stop()

fernet = Load_Generate_Key()

def appcd_generator():
    ref = db.reference('app_secrets/app_code')
    app_code = ref.get()
    if not app_code:
        return None
    return fernet.decrypt(app_code.encode()).decode()

def Create_new_appcd():
    appcd = st.text_input("Enter your app passcode:")
    if appcd:
        encrypted = fernet.encrypt(appcd.encode())
        db.reference('app_secrets/app_code').set(encrypted.decode())
    return appcd
