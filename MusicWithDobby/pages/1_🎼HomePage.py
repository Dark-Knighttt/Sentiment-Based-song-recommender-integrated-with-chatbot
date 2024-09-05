import streamlit as st

st.set_page_config(
    page_icon="🎧",
    page_title="MusicChatMate",
    layout="wide",
    # initial_sidebar_state="expanded",
)

st.title("MusicChatMate")

col1,col2 = st.columns(2)
with col2:
    # image = 'boticon.png'
    # container = st.container()
    # container.layout.width = '400%'
    # container.layout.height = '400%'
    # container.image(image, caption="", width=500)
    st.image('Donts_gif_File.gif')
with col1:
    # fn = f'\n\n'
    # st.write(fn)
    # st.write(fn)
    # fr = f'Hey!!! \n I\'m Dobby.I am sure I\'ll predict your moods and suggest you some amazing songs. Wanna give it a try???\n Come on. Let\'s chat......'
    # st.write(fr)

    # ft = f'Here we could communicate with chatbot and from the conversation We would get the emotion of the person.'
    # st.write(ft)

    # fk = f'Here, we are using a retrieval based chatbot using nltk, python, sentiment analyzer, etc....'
    # st.write(fk)

    # fb = f'Music with DOBBY  -  is a web app where user will converse with DOBBY #TheBOT and on the basis of the chats the emotion of the user will be judged by nltk sentiment analyzer and songs will be recommended using Spotify-api on the basis on emotion predict.'
    # st.write(fb)
    st.markdown(f"""
    <div style="text-align: center; padding-top: 10px;">
    <h3>🌟 Welcome to our realm of digital enchantment, where conversations and melodies collide in a symphony of innovation! 🤖🎵

    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""<div style="justify-content: center;"><i>Step into a world where our chatty AI companion doubles as a maestro, guiding your musical journey based on the sentiments expressed in your conversations. Engage in delightful banter with our witty chatbot, sharing tales, thoughts, or even pondering life's mysteries - all while unknowingly influencing your tailor-made music recommendations!

This isn't your average chit-chat; it's a gateway to discovering tunes that perfectly match the emotional essence of your discussions. Witness the magic as your words shape playlists and song suggestions, ensuring every beat resonates with your mood and sentiments.

Explore this whimsical fusion of conversation and melody, where our chatbot sparkles with personality and the music recommendation system orchestrates a symphony inspired by your unique interactions. Dive in, converse, and let the melodies spun from your chats be the soundtrack to your digital escapades! 🎶🤖✨
</i></div>""", unsafe_allow_html=True)
    
