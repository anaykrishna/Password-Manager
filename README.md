# Password Manager (Streamlit + Firebase)

A secure and easy-to-use password manager built with **Streamlit** for the frontend and **Firebase Realtime Database** for cloud-based storage. It also includes AES encryption using **cryptography's Fernet** module to safely store your credentials.

---

## Features

- Generate strong passwords with custom rules
- Store passwords encrypted in your own Firebase DB
- View saved passwords after verifying passcode
- Works entirely on the client side
- Modular, beginner-friendly code

---

## Tech Stack

- [Streamlit](https://streamlit.io/) – UI and frontend
- [Firebase Realtime Database](https://firebase.google.com/products/realtime-database) – Secure cloud storage
- [cryptography.fernet](https://cryptography.io/en/latest/fernet/) – AES encryption
- Python 3.7+

---

## Setup Instructions

### 1. Clone this repository

```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
```

### 2. Setup Firebase

- Create a Firebase project from https://console.firebase.google.com
- Enable Realtime Database (test mode)
- Create a service account and download serviceAccountKey.json and place it inside
```bash 
Firebase SDK/serviceAccountKey.json
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run App

```bash
streamlit run app.py
```

## Security Notes

- Your passwords are AES-encrypted using Fernet before being stored.
- A user-defined App Passcode is required to retrieve saved passwords.
- All Firebase credentials and encryption keys are unique per user.

## To-Do / Future Improvements

- Add user authentication (email/password or Google OAuth)
- Export/Import password vault
- Deploy to Streamlit Cloud with dynamic key input
