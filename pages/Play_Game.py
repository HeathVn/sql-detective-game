
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

def typewriter(text: [str,str], speed: int):
    
    container = st.empty()
    for i in text:
        tokens = i.split()
        
        

        for index in range(len(tokens) + 1):
            curr_full_text = " ".join(tokens[:index])
            container.markdown(curr_full_text, unsafe_allow_html=True)
            time.sleep(1/speed)
    

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


if 'click2' not in st.session_state:
    st.session_state.click = False

def on_button_click2():
    st.session_state.click2 = !True

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
                

                image = Image.open('spooky-house2.png')

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
                    
                    
                    typewriter(text=["<h2 style='text-align:center;'>Witness 2 submitted a photo to the case file</h1>","<h2 style='text-align:center;'>Access the photo by clicking the button below.</h1>","<h2 style='text-align:center;'>Press the button below to start your game</h1>"], speed=2.5)
                    #st.write('Witness 2 submitted a photo to the case file')

                    #add button
                    col1,col2 = st.columns([6,1])

                    with col1:
                        finished = st.button("""View Photo""", on_click = on_button_click2 )
                    with col2 :
                        pass 

                    #add picture
                    if click2:
                        st.image('red testla car.png')

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

                            st.write('Here is a list of suspects and the information collected from them. Based on the witness reports, are you able to guess the murderer?')

                            cursor.execute('''
                                SELECT p.name, dl.*, gym.membership_start_date, gym.membership_status
                                FROM drivers_license dl
                                INNER JOIN person p ON dl.id = p.license_id 
                                INNER JOIN get_fit_now_member as gym
                                ON p.id = gym.person_id 
                                ORDER BY dl.id DESC
                                LIMIT 20 
                            ''')

                            rows = cursor.fetchall()
                            column_names = [description[0] for description in cursor.description]

                            if rows:
                                df = pd.DataFrame(data=rows, columns=column_names)
                                st.table(df)

                            user_murderer = st.text_input('Who are you accusing of murder?')
                            user_murderer = user_murderer.strip()

                            if user_murderer.lower() in ['jeremy', 'jeremy bowers', 'bowers', 'jeremybowers']:

                                cursor.execute('''
                                    SELECT p.name
                                    FROM drivers_license dl
                                    INNER JOIN person p 
                                    ON dl.id = p.license_id 
                                    INNER JOIN get_fit_now_member as gym
                                    ON p.id = gym.person_id
                                    INNER JOIN get_fit_now_check_in as checkin
                                    ON gym.id = checkin.membership_id
                                    WHERE plate_number LIKE '%H42W%' 
                                    AND membership_status = 'gold'
                                    AND check_in_date = '20180109' 
                                ''')

                                rows = cursor.fetchall()
                                
                                column_names = [description[0] for description in cursor.description]

                                if rows:
                                    df = pd.DataFrame(data=rows, columns=column_names)
                                    st.table(df)
                                    st.write(f'Wow, that is amazing. You did it! {user_murderer.capitalize()} is the murderer.')
                                    time.sleep(1)
                                    st.balloons()
                                else:
                                    st.warning(f'Oh no! Your guess does not seem to be right. {user_murderer.capitalize()} is not the murderer. Please try again!') 

                                

                        else:
                            st.warning('Oh no, that does not seem correct. Please try again! Are you sure you got the codes right?')

                    else:
                        st.warning('Make sure that the ids for both Witness 1 and Witness 2 are entered')

                elif user_W2name.lower() == 'nan':
                    st.warning('No results found. Try again! Maybe you can try switching the order?')
                        
                else:
                    st.warning("Oh no! That seems to be incorrect. Please try again! Make sure there are no spaces between each letter, and you are looking for the right clue!")
            
            else:
                st.warning('Oh no! That seems to be incorrect. Please try again! Make sure there are no spelling mistakes, and you are looking for the right clue!')
        
        



