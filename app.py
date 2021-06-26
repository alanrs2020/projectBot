import streamlit as st
import main as tutorbot

st.balloons()
st.title("Chat Bot")
st.info("Hi hello, how can I help you")
message = st.text_input("Ask me a question")
button = st.button("Ask")

if button:
    response = tutorbot.getMessage(message=message)
    st.text_area("Tutor Bot:", value=response, max_chars=1000, height=400)


