from pages.hashing import generate_hash, is_valid_hash
from app_model.db import get_connection
from app_model.users import add_user, get_user

conn = get_connection()

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
)

st.title("Welcome to the Main Page🏠")

if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

tab_login, tab_register = st.tabs(["Login", "Register"])


with tab_login:
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Log In"):
        id, user_name, user_hash = get_user(conn, login_username)

        if login_username == user_name and is_valid_hash(login_password, user_hash):
            st.session_state['logged_in'] = True
            st.success("Logged in successfully!")
            st.change_page("pages/1_Dashboard.py")
        else:
            st.error("Invalid username or password")


with tab_register:
    register_username = st.text_input("New Username")
    register_password = st.text_input("New Password", type="password")

    if st.button("Register"):
        hash_password = generate_hash(register_password)
        add_user(conn, register_username, hash_password)
        st.success("Registration successful! Please log in.")