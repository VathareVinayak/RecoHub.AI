# import pickle  # Pickle for loading models
# import streamlit as st  # Streamlit for UI
# import pandas as pd  # Pandas for data handling
# import numpy as np  # NumPy for numerical operations
# import joblib  # Joblib for loading models
# import requests  # Requests for API calls
# import gdown  # gdown to fetch from Google Drive
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve the OMDB API key securely
# OMDB_API_KEY = os.getenv("OMDB_API_KEY")


# def fetch_poster(movie_title):
#     """
#     Fetches the movie poster URL from the OMDb API.
#     If no valid image is found, returns a placeholder image.
#     """
#     url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    
#     try:
#         response = requests.get(url)
#         data = response.json()
        
#         # Check if the response contains a valid poster
#         if data.get("Poster") and data["Poster"] != "N/A":
#             return data["Poster"]
#     except Exception as e:
#         print(f"Error fetching poster for {movie_title}: {e}")
    
#     # Return a default placeholder image if API request fails
#     return "https://via.placeholder.com/500"


# def recommend(movie_title):
#     """
#     Recommends similar movies based on the given movie title using a similarity matrix.
#     Returns lists of recommended movie names and their corresponding poster URLs.
#     """
#     try:
#         # Locate the index of the selected movie
#         movie_index = movies[movies['title'] == movie_title].index[0]
#         distances = similarity[movie_index]  # Fetch similarity scores
        
#         # Retrieve top 15 most similar movies (excluding the selected movie itself)
#         recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:16]
        
#         # Extract recommended movie titles and their posters
#         recommended_movies = [movies.iloc[i[0]].title for i in recommended_indices]
#         recommended_posters = [fetch_poster(movies.iloc[i[0]].title) for i in recommended_indices]
        
#         return recommended_movies, recommended_posters

#     except Exception as e:
#         print(f"Error in recommendation for {movie_title}: {e}")
#         return [], []


# # Load the pre-trained recommendation model and similarity matrix
# movie_dict = pickle.load(open(r"J:\#Recommendation-System\Models\movie_rec_model.pkl", "rb"))
# movies = pd.DataFrame(movie_dict)  # Convert loaded dictionary to DataFrame

# similarity = np.load(r"J:\#Recommendation-System\Models\movie_recommendation_model.pkl", allow_pickle=True)

# # Streamlit UI
# st.title('🎬 Movie Recommendation System')

# # Dropdown menu for movie selection
# selected_movie = st.selectbox('Select a movie:', movies['title'].values)

# # When the "Recommend" button is clicked
# if st.button('Recommend'):
#     recommended_movies, recommended_posters = recommend(selected_movie)
    
#     if recommended_movies:
#         # Organize recommended movies into three columns
#         cols = st.columns(3)

#         # Display recommendations in a structured format
#         for idx, (movie_name, movie_poster) in enumerate(zip(recommended_movies, recommended_posters)):
#             with cols[idx % 3]:  # Distribute movies evenly across columns
#                 st.image(movie_poster, width=150)
#                 st.caption(movie_name)
#     else:
#         st.error("No recommendations found. Try selecting another movie.")





# import streamlit as st  # Streamlit for UI
# import pandas as pd  # Pandas for data handling
# import numpy as np  # NumPy for numerical operations
# import joblib  # Joblib for loading models
# import requests  # Requests for API calls
# import zipfile  # Zipfile for handling compressed files
# import os
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Retrieve the OMDb API key securely
# OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# def fetch_poster(movie_title):
#     """
#     Fetches the movie poster URL from the OMDb API.
#     If no valid image is found, returns a placeholder image.
#     """
#     if not OMDB_API_KEY:
#         return "https://via.placeholder.com/500"  # Placeholder if API key is missing
    
#     url = f"http://www.omdbapi.com/?t={movie_title}&apikey={OMDB_API_KEY}"
    
#     try:
#         response = requests.get(url)
#         data = response.json()
        
#         # Check if the response contains a valid poster
#         if data.get("Poster") and data["Poster"] != "N/A":
#             return data["Poster"]
#     except Exception as e:
#         print(f"Error fetching poster for {movie_title}: {e}")
    
#     return "https://via.placeholder.com/500"  # Default placeholder image

# def recommend(movie_title):
#     """
#     Recommends similar movies based on the given movie title using a similarity matrix.
#     Returns lists of recommended movie names and their corresponding poster URLs.
#     """
#     try:
#         # Locate the index of the selected movie
#         movie_index = movies[movies['title'] == movie_title].index[0]
#         distances = similarity[movie_index]  # Fetch similarity scores
        
#         # Retrieve top 15 most similar movies (excluding the selected movie itself)
#         recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:16]
        
#         # Extract recommended movie titles and their posters
#         recommended_movies = [movies.iloc[i[0]].title for i in recommended_indices]
#         recommended_posters = [fetch_poster(movies.iloc[i[0]].title) for i in recommended_indices]
        
#         return recommended_movies, recommended_posters

#     except Exception as e:
#         print(f"Error in recommendation for {movie_title}: {e}")
#         return [], []
# import zipfile
# import os
# import joblib


# # Define paths
# zip_path = r"J:\#Recommendation-System\utils\movie_recommendation_model.zip"
# extract_to = r"J:\#Recommendation-System\utils"
# joblib_file = os.path.join(extract_to, "movie_recommendation_model.joblib")

# # 📌 Step 1: Extract if not already extracted
# if not os.path.exists(joblib_file):  # Only extract if missing
#     if os.path.exists(zip_path):
#         with zipfile.ZipFile(zip_path, "r") as zip_ref:
#             zip_ref.extractall(extract_to)  # Extract files
#             print(f"✅ Extracted files to: {extract_to}")
#     else:
#         print(f"❌ ZIP file not found at: {zip_path}")

# # 📌 Step 2: Ensure the joblib file exists before loading
# if os.path.exists(joblib_file):
#     similarity = joblib.load(joblib_file)
#     print("✅ Model loaded successfully!")
# else:
#     print(f"❌ Model file not found at: {joblib_file}")


# # 📌 Load the pre-trained recommendation model
# movie_dict = joblib.load(r"J:\#Recommendation-System\utils\movie_rec_model.joblib")

# movies = pd.DataFrame(movie_dict)  # Convert loaded dictionary to DataFrame

# # 📌 Load similarity matrix
# similarity = joblib.load("movie_recommendation_model.joblib")

# # Streamlit UI
# st.title('🎬 Movie Recommendation System')

# # Dropdown menu for movie selection
# selected_movie = st.selectbox('Select a movie:', movies['title'].values)

# # When the "Recommend" button is clicked
# if st.button('Recommend'):
#     recommended_movies, recommended_posters = recommend(selected_movie)
    
#     if recommended_movies:
#         # Organize recommended movies into three columns
#         cols = st.columns(3)

#         # Display recommendations in a structured format
#         for idx, (movie_name, movie_poster) in enumerate(zip(recommended_movies, recommended_posters)):
#             with cols[idx % 3]:  # Distribute movies evenly across columns
#                 st.image(movie_poster, width=150)
#                 st.caption(movie_name)
#     else:
#         st.error("No recommendations found. Try selecting another movie.")






import streamlit as st  
import pandas as pd  
import numpy as np  
import joblib  
import requests  
import bz2  
import os
from dotenv import load_dotenv

# 🔹 Load environment variables from .env file
load_dotenv()

# 🔹 Retrieve API key
OMDB_API_KEY = os.getenv("OMDB_API_KEY")  

# 🔹 Define file paths
movie_dict_file = "J:/#Recommendation-System/Models/movie_rec_model.joblib"  # Local file
similarity_model_file = "J:/#Recommendation-System/Models/movie_recommendation_model.joblib"  # Local similarity model

# ✅ Step 1: Load Similarity Model
try:
    similarity = joblib.load(similarity_model_file)  # Load locally
    st.write("✅ Recommendation Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Error loading similarity model: {e}")
    st.stop()

# ✅ Step 2: Load Movie Dictionary (Local File)
try:
    movie_dict = joblib.load(movie_dict_file)  # Load locally
    movies = pd.DataFrame(movie_dict)  # Convert to DataFrame
    st.write("✅ Movie Dictionary Loaded Successfully!")
except Exception as e:
    st.error(f"❌ Error loading movie dictionary: {e}")
    st.stop()

# 📌 Function to Fetch Movie Poster
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

# 📌 Function to Recommend Movies
def recommend(movie_title):
    """Recommends similar movies based on a given movie title."""
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
        distances = similarity[movie_index]
        
        recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:16]
        recommended_movies = [movies.iloc[i[0]].title for i in recommended_indices]
        recommended_posters = [fetch_poster(movies.iloc[i[0]].title) for i in recommended_indices]
        
        return recommended_movies, recommended_posters

    except Exception as e:
        print(f"Error in recommendation for {movie_title}: {e}")
        return [], []

# 📌 Streamlit UI
st.title('🎬 Movie Recommendation System')

# Dropdown for movie selection
selected_movie = st.selectbox('Select a movie:', movies['title'].values)

# "Recommend" button
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
