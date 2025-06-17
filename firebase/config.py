import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:
    cred = credentials.Certificate('Firebase SDK/serviceAccountKey.json')
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://password-manager-16b5f-default-rtdb.firebaseio.com/'
    })
