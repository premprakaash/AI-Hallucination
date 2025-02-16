import streamlit as st

# Title of the app
st.title('Hello, Streamlit!')

# Simple text display
st.write('Welcome to the Streamlit app!')

# Adding a text input widget
name = st.text_input("Enter your name")
st.write(f"Hello, {name}!")

# Button example
if st.button('Click Me'):
    st.write('Button was clicked!')
