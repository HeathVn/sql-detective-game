
import streamlit as st
import streamlit.components.v1 as components
import time
import hydralit as hy
import json
import requests
from streamlit_lottie import st_lottie
from streamlit.components.v1 import html

# Replace 'lottie_url' with the actual URL of your Lottie JSON animation
lottie_url = "https://lottie.host/embed/2e9086c6-9faf-451a-9880-af787469a8b1/F9hsq1ytrf.json"




def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
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
    

lottie_coding = load_lottiefile("/detective.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://lottie.host/7867624f-734c-48fd-8407-94a8f54fbb63/cEi3XEcPWT.json")

st_lottie(lottie_coding)

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp(is_home=True)
def my_home():
    typewriter(text='<h1>Hello! Welcome to Murder Mystery Detectives!</h1>', speed=3)

    hy.info('')

@app.addapp(title='Start Game',icon="🎮")
def app2():
 hy.info('Hello from app 2')

@app.addapp(title='Developers', icon="</>")
def app3():
 hy.info('Hello from app 3, A.K.A, The Best 🥰')

#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()



#st.write("Hello! Welcome to Murder Mystery Detectives! ")
