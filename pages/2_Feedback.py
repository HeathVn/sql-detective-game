import streamlit as st
from streamlit_star_rating import st_star_rating
import sqlite3

connection = sqlite3.connect('Modified SQL Database.db')
cursor = connection.cursor()



with st.form("user_feedback"):
    header = st.columns([0.8,1,0.5])
    header[1].subheader('Feedback Form')

    name = st.text_input('''Please enter your name:''')
    stars = st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 3, key = "rating", dark_theme = True , size=20)

    suggestion = st.text_area(label="Game Suggestions", value="", height=None, max_chars=None)

    submit = st.form_submit_button('Submit')

if submit:
    cursor.execute('''
        INSERT INTO Players(Player Name, Date Played, Start Time, End Time, Rating, Any feedback/suugestions)
        VALUES (?,'','','',?,?) 
    ''', (name, stars,suggestion))
                                         