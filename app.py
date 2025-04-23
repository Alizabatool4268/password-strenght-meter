import streamlit as st 
import re

st.set_page_config(page_title="password_strenght_meter",layout="wide",page_icon="🗂")
st.title("PASSWORD STRENGTH METER📝")
st.sidebar.title("REMINDER")
st.sidebar.write("""A strong password should:\n
✅ Be at least 8 characters long\n
✅ Contain uppercase & lowercase letters\n
✅ Include at least one digit (0-9)\n
✅ Have one special character (@#$%^&*<>|!?/)""")


#function to check strenght
def check_password_strength(password):
    
    #weak password check. if the password typed in the input feild matches in the list the function will break.
    weak_passwords=["Password123","password123","123456789","123456","987654321","America123",
    "pakistan123","canada","Dubai123","000000","111111","admin123","user123","iloveyou","qwerty"]
    if password_input in weak_passwords:
        st.warning("your password is way too common. It can be hacked easily try another one. ")
        return 0
    
    score = 0
    if len(password) >=8:
        score +=1
    else:
        st.write("✏️ Password must be eight letters")
    if re.search(r"[A-Z]",password) and re.search(r"[a-z]",password):
        score +=1
    else:
        st.write("✏️ Password must contain one uppercase as well as one lowercase letter")
    if re.search(r"\d",password):
        score += 1
    else:
        st.write("✏️password must contain at least one digit")
    if re.search(r"[@#$%^&*<>|!?/]",password):
        score += 1
    else:
        st.write("✏️password must contain at least one special character" )
    return score


password_input=st.text_input("Enter your password",type="password")
if st.button("check strength"):
#running the functio and checking the password strenght on the basis of score
    result = check_password_strength(password_input)
    if result == 4:
        st.success("Your password is very strong✨")
    elif result == 3:
        st.warning("Your password is moderate. It could be better")    
    else:
        st.error("Your password is weak.")    
    st.write(f"Password score: {result}/4")