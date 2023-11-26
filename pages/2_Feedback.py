import streamlit as st

from trubrics.integrations.streamlit import FeedbackCollector
collector = FeedbackCollector()
q1 = st.text_input("Q 1")
q2 = st.text_input("Q 2")
q3 = st.text_input("Q 3")
if q1 and q2 and q3:
    button = st.button(label="submit")
    if button:
        feedback = collector.st_feedback(
            "custom",
            user_response={
                "Q 1": q1,
                "Q 2": q2,
                "Q 3": q3,
            },
            path="../feedback.json",
        )
        feedback.dict() if feedback else None
