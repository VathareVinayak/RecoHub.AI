import streamlit as st
from streamlit_option_menu import option_menu
import os

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "🎬📻🎧 Recommendation Suite",
        ["Home", "Movie Recommendation", "Music Recommendation", "Podcast Recommendation"],
        icons=["house", "film", "music", "headphones"],
        default_index=0
    )

# Function to execute a script dynamically
def run_script(script_path):
    with open(script_path, "r", encoding="utf-8") as f:
        script_code = f.read()
    exec(script_code, globals())  # Execute the script in the global scope

# Movie Recommendation Page
if selected == "Movie Recommendation":
    run_script(r"J:\#Recommendation-System\utils\movie_recommendation.py")

# Music Recommendation Page
elif selected == "Music Recommendation":
    run_script(r"J:\#Recommendation-System\utils\music_recommendation.py")

# Podcast Recommendation Page
elif selected == "Podcast Recommendation":
    run_script(r"J:\#Recommendation-System\utils\podcast_recommendation.py")

# Home Page
else:
    st.title("📢 Welcome to the Recommendation Suite")
    st.write("This app provides recommendations for Movies, Music, and Podcasts.")
    st.write("Select an option from the sidebar to get started!")
