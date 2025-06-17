from firebase.secrets import fernet

def encrypt_password(password):
    return fernet.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password):
    return fernet.decrypt(encrypted_password.encode()).decode()
