
import streamlit as st
import streamlit.components.v1 as components
st.markdown(
    """
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
        }

        .navbar {
            overflow: hidden;
            background-color: lightblue;
            width: 100%;
            margin: 0;
        }

        .navbar a {
            display: inline;
            color: white;
            text-align: center;
            padding: 14px 16px;
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
    """,
    unsafe_allow_html=True,
)

# Your Streamlit app content
st.markdown("<div class='navbar'>Navbar content here</div>", unsafe_allow_html=True)

st.write("Hello! Welcome to Murder Mystery Detectives! ")
