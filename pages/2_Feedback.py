import streamlit as st
from streamlit_star_rating import st_star_rating

with st.form("user_feedback"):
    header = st.columns([0.8,1,0.5])
    header[1].subheader('Feedback Form')

    stars = st_star_rating(label = "Please rate you experience", maxValue = 5, defaultValue = 3, key = "rating", dark_theme = True , size=15)



    st.form_submit_button('Submit')
    