import streamlit as st
import pandas as pd
import pickle
from collections import Counter

# Load the preprocessed dataset
podcast_data_path = "J:\#Recommendation-System\Models\cleaned_podcasts.pkl"  # Update the path if needed
podcasts = pickle.load(open(podcast_data_path, "rb"))

# Streamlit UI
st.title('🎧 Podcast Recommendation System')

# Select Language
languages = podcasts['language'].unique().tolist()
selected_language = st.selectbox("Select a Language", languages)

# Extract unique categories and clean them
tags = []
podcasts['categories'].dropna().apply(lambda x: tags.extend(eval(x) if isinstance(x, str) and x.startswith('[') else [x]))

# Clean the category names (remove brackets, extra quotes)
tags = [tag.strip().replace("'", "").replace('"', '') for tag in tags]

# Sort categories based on popularity (most used first)
tag_counts = Counter(tags)
sorted_tags = [tag for tag, _ in tag_counts.most_common()]

# Display categories with most searched ones at the top
selected_tags = st.multiselect("Select Categories (You can choose multiple)", sorted_tags)

# Recommendation Function
def recommend_podcasts(language, selected_tags):
    filtered_podcasts = podcasts[podcasts['language'] == language]
    
    if selected_tags:
        filtered_podcasts = filtered_podcasts[
            filtered_podcasts['categories'].apply(lambda x: any(tag in eval(x) if isinstance(x, str) and x.startswith('[') else tag in [x] for tag in selected_tags))
        ]
    
    return filtered_podcasts.head(5)  # Return top 5 results

# Button to get recommendations
if st.button("Recommend"):
    recommended_podcasts = recommend_podcasts(selected_language, selected_tags)
    
    if recommended_podcasts.empty:
        st.write("No podcasts found for the selected criteria. Try different tags!")
    else:
        for _, podcast in recommended_podcasts.iterrows():
            st.subheader(podcast['title'])
            st.image(podcast['image'], width=300)
            st.write(f"**Description:** {podcast['description']}")
            st.write(f"**Categories:** {', '.join(eval(podcast['categories'])) if isinstance(podcast['categories'], str) and podcast['categories'].startswith('[') else podcast['categories']}")
            st.write("---")
