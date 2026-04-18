import streamlit as st
import pandas as pd

from app_model.db import get_connection
from app_model.cyber_incidents import get_all_cyber_incidents
from app_model.users import add_user, get_user

st.set_page_config(
    page_title="Home",
    page_icon="🏠",
    layout="wide",
)

st.title("Welcome to the Cyber Incidents Dashboard")

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


if not st.session_state["logged_in"]:
    st.warning("Please log in to access the dashboard!")

    if st.button("Go to Login Page"):
        st.switch_page("Home1")
        st.stop()

    st.stop()

else:
    st.success("You are logged in!")


conn = get_connection()
data = get_all_cyber_incidents(conn)

data["timestamp"] = pd.to_datetime(data["timestamp"])

with st.sidebar:
    st.header("Navigation")

    severity_ = st.selectbox(
        "Severity Level",
        data["severity"].unique()
    )

filtered_data = data[data["severity"] == severity_]

col1, col2 = st.columns(2)

with col1:
    st.subheader(f"Cyber Incidents: {severity_}")
    st.bar_chart(filtered_data["category"].value_counts())

with col2:
    st.subheader("Category Trend Over Time")
    st.line_chart(filtered_data, x="timestamp", y="category")

st.subheader("Filtered Data")
st.dataframe(filtered_data)
