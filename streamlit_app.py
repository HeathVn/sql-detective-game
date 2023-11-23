
import streamlit as st
import streamlit.components.v1 as components


custom_html = """
<div style="margin:0;width: 100vw; height: 300px; background-color: lightblue;">
    This is a custom HTML component with full screen width.
</div>
"""

# Display the HTML using components.html
st.components.v1.html(custom_html, height=350)

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
            margin:0;
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
    </style>
</head>
<body>

    <div class="navbar">
        <a href="#home">Home</a>
        <a href="#page1">Page 1</a>
        <a href="#page2">Page 2</a>
    </div>
</body>

"""
)

st.write("Hello! Welcome to Murder Mystery Detectives! ")
