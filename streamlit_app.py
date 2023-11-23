
import streamlit as st
import streamlit.components.v1 as components

full_width_style = """
<style>
    .navbar {
        background-color: #FFFFFF;
        width: 100%;
        text-align: center;
        box-sizing: border-box;
    }

    .navbar a:hover {
            background-color: #ddd;
            float: left;
            display: block;
            color: white;
            text-align: center;
            padding: 14px 16px;
            text-decoration: none;
     }
</style>
"""

# Apply the custom CSS
st.markdown(full_width_style, unsafe_allow_html=True)

st.markdown("<div class='navbar'><a href='#home'>Home</a><a href='#page1'>Page 1</a><a href='#page2'>Page 2</a></div>", unsafe_allow_html=True)

st.write("Hello! Welcome to Murder Mystery Detectives! ")
