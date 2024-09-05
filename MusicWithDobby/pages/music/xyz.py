import streamlit as st
import pickle
import pandas as pd
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

client_credentials_manager = SpotifyClientCredentials(client_id = CLIENT_ID,client_secret = CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

def fetch_poster(music_title,music_artist):
    search_query = f"track : {music_title} artist:{music_artist}"
    results = sp.search(q=search_query, type = "track")
    print(results["tracks"]["items"])
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        print(album_cover_url," ................ ")
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

def recommend(mood):

    md = music[music['m'] == mood].index[0]
    distances = similarity[md]
    music_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]
    recommend_music = []
    recommend_music_poster = []   
    
    for i in music_list:
        music_title = music.iloc[i[0]].name
        music_artist = music.iloc[i[0]].artist

        recommend_music.append(music['name'].iloc[i[0]])
        recommend_music_poster.append(fetch_poster(music_title,music_artist))
        # print('mai chal gya')
    return recommend_music , recommend_music_poster

music_dict = pickle.load(open('pages\music\musicrec.pkl','rb'))
music = pd.DataFrame(music_dict)

similarity = pickle.load(open('pages\music\similarities (1).pkl','rb'))

st.title('Music Recommendation System')

# selected_music_title = st.selectbox('Select a music you like', music['title'].values)
selected_music_mood = 'Happy'
if st.button('Recommend'):
    names,posters = recommend(selected_music_mood)
    
    col1,col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])


# https://api.spotify.com/v1/audio-features/32OlwWuMpZ6b0aN2RZOeMS