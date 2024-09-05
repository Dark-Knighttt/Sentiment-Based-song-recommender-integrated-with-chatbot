import streamlit as st
from PIL import Image
import numpy as np

st.set_page_config(
    page_icon= "🎧",
    page_title="MusicChatMate",
    layout="wide",
    # initial_sidebar_state="expanded",
)


st.markdown(f"""
<div style="text-align: center; padding-top: 10px;">
    <h1><u>MusicChatMate: A Musical Companion</u></h1>
</div>
""", unsafe_allow_html=True)


st.sidebar.title("MusicChatMate")
# st.sidebar.success("Select a page above")

st.set_option('deprecation.showfileUploaderEncoding', False)
# container = st.container()
# container.layout.width = '400%'
# container.layout.height = '250%'
# image = "girl-1990347_1280(1).jpg"

# container.image(image, caption="Your Chat Companion, Your Melodic Guide: Where Conversation Meets Harmony!", width=1200)

image = Image.open('girl-1990347_1280(1).jpg')
# Display the original image
st.image(image, caption='Your Chat Companion, Your Melodic Guide: Where Conversation Meets Harmony!', use_column_width=True)

st.markdown(f"""
<div style="text-align: center; padding-top: 8px;">
    <h2>Chat, Discover, Groove!</h2>
    <h4><i>Dive into conversations with our witty bot and let our music wizardry recommend tunes that match your vibe. Get ready to chat and jam like never before!</i></h3>
</div>
""", unsafe_allow_html=True)
st.write("")