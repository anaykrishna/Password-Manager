import streamlit as st
from firebase.secrets import fernet, appcd_generator, Create_new_appcd
from utilities.password_generator import Password_Generator
from services.store import save_pass_to_firebase, load_pass_from_firebase
from services.helper import list_services

appcd = appcd_generator()

def add_password():
    service = st.text_input("Enter the name of the service:")
    username = st.text_input("Enter the username:")
    if 'recent_passwd' in st.session_state and st.session_state['recent_passwd'] != '_':
        ch = st.checkbox("Use Suggested Password")
        if ch:
            password = st.session_state['recent_passwd']
        else:
            password = st.text_input("Enter the password:", type="password")
    else:
        password = st.text_input("Enter the password:", type="password")
    if service and username and password:
        save_pass_to_firebase(service, username, password)
        st.success("Password added successfully")

def view_password():
    services = list_services()
    if not services:
        return
    
    selected_service = st.selectbox("Select a service:", list(services.keys()))
    usernames = services.get(selected_service, [])
    selected_username = st.selectbox("Select Username:", usernames)

    keyword = st.text_input("Enter the app code:", type="password")
    if st.button("Retrieve Password"):
        if keyword != appcd:
            st.error("Wrong Passcode")
            return
        password = load_pass_from_firebase(selected_service, selected_username)
        if password:
            st.info(f"Password: {password}")
        else:
            st.error("Password not found")

def suggest_password():
    st.session_state['recent_passwd'] = Password_Generator()

def main():
    st.title("Password Manager")
    global appcd

    if appcd is None:
        st.warning("Please set up your app passcode.")
        appcd = Create_new_appcd()
        if appcd:
            st.success("App passcode set successfully! Please reload the page.")
            st.stop()
    else:
        menu = ["Add Password", "View Password", "Suggest Password"]
        choice = st.sidebar.selectbox("Menu", menu)

        if choice == "Add Password":
            add_password()
        elif choice == "View Password":
            view_password()
        elif choice == "Suggest Password":
            suggest_password()

if __name__ == "__main__":
    main()
