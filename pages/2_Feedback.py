import streamlit as st
from streamlit_star_rating import st_star_rating
import sqlite3

connection = sqlite3.connect('Modified SQL Database.db')
cursor = connection.cursor()


header = st.columns([0.8,1.5,0.5])
header[1].title('Feedback Form')

with st.form("user_feedback"):
    

    name = st.text_input('''Please enter your name:''')
    stars = st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 3, key = "rating", dark_theme = True , size=20)

    suggestion = st.text_area(label="Game Suggestions", value="", height=None, max_chars=None)

    submit = st.form_submit_button('Submit')

    if submit:
        cursor.execute('''INSERT INTO Players VALUES (?,'','','',?,?)''', (name, stars,suggestion))
        connection.commit()
        connection.close()
        st.toast('Your feedback was successfully submitted!')
                                         