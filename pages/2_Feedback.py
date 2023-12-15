import streamlit as st



with st.form("user_feedback"):
    header = st.columns([0.8,1,0.5])
    header[1].subheader('Feedback Form')

   # stars = st_star_rating(label, amount_of_stars, default_value, size, emoticons, read_only, dark_theme, resetButton=reset_btn, resetLabel=reset_label,
                       #customCSS=css_custom, on_click=function_to_run_on_click if enable_on_click else None)



    st.form_submit_button('Submit')
    