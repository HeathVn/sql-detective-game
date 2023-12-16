import streamlit as st
from streamlit_star_rating import st_star_rating
import sqlite3

connection = sqlite3.connect('Modified SQL Database.db')
cursor = connection.cursor()

st.markdown(f'''Hi {st.session_state.player_name}, please fill out thye below feedback form. ''')

with st.form("user_feedback"):
    header = st.columns([0.8,1,0.5])
    header[1].subheader('Feedback Form')

    
    stars = st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 3, key = "rating", dark_theme = True , size=20)

    st.text_area(label="Game Suggestions", value="", height=None, max_chars=None)

    submit = st.form_submit_button('Submit')

#if submit:
    