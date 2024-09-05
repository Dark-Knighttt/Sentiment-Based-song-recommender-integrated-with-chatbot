import streamlit as st
from subprocess import call
from pages.chatbot_files import main

st.set_page_config(
    page_icon="🎧",
    page_title="MusicChatMate",
    layout="wide",
    # initial_sidebar_state="expanded",
)

st.title("Let's chit-chat !!")
file = open('chat.txt','a')
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("What is up?")
if prompt:
    # display user message in chat message container
    
    with st.chat_message("user"):
        st.markdown(prompt)
    file.write(prompt + "\n")
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = main.chat_bot(prompt)
        # file.write("assistant : " + full_response + "\n")
        # st.write(full_response)
        # st.markdown(full_response)
        full_response = ""
        full_response += main.chat_bot(prompt)
        message_placeholder.markdown(full_response + " ")
    message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role":"assistant" , "content" : full_response})