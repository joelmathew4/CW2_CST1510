from tokenize import Name

import streamlit as st 
import pandas as pd


st.title("Welcome to my world!")
st.write("This is home page of steramlit app. Here you can find some information about the app and its features.")

st.subheader("Features")

st.markdown("- **feature 1:** Description of feature 1.")
st.caption("This is a caption for feature 1.")
st.text('''this is some additional information about feature 1.''')


df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35],    
})

st.write(df)

age = st.number_input("Enter your age", min_value=0, max_value=100)
st.write(f"Hello, {Name}! Welcome to our Streamlit app. You are {age} years old.")


st.write('Choose a value between 0 and 100:')
slid_ = st.slider('Select a value', 0, 100, 50)
st.write(f'You picked: {slid_}')


selected_option = st.selectbox('Select an option', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {selected_option}')

st.checkbox('I agree to the terms and conditions')
st.checkbox('I disagree to the terms and conditions')

st.multiselect('Select your favorite colors', ['Red', 'Green', 'Blue', 'Yellow'])


name = st.text_input('Enter your name')

if st.button('Submit'):
    st.write(f'Hello, {name}! Welcome to our Streamlit app.')

    if name:
        st.write(f'Hello, {name}! Welcome to our Streamlit app.')
    else:
        st.warning('Please enter your name to proceed.')
