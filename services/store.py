from firebase.config import db
from utilities.cryptography import encrypt_password, decrypt_password

def save_pass_to_firebase(service, username, password):
    encrypted_password = encrypt_password(password)
    ref = db.reference(f'passwords/{service}')
    ref.update({
        f'passwords/{username}': encrypted_password
    })
    usernames_ref = ref.child('usernames')
    current_usernames = usernames_ref.get() or []
    if username not in current_usernames:
        usernames_ref.set(current_usernames + [username])

def load_pass_from_firebase(service, username):
    ref = db.reference(f'passwords/{service}/passwords/{username}')
    password = ref.get()
    if password:
        return decrypt_password(password)
    return None
