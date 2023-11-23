import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt


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

st.pyplot(fig)
