
import streamlit as st
import streamlit.components.v1 as components
import time as time
import hydralit as hy


custom_css = """
<style>
    body {
        background-color: #f0f0f0; /* Light gray background color */
    }

    .my-text {
        color: blue;
        font-size: 18px;
    }

    .navbar {
            overflow: hidden;
            background-color: lightblue;
            width:100vw;
            height: 80px;
            margin:0;
            
    }
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

def typewriter(text: str, speed: int):
    tokens = text.split()
    container = st.empty()
    for index in range(len(tokens) + 1):
        curr_full_text = " ".join(tokens[:index])
        container.markdown(curr_full_text, unsafe_allow_html=True)
        time.sleep(1/speed)



app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp(is_home=True)
def my_home():
    typewriter(text='<h1>Hello! Welcome to Murder Mystery Detectives!</h1>', speed=3)

    hy.info('Hello from Home!')

@app.addapp(title='Start Game',icon="🎮")
def app2():
 hy.info('Hello from app 2')

@app.addapp(title='Developers', icon="</>")
def app3():
 hy.info('Hello from app 3, A.K.A, The Best 🥰')

#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()



#st.write("Hello! Welcome to Murder Mystery Detectives! ")
