import streamlit as st
from streamlit_option_menu import option_menu
from st_social_media_links import SocialMediaIcons

# Sidebar Navigation
with st.sidebar:
    selected = option_menu(
        "   RecoHub.AI",
        ["Home", "Movie Recommendation", "Music Recommendation", "Podcast Recommendation"],
        icons=["house", "film", "music-note-beamed", "mic"],  # Using 'music-note-beamed' as an alternative
        menu_icon="menu-app",  # Sidebar menu icon
        default_index=0,  # Default to Home
        styles={
            "container": {"background-color": "#1E1E1E"},  # Dark background
            "icon": {"color": "white", "font-size": "20px"},  # White icons
            "nav-link": {"font-size": "16px", "color": "white", "text-align": "left", "margin": "5px"},
            "nav-link-selected": {"background-color": "#4CAF50"},  # Highlight color for selected menu
        }
    )


# Function to execute a script dynamically
def run_script(script_path):
    try:
        with open(script_path, "r", encoding="utf-8") as f:
            script_code = f.read()
        exec(script_code, globals())  # Execute the script safely
    except Exception as e:
        st.error(f"⚠️ Error loading script: {e}")

# Clear previous content before rendering new selection
st.empty()  # Ensures page content is reset before loading new content

# Create a container to hold dynamic content
with st.container():
    if selected == "Movie Recommendation":
        run_script(r"./utils/movie_recommendation.py")

    elif selected == "Music Recommendation":
        run_script(r"./utils/music_recommendation.py")

    elif selected == "Podcast Recommendation":
        run_script(r"./utils/podcast_recommendation.py")

    elif selected == "Home":
        st.title("📢 Welcome to the AI-Based Recommendation")
        st.subheader("An AI-powered recommendation system for entertainment.")

        st.image(r'./images/banner.webp', use_container_width=True)

        # Create tabs for Home, About, and Contact
        tab1, tab2, tab3 = st.tabs(["Home", "About", "Contact"])

        with tab1:
            st.subheader("1️⃣ Objective")
            st.write("""
                The Recommendation Suite is designed to provide users with personalized suggestions 
                for movies, music, and podcasts based on their preferences.
            """)

            st.subheader("2️⃣ Features")
            st.markdown("""
            - **🎥 Movie Recommendation**: Get personalized movie recommendations based on Movie Tastes.
            - **🎵 Music Recommendation**: Discover new songs and artists that match your taste.
            - **🎙 Podcast Recommendation**: Find engaging podcasts based on topics and interests.
            """)

            st.subheader("3️⃣ Navigation")
            st.markdown("""
            - Use the **sidebar menu** to select the type of recommendation you need.
            - Click on a category (Movies, Music, or Podcasts) to get tailored suggestions.
            """)

            st.subheader("4️⃣ Input Data")
            st.markdown("""
            - **Movies & Music**: Enter the name of a movie or a music track to receive recommendations.
            - **Podcasts**: Select a **language and a category** to get podcast suggestions.
            """)

            st.subheader("5️⃣ Recommendation Outputs")
            st.write("""
            - The system displays a **list of recommended content**.
            """)

            st.subheader("6️⃣ Accuracy and Improvement")
            st.write("""
            - The recommendation models are built using **machine learning techniques**.
            - **Continuous updates** and user feedback help improve accuracy over time.
            """)

            st.subheader("7️⃣ Ethical Considerations")
            st.write("""
            - **User data is kept private** and is not shared.
            - **Transparent algorithms** ensure unbiased recommendations.
            """)

            st.subheader("✨ Get Started")
            st.write("Select a recommendation category from the sidebar and explore personalized suggestions!")

        with tab2:
            st.markdown("""
            <style>
            @keyframes wave {
                0% { transform: rotate(0deg); }
                10% { transform: rotate(14deg); }
                20% { transform: rotate(-8deg); }
                30% { transform: rotate(14deg); }
                40% { transform: rotate(-4deg); }
                50% { transform: rotate(10deg); }
                60% { transform: rotate(0deg); }
                100% { transform: rotate(0deg); }
            }
            .wave {
                display: inline-block;
                animation: wave 2s infinite;
                font-size: 2rem;
            }
            </style>
            <h1>Hello, Folks! <span class="wave">👋</span></h1>
        """, unsafe_allow_html=True)
            st.title("I am Vinayak Vathare!")

            st.write("""
                I'm a passionate Data Scientist and Machine Learning Enthusiast with a strong drive to transform data into actionable insights.
                My expertise spans across Python, Data Science, and Machine Learning, with hands-on experience in data visualization, database management, and analytics.
            """)

            st.write("""
                Throughout my journey, I have worked on diverse projects, including Movie, Music, and Podcast Recommendation Systems, implementing cutting-edge algorithms to enhance user experiences.
                I actively engage in data analysis, Power BI projects, and automation techniques to extract meaningful patterns and trends from complex datasets.
            """)

            st.write("""
                I am eager to collaborate on projects, hackathons, and industry-level challenges that require innovation and problem-solving through data-driven solutions.
                Let's connect and explore the endless possibilities of AI, Machine Learning, and Data Science to drive impactful change in the world!
            """)

        with tab3:
            st.subheader("Contact")
            st.write("Feel free to reach out for collaborations or inquiries:")
            st.write("- **Email**: work.vinayakvathare@gmail.com")
            st.write("- **LinkedIn**: [Vinayak Vathare](https://www.linkedin.com/in/vinayak-vathare-4bb135279/)")
            st.write("- **GitHub**: [VathareVinayak](https://github.com/VathareVinayak)")

            # Display social media icons
            social_media_links = [
                "https://www.linkedin.com/in/vinayak-vathare-4bb135279/",
                "https://github.com/VathareVinayak",
                "mailto:work.vinayakvathare@gmail.com"
            ]
            social_media_icons = SocialMediaIcons(social_media_links)
            social_media_icons.render()
