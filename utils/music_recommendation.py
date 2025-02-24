import streamlit as st  # Streamlit for web UI
import pandas as pd  # Pandas for handling data
import numpy as np  # NumPy for numerical operations
import pickle  # Pickle for loading pre-trained models
import requests  # Requests for API calls

def fetch_poster(music_title):
    """
    Fetch the poster URL of a music track using an API.
    If no image is found, a placeholder image is used.
    """
    url = f"https://saavn.dev/api/search/songs?query={music_title}"
    response = requests.get(url)
    
    try:
        data = response.json()
        
        if "data" in data and "results" in data["data"] and len(data["data"]["results"]) > 0:
            song_data = data["data"]["results"][0]  # Taking the first result
            if "image" in song_data and len(song_data["image"]) >= 3:
                return song_data["image"][2]["url"]  # Fetch high-quality image (500x500)
    except Exception:
        pass
    
    return "https://via.placeholder.com/500"

def get_top_albums():
    """Fetch top 4 albums/movies with their top 4 songs."""
    top_albums = music['Album/Movie'].value_counts().nlargest(4).index.tolist()
    album_music = {
        album: music[music['Album/Movie'] == album].head(4)[['Song-Name', 'Album/Movie']].to_dict('records')
        for album in top_albums
    }
    return album_music

# Load the pre-trained recommendation model and similarity matrix
music = pd.read_csv("J:\#Recommendation-System\Systems\Music_Recomendation_System\Music-Recomendation-System.csv")

similarity = np.load("J:\#Recommendation-System\Models\music_recommendation_model.pkl", allow_pickle=True)

"""
    Recommend similar music tracks based on the given music title.
    Uses a precomputed similarity matrix.
"""
def recommend(music_title):
    try:
        music_index = music[music['Song-Name'] == music_title].index[0]
        distances = similarity[music_index]
        recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:16]
        recommended_musics = [music.iloc[i[0]]['Song-Name'] for i in recommended_indices]
        recommended_musics_posters = [fetch_poster(music.iloc[i[0]]['Song-Name']) for i in recommended_indices]
        return recommended_musics, recommended_musics_posters
    except Exception:
        return [], []


def get_top_genres():
    """Fetch top 4 genres with their top 5 songs."""
    top_genres = music['Genre'].value_counts().nlargest(4).index.tolist()
    genre_music = {
        genre: music[music['Genre'] == genre].head(5)[['Song-Name', 'Genre']].to_dict('records')
        for genre in top_genres
    }
    return genre_music



# Streamlit UI
st.title('🎵 Music Recommendation System')

# Creating tabs
tab1, tab2, tab3 = st.tabs(["Recommendation", "Genres", "Albums/Movies"])

with tab1:
    st.subheader("🎧 Music Recommendation")
    selected_music = st.selectbox('Select a music', music['Song-Name'].values)
    if st.button('Recommend', key="music_recommend"):
        names, posters = recommend(selected_music)
        if len(names) >= 15:
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.text(names[0])
                st.image(posters[0])
                st.text(names[1])
                st.image(posters[1])
                st.text(names[2])
                st.image(posters[2])
                st.text(names[3])
                st.image(posters[3])
                st.text(names[4])
                st.image(posters[4])
            
            with col2:
                st.text(names[5])
                st.image(posters[5])
                st.text(names[6])
                st.image(posters[6])
                st.text(names[7])
                st.image(posters[7])
                st.text(names[8])
                st.image(posters[8])
                st.text(names[9])
                st.image(posters[9])
            
            with col3:
                st.text(names[10])
                st.image(posters[10])
                st.text(names[11])
                st.image(posters[11])
                st.text(names[12])
                st.image(posters[12])
                st.text(names[13])
                st.image(posters[13])
                st.text(names[14])
                st.image(posters[14])

with tab2:
    st.subheader("🎼 Top 4 Genres")
    genre_data = get_top_genres()
    for genre, songs in genre_data.items():
        st.subheader(f"🎶 {genre}")
        cols = st.columns(5)
        for idx, song in enumerate(songs):
            song_poster = fetch_poster(song['Song-Name'])
            with cols[idx % 5]:
                st.image(song_poster, width=100)
                st.caption(song['Song-Name'])

with tab3:
    st.subheader("🎬 Top 4 Albums/Movies")
    album_data = get_top_albums()
    for album, songs in album_data.items():
        st.subheader(f"📀 {album}")
        cols = st.columns(4)
        for idx, song in enumerate(songs):
            song_poster = fetch_poster(song['Song-Name'])
            with cols[idx % 4]:
                st.image(song_poster, width=100)
                st.caption(song['Song-Name'])
