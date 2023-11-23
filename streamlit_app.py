
import streamlit as st
import streamlit.components.v1 as components

import hydralit as hy

app = hy.HydraApp(title='Simple Multi-Page App')

@app.addapp(is_home=True)
def my_home():
 hy.info('Hello from Home!')

@app.addapp()
def app2():
 hy.info('Hello from app 2')

@app.addapp(title='The Best', icon="🥰")
def app3():
 hy.info('Hello from app 3, A.K.A, The Best 🥰')

#Run the whole lot, we get navbar, state management and app isolation, all with this tiny amount of work.
app.run()

#
components.html(
"""
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .navbar {
            overflow: hidden;
            background-color: lightblue;
            width:100vw;
            height: 80px;
            margin:0;
        }

        .navbar a {
            
            display: inline;
            color: white;
            text-align: center;
            padding: 24px 24px;
            position:relative;
            text-decoration: none;
        }

        .navbar a:hover {
            background-color: #ddd;
            color: black;
        }
        
        .streamlit-container {
            max-width: 100%;
        }
    </style>
</head>
<body>

    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#page1">Page 1</a>
        <a href="#page2">Page 2</a>
    </div>
</body>

""")


st.write("Hello! Welcome to Murder Mystery Detectives! ")
