# import pickle
# import streamlit as st
# import spotipy
# from spotipy.oauth2 import SpotifyOAuth
# from spotipy.oauth2 import SpotifyClientCredentials
# from pages.sentiment_analysis import data_cleaning
# import random
# import webbrowser

# st.set_page_config(
#     page_icon="🎧",
#     page_title="MusicChatMate",
#     layout="wide",
#     # initial_sidebar_state="expanded",
# )

# CLIENT_ID = "786b703a4f3c4f7da2582611b7c9b471"
# CLIENT_SECRET = "e60fe38eeebf42b7a37632e8fb117851"

# # Initialize the Spotify client
# client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
# # sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
#                                                client_secret=CLIENT_SECRET,
#                                                redirect_uri="http://localhost:8502/callback"))

# def get_song_album_cover_url(song_name, artist_name):
#     search_query = f"track:{song_name} artist:{artist_name}"
#     results = sp.search(q=search_query, type="track")

#     if results and results["tracks"]["items"]:
#         track = results["tracks"]["items"][0]
#         album_cover_url = track["album"]["images"][0]["url"]
#         # print(album_cover_url)
#         return album_cover_url
#     else:
#         return "https://i.postimg.cc/0QNxYz4V/social.png"

# def get_song_album_url(song_name, artist_name):
#     search_query = f"track:{song_name} artist:{artist_name}"
#     results = sp.search(q=search_query, type="track")
#     # print(results)

#     if results and results["tracks"]["items"]:
#         track = results["tracks"]["items"][0]
#         album_url = track['external_urls']['spotify']
#         # print(album_url)
#         return album_url
    
# def recommend(mood):
#     index = music[music['m'] == mood].index[0]
#     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
#     recommended_music_names = []
#     recommended_music_posters = []
#     recommended_music_url = []
#     recommended_music_names1 = []
#     recommended_music_posters1 = []
#     recommended_music_url1 = []
#     distances1 = random.choices(distances,k=50)
#     for i in distances1[1:50]:
#         # fetch the movie poster
#         artist = music['artist'].iloc[i[0]]
#         # print(artist)
#         # print(music.iloc[i[0]].name)
#         recommended_music_url.append(get_song_album_url(music['name'].iloc[i[0]], artist))
#         recommended_music_posters.append(get_song_album_cover_url(music['name'].iloc[i[0]], artist))
#         recommended_music_names.append(music['name'].iloc[i[0]])
#         # print(recommended_music_url[0])
#     for i in range(1,40):
        
#         if((recommended_music_names[i]!=None)&(recommended_music_posters[i]!=None)&(recommended_music_url[i]!=None)):
#             recommended_music_url1.append(recommended_music_url[i])
#             recommended_music_names1.append(recommended_music_names[i])
#             recommended_music_posters1.append(recommended_music_posters[i])
#     return recommended_music_names1,recommended_music_posters1,recommended_music_url1


# st.header('Music & me')
# music = pickle.load(open('pages\music\musicrec.pkl','rb'))
# similarity = pickle.load(open('pages\music\similarities (1).pkl','rb'))

# music_list = music['name'].values
# selected_mood = data_cleaning.use()
# print(selected_mood)

# if st.button('Show Recommendation'):
#     recommended_music_names,recommended_music_posters,recommended_music_urls = recommend(selected_mood)
#     col1, col2, col3, col4, col5= st.columns(5)

#     with col1:
#         st.text(recommended_music_names[0])
#         st.image(recommended_music_posters[0])
        
#     with col2:
#         st.text(recommended_music_names[1])
#         st.image(recommended_music_posters[1])

#     with col3:
#         st.text(recommended_music_names[2])
#         st.image(recommended_music_posters[2])
#     with col4:
#         st.text(recommended_music_names[3])
#         st.image(recommended_music_posters[3])
#     with col5:
#         st.text(recommended_music_names[4])
#         st.image(recommended_music_posters[4])

# def container():
#     coll1,coll2,coll3,coll4,coll5 = st.columns(5)
#     colll1 = st.columns(1)
#     recommended_music_names,recommended_music_posters,recommended_music_url = recommend(selected_mood)
#     # print(recommended_music_url[0])
#     # print(type(recommended_music_url[0]))
#     with coll1:
#         if st.button("Play"):
#             url = recommended_music_url[0]
#             print(url)
#             webbrowser.open(url)
            
#     with coll2:
#         if st.button(key=2,label="Play"):
#             url = recommended_music_url[1]
#             webbrowser.open(url)
#     with coll3:
#         if st.button(key=3,label="Play"):
#             url = recommended_music_url[2]
#             webbrowser.open(url)
#     with coll4:
#         if st.button(key=4,label="Play"):
#             url = recommended_music_url[3]
#             webbrowser.open(url)
#     with coll5:
#         if st.button(key=5,label="Play"):
#             url = recommended_music_url[4]
#             webbrowser.open(url)

# container()
# ------------------------------------------------------------------------------------------------------------------------------------------


import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from pages.sentiment_analysis import data_cleaning
import random
import webbrowser

st.set_page_config(
    page_icon="🎧",
    page_title="MusicChatMate",
    layout="wide",
)

# Spotify API credentials
CLIENT_ID = "786b703a4f3c4f7da2582611b7c9b471"
CLIENT_SECRET = "e60fe38eeebf42b7a37632e8fb117851"
REDIRECT_URI = "http://localhost:8502/callback"  # Ensure this is the correct redirect URI

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope="user-library-read"))

def get_song_details(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        return {
            "name": song_name,
            "artist": artist_name,
            "album_cover_url": track["album"]["images"][0]["url"],
            "track_url": track['external_urls']['spotify']
        }
    else:
        return {
            "name": song_name,
            "artist": artist_name,
            "album_cover_url": "https://i.postimg.cc/0QNxYz4V/social.png",
            "track_url": None
        }

def recommend(mood):
    index = music[music['m'] == mood].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music = []

    distances1 = random.choices(distances, k=50)
    for i in distances1[1:50]:
        artist = music['artist'].iloc[i[0]]
        song_name = music['name'].iloc[i[0]]
        details = get_song_details(song_name, artist)
        if details["track_url"]:
            recommended_music.append(details)

    return recommended_music[:5]  # Return top 5 recommendations

st.header('Music & me')
music = pickle.load(open('pages/music/musicrec.pkl', 'rb'))
similarity = pickle.load(open('pages/music/similarities (1).pkl', 'rb'))

selected_mood = data_cleaning.use()
print(selected_mood)

if st.button('Show Recommendation'):
    recommended_music = recommend(selected_mood)
    cols = st.columns(5)

    for i, col in enumerate(cols):
        if i < len(recommended_music):
            song = recommended_music[i]
            with col:
                st.text(song["name"])
                st.image(song["album_cover_url"])
                # if st.button("Play", key=f"play{i}"):
                #     webbrowser.open(song["track_url"])

def container():
    cols = st.columns(5)
    recommended_music = recommend(selected_mood)

    for i, col in enumerate(cols):
        if i < len(recommended_music):
            song = recommended_music[i]
            with col:
                button_key = f"play_{i}"
                if st.button(f"Play", key=button_key):
                    webbrowser.open(song["track_url"])

container()

