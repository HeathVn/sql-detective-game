
import streamlit as st
import streamlit.components.v1 as components

full_width_style = """
<style>
    .navbar {
        background-color: #333;
        width: 100%;
        text-align: center;
    }

    .navbar a:hover {
            background-color: #ddd;
            color: black;
     }
</style>
"""

# Apply the custom CSS
st.markdown(full_width_style, unsafe_allow_html=True)

st.markdown("<div class='navbar'><a href='#home'>Home</a><a href='#page1'>Page 1</a><a href='#page2'>Page 2</a></div>", unsafe_allow_html=True)

st.write("Hello! Welcome to Murder Mystery Detectives! ")
