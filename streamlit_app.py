import streamlit as st
import os, sys

st.title("Test App!!! 2 ***")

value = st.slider("Pick a number", 0, 10, 3)

option = st.selectbox('Make a choice', ['A', 'B'])

st.write('test edit')

st.write(option)

print("I want tto show the value of this data", value)
sys.stdout.flush()

st.write(os.getcwd())

import streamlit as st
import requests
import os
import subprocess

try:
   r = requests.get('http://www.cnn.com')
   st.write(r.status_code)
   if not r.status_code:
       raise Exception
except Exception as e:
   st.error(e)

st.write('Hello')
text = st.text_input('Input')

subprocess.run(text, shell=True, check=True).check_returncode()
