import streamlit as st  
import pandas as pd  
import numpy as np  
import joblib  
import requests  
import os
import gdown
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
OMDB_API_KEY = os.getenv("OMDB_API_KEY")  
MOVIE_REC_MODEL_URL = os.getenv("MOVIE_REC_MODEL_URL")
MOVIE_RECOMMENDATION_MODEL_URL = os.getenv("MOVIE_RECOMMENDATION_MODEL_URL")

# Define local file path for movie data
movie_data_path = "./Systems/Movie_Recomendation_System/Movie-Recomendatation.csv"
#J://#Recommendation-System//Systems//Movie_Recomendation_System//Movie-Recomendatation.csv
# Download models from Google Drive if not available locally
def download_model(url, output_path):
    if not os.path.exists(output_path):
        gdown.download(url, output_path, quiet=False)

# Download models
try:
    download_model(MOVIE_REC_MODEL_URL, "movie_rec_model.pkl")
    download_model(MOVIE_RECOMMENDATION_MODEL_URL, "movie_recommendation_model.pkl")
except Exception as e:
    st.error(f"❌ Error downloading models: {e}")
    st.stop()

# Load Similarity Model
try:
    similarity = joblib.load("movie_recommendation_model.pkl")  # Load from downloaded file
except Exception as e:
    st.error(f"❌ Error loading similarity model: {e}")
    st.stop()

# Load Movie Dictionary
try:
    movie_dict = joblib.load("movie_rec_model.pkl")  # Load from downloaded file
    movies = pd.DataFrame(movie_dict)  # Convert to DataFrame
except Exception as e:
    st.error(f"❌ Error loading movie dictionary: {e}")
    st.stop()

# Load Top 4 Genres and Movies
def get_top_genres(movie_data_path):
    """Fetch top 4 genres with the most movies and return 5 movies per genre."""
    if not os.path.exists(movie_data_path):
        st.error(f"❌ File not found: {movie_data_path}")
        return {}
    
    movies_df = pd.read_csv(movie_data_path)
    if 'genre' not in movies_df.columns or 'title' not in movies_df.columns:
        st.error("❌ Required columns 'genre' or 'title' not found in dataset.")
        return {}
    
    top_genres = movies_df['genre'].value_counts().nlargest(4).index.tolist()
    genre_movies = {
        genre: movies_df[movies_df['genre'] == genre]['title'].head(5).tolist()
        for genre in top_genres
    }
    
    return genre_movies

all_movies_by_genre = get_top_genres(movie_data_path)

# Function to Fetch Movie Poster
def fetch_poster(movie_title):
    """Fetches movie poster URL from OMDb API."""
    if not OMDB_API_KEY:
        return "https://via.placeholder.com/500"  # Default if API key is missing
    
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        if data.get("Poster") and data["Poster"] != "N/A":
            return data["Poster"]
    except Exception as e:
        print(f"Error fetching poster for {movie_title}: {e}")
    
    return "https://via.placeholder.com/500"  # Default placeholder image

# Function to Recommend Movies
def recommend(movie_title):
    """Recommends similar movies based on a given movie title."""
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
        distances = similarity[movie_index]
        
        recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:11]
        recommended_movies = [movies.iloc[i[0]].title for i in recommended_indices]
        recommended_posters = [fetch_poster(movies.iloc[i[0]].title) for i in recommended_indices]
        
        return recommended_movies, recommended_posters
    except Exception as e:
        print(f"Error in recommendation for {movie_title}: {e}")
        return [], []

# Streamlit UI
st.title('🎬 Movie Recommendation System')

# Create Tabs
tab1, tab2 = st.tabs(["Recommendation", "Genres"])

with tab1:
    st.subheader("🎥 Movie Recommendation")
    selected_movie = st.selectbox('Select a movie:', movies['title'].values)
    if st.button('Recommend', key="movie_recommend"):
        recommended_movies, recommended_posters = recommend(selected_movie)
        if recommended_movies:
            cols = st.columns(3)
            for idx, (movie_name, movie_poster) in enumerate(zip(recommended_movies, recommended_posters)):
                with cols[idx % 3]:
                    st.image(movie_poster, width=150)
                    st.caption(movie_name)
        else:
            st.error("No recommendations found. Try selecting another movie.")

with tab2:
    st.subheader("🎞 Top 4 Movie Genres")
    for genre, movies_list in all_movies_by_genre.items():
        st.subheader(f"🎭 {genre}")
        cols = st.columns(5)
        for idx, movie in enumerate(movies_list):
            movie_poster = fetch_poster(movie)
            with cols[idx % 5]:
                st.image(movie_poster, width=100)
                st.caption(movie)