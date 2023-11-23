
import streamlit as st
import streamlit.components.v1 as components

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
            background-color: #333;
        }

        .navbar a {
            float: left;
            display: block;
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
    <!-- Add more links as needed -->
</div>
    """
)

st.write("Hello! Welcome to Murder Mystery Detectives! ")
