import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import webbrowser
# from streamlit.components.v1 import Button

CLIENT_ID = "70a9fb89662f4dac8d07321b259eaad7"
CLIENT_SECRET = "4d6710460d764fbbb8d8753dc094d131"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def redirect_to_url(url):
    return f'<script>window.location.href="{url}";</script>'


def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    # print(results)

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        # if((track["album"]["images"][0]["url"] != None) & (track['external_urls']['spotify'] != None)):
        album_cover_url = track["album"]["images"][0]["url"]
        album_url = track['external_urls']['spotify']
        # print(album_cover_url)
        
        return album_cover_url,album_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"
    
def get_song_album_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    # print(results)

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_url = track['external_urls']['spotify']
        # print(album_url)
        return album_url
    # else:
        # return "https://i.postimg.cc/0QNxYz4V/social.png"


def recommend(mood):
    index = music[music['m'] == mood].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    recommended_music_url = []
    recommended_music_names1 = []
    recommended_music_posters1 = []
    recommended_music_url1 = []
    distances1 = random.choices(distances,k=50)
    for i in distances1[1:50]:
        # fetch the movie poster
        artist = music['artist'].iloc[i[0]]
        # print(artist)
        # print(music.iloc[i[0]].name)
        result = get_song_album_cover_url(music['name'].iloc[i[0]], artist)

# Check the number of returned values and handle accordingly
        if len(result) >= 2:
            poster, url = result[:2]
        recommended_music_url.append(url)
        recommended_music_posters.append(poster)
        recommended_music_names.append(music['name'].iloc[i[0]])
        # print(recommended_music_url[0])
    for i in range(1,40):
        
        if((recommended_music_names[i]!=None)&(recommended_music_posters[i]!=None)&(recommended_music_url[i]!=None)):
            recommended_music_url1.append(recommended_music_url[i])
            recommended_music_names1.append(recommended_music_names[i])
            recommended_music_posters1.append(recommended_music_posters[i])
    return recommended_music_names1,recommended_music_posters1,recommended_music_url1


   
st.header('Music Recommender System')
music = pickle.load(open('pages\music\musicrec.pkl','rb'))
similarity = pickle.load(open('pages\music\similarities (1).pkl','rb'))

music_list = music['name'].values
selected_mood = 'Calm'


if st.button('Show Recommendation'):
    col1, col2, col3, col4, col5= st.columns(5)

    recommended_music_names,recommended_music_posters,recommended_music_url = recommend(selected_mood)
    
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0])
        url = recommended_music_url[0]
        # print(url)
        # print(type(url))
        # webbrowser.open(url)
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1])
                
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2])
        
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3])
        
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4])
        
def container():
    coll1,coll2,coll3,coll4,coll5 = st.columns(5)
    colll1 = st.columns(1)
    recommended_music_names,recommended_music_posters,recommended_music_url = recommend(selected_mood)
    # print(recommended_music_url[0])
    # print(type(recommended_music_url[0]))
    with coll1:
        if st.button("Play"):
            url = recommended_music_url[0]
            print(url)
            webbrowser.open(url)
            
    with coll2:
        if st.button(key=2,label="Play"):
            url = recommended_music_url[1]
            webbrowser.open(url)
    with coll3:
        if st.button(key=3,label="Play"):
            url = recommended_music_url[2]
            webbrowser.open(url)
    with coll4:
        if st.button(key=4,label="Play"):
            url = recommended_music_url[3]
            webbrowser.open(url)
    with coll5:
        if st.button(key=5,label="Play"):
            url = recommended_music_url[4]
            webbrowser.open(url)

container()