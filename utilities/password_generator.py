import random
import streamlit as st

def Password_Generator():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] 
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<'] 

    FULL_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    pass_len = st.number_input("Enter the length of the password:", min_value=1, step=1)
    upper_len = st.number_input("Enter the minimum number of uppercase alphabets in the password:", min_value=0, step=1)
    lower_len = st.number_input("Enter the minimum number of lowercase alphabets in the password:", min_value=0, step=1)
    num_len = st.number_input("Enter the minimum number of digits in the password:", min_value=0, step=1)
    symbol_len = st.number_input("Enter the minimum number of symbols in the password:", min_value=0, step=1)

    temp_pass = ''

    if (upper_len + lower_len + num_len + symbol_len > pass_len):
        st.error("Invalid password length")
        return None
    else:
        for i in range(upper_len):
            temp_pass += random.choice(UPCASE_CHARACTERS)
        for i in range(lower_len):
            temp_pass += random.choice(LOCASE_CHARACTERS)    
        for i in range(num_len):
            temp_pass += random.choice(DIGITS)
        for i in range(symbol_len):
            temp_pass += random.choice(SYMBOLS)
        for i in range(pass_len - upper_len - lower_len - num_len - symbol_len):
            temp_pass += random.choice(FULL_LIST)    
        password = list(temp_pass)
        random.shuffle(password)
        password = ''.join(password)

        st.info(f"Your Password is: {password}")
    return password
