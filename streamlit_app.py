import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import subprocess


packages = ["matplotlib"]
install_command = ["pip", "install"] + packages
subprocess.call(install_command)

import matplotlib as mt


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

# Function to update the text position in the animation
def update(frame):
    x, y = text.get_position()
    text.set_position((x + 0.1, y))
    return text,

# Create a figure and axis
fig, ax = plt.subplots()

# Set initial text position
x0, y0 = 0, 0
text = ax.text(x0, y0, 'Hello! welcome to Murder Mystery Detectives!', fontsize=12)

# Set the axis limits
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 1)

# Create the animation
ani = animation.FuncAnimation(fig, update, frames=range(100), interval=50, blit=True)

# Show the animation
plt.show()
