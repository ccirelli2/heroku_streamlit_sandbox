"""
"""
import os
import sys
import streamlit as st

st.title("My Streamlit App")

# Input
input_message = st.text_input("Message", "World")

# Response
st.title("Response")
st.write(f'Hello {input_message}')
