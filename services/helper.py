from firebase.config import db
import streamlit as st

def list_services():
    ref = db.reference('passwords')
    data = ref.get()

    if not data:
        st.warning("No services found.")
        return None

    services = {}
    for service, details in data.items():
        usernames = details.get('usernames', [])
        services[service] = usernames
    return services