
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
from PIL import Image

connection = sqlite3.connect('sql-murder-mystery copy.db')
cursor = connection.cursor()

container_style = """
    width:0px;
    height:0px;
    position:relative;
    margin-left:auto;
    margin-right:auto;
"""

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

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("riddle1.json")

col1,col2,col3 = st.columns([2,3,2])

with col1 :
    pass
with col2 :
    st.markdown(f"""<div style="width: 50%; height: 50%;">{st_lottie(lottie_coding,key="lottie1")}</div>""",unsafe_allow_html=True)
with col3 :
    pass  

st.write('''Welcome! Please enter your name to begin.''')
player_name = st.text_input('Player Name:')


if 'click' not in st.session_state:
    st.session_state.click = False

def on_button_click():
    st.session_state.click = True

#click = False


#def clicked():
    #global click
    #click = True




if player_name:
    st.write(f'''Hi {player_name}, let's view the crime scene report we have received for this incident''')

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
            finished = st.button("""Press Button if finished reading""", on_click = on_button_click )
        with col2 :
            pass 
    else:
        st.warning('No results found.')

    #st.write(st.session_state.click)

    if st.session_state.click:
        st.write('''Oh no! It looks like someone meddled with the crime scene reports and some of the key information are missing. Solve this secret code below to find out the missing information!  ''')
        
        image = Image.open('spooky-house.jpeg')

        st.image(image, caption='Crime Scene') 
        
        user_guess = st.text_input('''Enter the secret code that you have found in the image above: ''')

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

            
            user_W1name = st.text_input('''Who is Witness 1? Write the name here:''')
            user_W1name = user_W1name.strip()

            if user_W1name.lower() in ['morty schapiro', 'morty', 'schapiro']:

                cursor.execute('''
                    SELECT * 
                    FROM person
                    WHERE LOWER(address_street_name) = 'northwestern dr' 
                    ORDER BY address_number DESC
                    LIMIT 1
                ''')

                rows = cursor.fetchall()

                column_names = [description[0] for description in cursor.description]

                if rows:
                    df = pd.DataFrame(data=rows, columns=column_names)
                    st.table(df)
                else:
                    st.warning('Oh no! That seems to be incorrect. Please try again! Make sure there are no spelling mistakes, and you are looking for the right clue!')

                image = Image.open('spooky-house.jpeg')

                st.image(image, caption='Crime Scene')

                user_W2name = st.text_input("What letters do you see in the image? Type it here, so we can find the identity of Witness 2!")
                user_W2name = user_W2name.strip()

                if user_W2name.lower() in ['ann', 'nna']:

                    cursor.execute('''
                        SELECT * 
                        FROM person
                        WHERE address_street_name = 'Franklin Ave'
                        AND LOWER(name) LIKE ?
                    ''', ('%' + user_W2name.lower() + '%',))

                    rows = cursor.fetchall()
                    column_names = [description[0] for description in cursor.description]

                    if rows:
                        df = pd.DataFrame(data=rows, columns=column_names)
                        st.table(df)

                    user_W1id = st.text_input("What is the ID number of Witness 1?")
                    user_W1id = user_W1id.strip()

                    user_W2id = st.text_input("What is the ID number of Witness 2?")
                    user_W2id = user_W2id.strip()
                    
                    if user_W1id and user_W2id:
                        cursor.execute('''
                            SELECT *
                            FROM interview
                            WHERE person_id IN (?, ?)
                        ''', (user_W1id, user_W2id))

                        rows = cursor.fetchall()
                        column_names = [description[0] for description in cursor.description]

                        if rows:
                            df = pd.DataFrame(data=rows, columns=column_names)
                            st.table(df)
                        else:
                            st.warning('Oh no, that does not seem correct. Please try again! Are you sure you got the codes right?')
                    else:
                        st.warning('Make sure that the ids for both Witness1 and Witness 2 are entered')

                elif user_W2name.lower() == 'nan':
                    st.warning('No results found. Try again! Maybe you can try switching the order?')
                        
                else:
                    st.warning("Oh no! That seems to be incorrect. Please try again! Make sure there are no spaces between each letter, and you are looking for the right clue!")
            



