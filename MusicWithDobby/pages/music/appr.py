import streamlit as st
import pickle
import pandas as pd
import requests
import json

def fetch_poster(music_title):
    # print("iiiii")
    response = requests.get("https://saavn.me/search/songs?query={}&page=1&limit=2".format(music_title))
    # print("mai chala")
    data = response.json()
    # print(data)
    # print("mai bhi")
    nd = data['data']['results'][0]['image'][2]['link']
    # print(type(nd))
    return nd

def recommend(mood):

    md = music[music['m'] == mood].index[0]
    distances = similarity[md]
    music_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]
    recommend_music = []
    recommend_music_poster = []   
    
    for i in music_list:
        music_title = music.iloc[i[0]].name
        recommend_music.append(music['name'].iloc[i[0]])
        recommend_music_poster.append(fetch_poster(music_title))
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
    # print(names)
    # poster1 = poster[0]   #[21][2][2]
    # print(poster1)
    # poster2 = poster['image']
    # posters = poster2
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