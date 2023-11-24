
import streamlit as st
import streamlit.components.v1 as components
import time
import hydralit as hy
import json
import requests
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html
from streamlit_card import card

# Replace 'lottie_url' with the actual URL of your Lottie JSON animation
lottie_url = "https://lottie.host/embed/2e9086c6-9faf-451a-9880-af787469a8b1/F9hsq1ytrf.json"

container_style = """
    width:100px;
    height:100px;
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


def typewriter(text: [str,str], speed: int):
    
    container = st.empty()
    for i in text:
        tokens = i.split()
        
        

        for index in range(len(tokens) + 1):
            curr_full_text = " ".join(tokens[:index])
            container.markdown(curr_full_text, unsafe_allow_html=True)
            time.sleep(1/speed)

    


   

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    

lottie_coding = load_lottiefile("detective.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/7867624f-734c-48fd-8407-94a8f54fbb63/cEi3XEcPWT.json")

#centered_lottie_html = f""" <div style='display: flex; justify-content: center; align-items: center; height: 300px;'><lottie-player src='{lottie_url}' background='transparent' speed='1' style='width: 300px; height: 300px;' loop autoplay ></lottie-player></div>"""

# Display the centered Lottie animation using st.markdown
#st.markdown(centered_lottie_html, unsafe_allow_html=True)

st.markdown('# Section 1')

st.markdown(f"""<div style='{container_style}'>{st_lottie(lottie_coding,key="lottie1")}</div>""",unsafe_allow_html=True)
    
#st_lottie(lottie_coding, width=500, height=500)
typewriter(text=["<h2 style='text-align:center;'>Hello! Welcome to Murder Mystery Detectives!</h1>","<h2 style='text-align:center;'>Your journey begins here</h1>","<h2 style='text-align:center;'>Press the button below to start your game</h1>"], speed=2.5)


col1, col2, col3,col4,col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col3 :
    st.markdown(f''' <a target='_self' href='#get-started'><button style='{button_style}'>Start Game</button> </a>''', unsafe_allow_html=True)
with col4 :
    pass
with col5 :
    pass

# Use st.markdown to display the HTML content
#st.markdown(f"""<div style='{button_style}'>{st.button(label="Start Game",key="button1")}</div>""", unsafe_allow_html=True)
 

#st.write("Hello! Welcome to Murder Mystery Detectives! ")


col1, col2, col3 = st.columns([2,2,1])

with col1:
    pass
with col2:
    st.markdown('### Get Started')
with col3 :
    pass

card(
    title="Game Instructions",
    text="This is a test card",
    image="https://github.com/HeathVn/streamlit-example/blob/master/detective-2.png",
    styles={
        "card": {
            "width": "600px",
            "height": "500px",
            "border-radius": "60px",
            "box-shadow": "0 0 10px rgba(0,0,0,0.5)",
            "background-color": "#fff",
        },
        "text": {
            "font-family": "serif",
        }
    },
   
)



