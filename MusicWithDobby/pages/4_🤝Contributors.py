import streamlit as st

st.set_page_config(
    page_icon="🎧",
    page_title="MusicChatMate",
    layout="wide",
    # initial_sidebar_state="expanded",
)


st.title("Contributors")

col1,col2 = st.columns(2)

with col1:
    image = 'WhatsApp Image 2023-10-31 at 03.52.54.jpeg'
    container = st.container()
    container.layout.width = '400%'
    container.layout.height = '400%'
    container.image(image, caption="", width=400)

with col2:
    image = 'WhatsApp Image 2023-10-31 at 04.00.19.jpeg'
    container = st.container()
    container.layout.width = '400%'
    container.layout.height = '400%'
    container.image(image, caption="", width=350)