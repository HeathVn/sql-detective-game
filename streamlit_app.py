
import streamlit as st
import streamlit.components.v1 as components

import hydralit as hy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Create a figure and axis
fig, ax = plt.subplots()

# Set initial text position
x0, y0 = 0, 0
text = ax.text(x0, y0, 'Hello, Python!', fontsize=12)

# Set the axis limits
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 1)

# Create a text element with white color
text = ax.text(0.5, 0.5, 'Animated Text', color='white', ha='center', va='center', fontsize=20)

# Set the initial state of the text
def init():
    text.set_text('')
    return text,

# Update the text in each frame
def update(frame):
    text.set_text('Frame {}'.format(frame))
    return text,

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=10, init_func=init, blit=True, interval=500)

plt.show()



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
