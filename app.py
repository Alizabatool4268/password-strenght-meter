import streamlit as st 
import re

st.set_page_config(page_title="password_strenght_meter",layout="wide",page_icon="🗂")
st.title("PASSWORD STRENGTH METER")    



try:
    def check_password_strenght(password):
        score = 0
        if len(password) >=8:
            score +=1
        else:
            print("Password must be eight letters")
        if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
            score +=1
        else:
            print("Password must contain one uppercase as well as one lowercase letter  ")    
            
               
except ValueError:
    print("SomeThing went wrong ")
    
    
    
st.text_input("Enter your password")
st.button("check strenght")