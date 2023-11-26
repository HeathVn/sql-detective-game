
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

button_style = """
    background-color: transparent; 
    border: 2px solid white;
    border-radius: 15px;
    color: white;
    padding-left: 10px;
    padding-right:10px;
    text-decoration: none;
    font-size: 16px;
"""

st.write('''Welcome! Please enter your name to begin.''')
player_name = st.text_input('Player Name:')


# Define a SessionState class for persisting state across interactions
class SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

# Function to create or get the SessionState object
def get_session_state():
    ctx = get_report_ctx()
    session_state = getattr(ctx, "_session_state", None)
    if session_state is None:
        session_state = ctx._session_state = SessionState()
    return session_state

# Create or get the SessionState object
session_state = get_session_state()

# Global-like variable
if not hasattr(session_state, "global_variable"):
    session_state.clicked = False

# Function to update the global-like variable
def update_global_variable():
    session_state.clicked = True

#click = False


#def clicked():
    #global click
    #click = True

if player_name:
    st.write('''Let's view the crime scene report we have received for this''')

    cursor.execute('''
        SELECT * 
        FROM crime_scene_report
        WHERE type = 'murder' 
        AND city = 'Mellon City' 
    ''')

    rows = cursor.fetchall()

    column_names = [description[0].capitalize() for description in cursor.description]


    if rows and column_names:
        df = pd.DataFrame(data=rows, columns=column_names)
        st.table(df)

        col1,col2 = st.columns([6,1])

        with col1:
            finished = st.button("""Press Button if finished reading""", on_click = update_global_variable)
        with col2 :
            pass 
    else:
        st.warning('No results found.')

    st.write(click)

    if click == True:
 
        user_guess = st.text_input(''' Oh no! It looks like someone meddled with the crime scene reports and some of the key information are missing. Solve this secret code below to find out the missing information!''')

        if user_guess:
            user_guess = user_guess.strip()

            cursor.execute('''
                SELECT * 
                FROM person
                WHERE LOWER(address_street_name) = ?
                ORDER BY name DESC
            ''', (user_guess.lower(),))  # Using a placeholder and passing the variable as a parameter

        
            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            if rows:
                df = pd.DataFrame(data=rows, columns=column_names)
                st.table(df)
            else:
                st.warning('No results found. Try again!')




