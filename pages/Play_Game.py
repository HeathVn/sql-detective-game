
import streamlit as st
import streamlit.components.v1 as components
import time
import hydralit as hy
import json
import requests
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
from streamlit_card import card
import pandas as pd 
import sqlite3

connection = sqlite3.connect('sql-murder-mystery copy.db')
cursor = connection.cursor()

st.write('''Welcome! Please nter your name to begin.''')
player_name = st.text_input('Player Name:')

st.write('''Let's view the crime scene report we have received for this''')

cursor.execute('''
    SELECT * 
    FROM crime_scene_report
    WHERE type = 'murder' 
    AND city = 'Mellon City' 
''')

rows = cursor.fetchall()

column_names = [description[0] for description in cursor.description]


if rows:
    df = pd.DataFrame(data=rows, columns=column_names.capitalize())
    st.table(df)

else:
    st.warning('No results found.')


user_guess = st.text_input((''' Oh no! It looks like someone meddled with the crime scene reports and some of the key information are missing. Solve this secret code below to find out the missing information!''')

if user_guess:
    user_guess = user_guess.strip()

cursor.execute('''
    SELECT * 
    FROM person
    WHERE LOWER(address_street_name) = ?
    ORDER BY name DESC
''', (user_guess.lower(),))  # Using a placeholder and passing the variable as a parameter

rows = cursor.fetchall()

if rows:
    df = pd.DataFrame(data=rows, columns=column_names)
    st.table(df)
else:
    print ('No results found. Try again!')




