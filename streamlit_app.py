
import streamlit as st
import streamlit.components.v1 as components
import time
import hydralit as hy
#from streamlit_lottie import st_lottie

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
    

#lottie_coding = load_lottiefile("lottiefile.json")  # replace link to local lottie file
#lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp(is_home=True)
def my_home():
    typewriter(text='<h1>Hello! Welcome to Murder Mystery Detectives!</h1>', speed=3)

    st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    renderer="svg", # canvas
    height=None,
    width=None,
    key=None,
)
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
