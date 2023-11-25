
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
    st.table(data=rows, header=column_names)
else:
    st.warning('No results found.')

    

player_name = st.text_input('Player Name:')

split_data = player_name.split(',')

st.write(split_data[1])

name1 = split_data[0]
name2 = split_data[1]

data = [ name1,name2 ]

st.write(data)

df = pd.DataFrame( data , columns=['Name1'])

st.dataframe(df)
