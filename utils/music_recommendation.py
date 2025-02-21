# import streamlit as st  # Streamlit for web UI
# import pandas as pd  # Pandas for handling data
# import numpy as np  # NumPy for numerical operations
# import pickle  # Pickle for loading pre-trained models
# import requests  # Requests for API calls

# def fetch_poster(music_title):
#     """
#     Fetch the poster URL of a music track using an API.
#     If no image is found, a placeholder image is used.
#     """
#     url = f"https://saavn.dev/api/search/songs?query={music_title}"
#     response = requests.get(url)
    
#     try:
#         data = response.json()
        
#         # Debugging: Print the entire API response for reference
#         print("API Response:", data) 
        
#         # Extract image URL if available
#         if "data" in data and "results" in data["data"] and len(data["data"]["results"]) > 0:
#             song_data = data["data"]["results"][0]  # Taking the first result
            
#             # Checking if 'image' key exists and has high-quality images
#             if "image" in song_data and len(song_data["image"]) >= 3:
#                 image_url = song_data["image"][2]["url"]  # Fetch high-quality image (500x500)
#                 print(f"Fetched Image URL: {image_url}")  # Debugging
#                 return image_url
            
#     except Exception as e:
#         print(f"Error parsing API response: {e}")
    
#     # Return a placeholder image if fetching fails
#     return "https://via.placeholder.com/500"

# def recommend(music_title):
#     """
#     Recommend similar music tracks based on the given music title.
#     Uses a precomputed similarity matrix.
#     """
#     try:
#         music_index = music[music['title'] == music_title].index[0]  # Get index of selected music
#         distances = similarity[music_index]  # Fetch similarity scores
        
#         # Sort music by similarity score in descending order (excluding itself)
#         recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:6]
        
#         recommended_musics = []
#         recommended_musics_posters = []
        
#         for i in recommended_indices:
#             recommended_title = music.iloc[i[0]].title
#             recommended_musics.append(recommended_title)
#             recommended_musics_posters.append(fetch_poster(recommended_title))  # Fetch poster
        
#         return recommended_musics, recommended_musics_posters
#     except Exception as e:
#         print(f"Error in recommendation: {e}")
#         return [], []

# # Load the pre-trained recommendation model and similarity matrix
# music_dict = pickle.load(open(r"J:\#Recommendation-System\Models\music_rec_model.pkl", "rb")) 
# music = pd.DataFrame(music_dict)  # Convert loaded dictionary to DataFrame

# similarity = np.load(r"J:\#Recommendation-System\Models\music_recommendation_model.pkl", allow_pickle=True)

# # Streamlit UI
# st.title('Music Recommendation System')  # Set title of the web app

# # Dropdown to select a music track
# selected_music = st.selectbox('Select a music', music['title'].values)

# # Button to generate recommendations
# if st.button('Recommend'):
#     names, posters = recommend(selected_music)
    
#     # Debugging: Print fetched posters
#     print("Fetched Posters:", posters)
    
#     # Display recommendations in columns for better UI
#     cols = st.columns(5)  # Create five columns
#     for col, name, poster in zip(cols, names, posters):
#         with col:
#             st.text(name)  # Show recommended music name
#             st.image(poster)  # Show corresponding music poster

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
        
        # Debugging: Print the entire API response for reference
        print("API Response:", data) 
        
        # Extract image URL if available
        if "data" in data and "results" in data["data"] and len(data["data"]["results"]) > 0:
            song_data = data["data"]["results"][0]  # Taking the first result
            
            # Checking if 'image' key exists and has high-quality images
            if "image" in song_data and len(song_data["image"]) >= 3:
                image_url = song_data["image"][2]["url"]  # Fetch high-quality image (500x500)
                print(f"Fetched Image URL: {image_url}")  # Debugging
                return image_url
            
    except Exception as e:
        print(f"Error parsing API response: {e}")
    
    # Return a placeholder image if fetching fails
    return "https://via.placeholder.com/500"

def recommend(music_title):
    """
    Recommend similar music tracks based on the given music title.
    Uses a precomputed similarity matrix.
    """
    try:
        music_index = music[music['title'] == music_title].index[0]  # Get index of selected music
        distances = similarity[music_index]  # Fetch similarity scores
        
        # Sort music by similarity score in descending order (excluding itself)
        recommended_indices = sorted(list(enumerate(distances)), key=lambda x: x[1], reverse=True)[1:16]  # Increased to 15
        
        recommended_musics = [music.iloc[i[0]].title for i in recommended_indices]
        recommended_musics_posters = [fetch_poster(music.iloc[i[0]].title) for i in recommended_indices]
        
        return recommended_musics, recommended_musics_posters
    except Exception as e:
        print(f"Error in recommendation: {e}")
        return [], []

# Load the pre-trained recommendation model and similarity matrix
music_dict = pickle.load(open(r"J:\#Recommendation-System\Models\music_rec_model.pkl", "rb")) 
music = pd.DataFrame(music_dict)  # Convert loaded dictionary to DataFrame

similarity = np.load(r"J:\#Recommendation-System\Models\music_recommendation_model.pkl", allow_pickle=True)

# Streamlit UI
st.title('Music Recommendation System')  # Set title of the web app

# Dropdown to select a music track
selected_music = st.selectbox('Select a music', music['title'].values)

# Button to generate recommendations
if st.button('Recommend'):
    names, posters = recommend(selected_music)
    
    # Debugging: Print fetched posters
    print("Fetched Posters:", posters)
    
    # Display recommendations using manually defined rows and columns
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
