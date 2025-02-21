import pickle  # Pickle for loading models
import streamlit as st  # Streamlit for UI
import pandas as pd  # Pandas for data handling
import numpy as np  # NumPy for numerical operations
import joblib  # Joblib for loading models
import requests  # Requests for API calls
import gdown  # gdown to fetch from Google Drive
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OMDB API key securely
OMDB_API_KEY = os.getenv("OMDB_API_KEY")


def fetch_poster(movie_title):
    """
    Fetches the movie poster URL from the OMDb API.
    If no valid image is found, returns a placeholder image.
    """
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Check if the response contains a valid poster
        if data.get("Poster") and data["Poster"] != "N/A":
            return data["Poster"]
    except Exception as e:
        print(f"Error fetching poster for {movie_title}: {e}")
    
    # Return a default placeholder image if API request fails
    return "https://via.placeholder.com/500"


def recommend(movie_title):
    """
    Recommends similar movies based on the given movie title using a similarity matrix.
    Returns lists of recommended movie names and their corresponding poster URLs.
    """
    try:
        # Locate the index of the selected movie
        movie_index = movies[movies['title'] == movie_title].index[0]
        distances = similarity[movie_index]  # Fetch similarity scores
        
        # Retrieve top 15 most similar movies (excluding the selected movie itself)
        recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:16]
        
        # Extract recommended movie titles and their posters
        recommended_movies = [movies.iloc[i[0]].title for i in recommended_indices]
        recommended_posters = [fetch_poster(movies.iloc[i[0]].title) for i in recommended_indices]
        
        return recommended_movies, recommended_posters

    except Exception as e:
        print(f"Error in recommendation for {movie_title}: {e}")
        return [], []


# Load the pre-trained recommendation model and similarity matrix
movie_dict = pickle.load(open(r"J:\#Recommendation-System\Models\movie_rec_model.pkl", "rb"))
movies = pd.DataFrame(movie_dict)  # Convert loaded dictionary to DataFrame

similarity = np.load(r"J:\#Recommendation-System\Models\movie_recommendation_model.pkl", allow_pickle=True)

# Streamlit UI
st.title('🎬 Movie Recommendation System')

# Dropdown menu for movie selection
selected_movie = st.selectbox('Select a movie:', movies['title'].values)

# When the "Recommend" button is clicked
if st.button('Recommend'):
    recommended_movies, recommended_posters = recommend(selected_movie)
    
    if recommended_movies:
        # Organize recommended movies into three columns
        cols = st.columns(3)

        # Display recommendations in a structured format
        for idx, (movie_name, movie_poster) in enumerate(zip(recommended_movies, recommended_posters)):
            with cols[idx % 3]:  # Distribute movies evenly across columns
                st.image(movie_poster, width=150)
                st.caption(movie_name)
    else:
        st.error("No recommendations found. Try selecting another movie.")
