
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



player_name = st.text_input('Player Name:')

split_data = player_name.split(',')

st.write(split_data[0])

data = [ split_data[0], split_data[1] ]

st.write(data)

#df = pd.DataFrame(data, columns=['Name1'])

#st.dataframe(df)
