import streamlit as st
import os, sys

st.title("Test App!!!")

value = st.slider("Pick a number", 0, 10, 3)

option = st.selectbox('Make a choice', ['A', 'B'])

st.write('test edit')

st.write(option)

print("I want tto show the value of this data", value)
sys.stdout.flush()

st.write(os.getcwd())
