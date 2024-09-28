import streamlit as st
from streamlit_option_menu import option_menu
import dTube  # Import the youtube.py module
import news
import about  # Import the about.py module
import tempfile
import yt_dlp
import os

# Set the page title, layout, and hide menu items (like "Rerun", "Settings", etc.)
st.set_page_config(
    page_title="dTube",
    page_icon=":movie_camera:",
    layout="wide",  # Use wide layout to give more flexibility for positioning
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)

# Capture the selected option from the menu
selected = option_menu(
    menu_title=None,  # Leave blank so that no title appears
    options=["Home", "dTube", "News", "About"],  # Menu options
    icons=["house", "youtube", "newspaper", "info-circle"],  # Icons for each option
    menu_icon="cast",  # Optional: use a cast icon as the menu button
    default_index=0,  # Set the default selected item (0 means "Home")
    orientation="horizontal",  # Set menu orientation to horizontal
    styles={
        "container": {"padding": "0!important", "background-color": "#111"},
        "nav-link": {"font-size": "14px", "text-align": "left", "margin": "0px", "padding": "10px", "--hover-color": "#444"},
        "nav-link-selected": {"background-color": "#FF4B4B"},  # Style for selected item
    },
)

# Show content based on the selected menu item
if selected == "Home":

    # Title of the app
    st.title("dTube - Download YouTube Video")

    # Input for the YouTube URL
    video_url = st.text_input("Enter the YouTube video URL")

    # Animation CSS for a minimalist loading bar
    st.markdown(
        """
        <style>
        .loading-bar {
            width: 100%;
            background-color: #f3f3f3;
            border-radius: 5px;
            overflow: hidden;
            position: relative;
            height: 20px;
            margin-top: 20px;
        }
        .loading-fill {
            height: 100%;
            background-color: #FF4B4B;
            width: 0%;
            animation: load 3s ease-in-out forwards;
        }
        @keyframes load {
            0% { width: 0%; }
            100% { width: 100%; }
        }
        </style>
        """, unsafe_allow_html=True
    )

    # Button to download the video
    if st.button("Process Download"):
        if video_url:
            try:
                # Display animation when the button is clicked
                st.markdown(
                    """
                    <div class="loading-bar">
                        <div class="loading-fill"></div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # Inform the user that the download is in progress
                with st.spinner('Downloading... Please wait...'):
                    # Create a temporary directory on the cloud server
                    with tempfile.TemporaryDirectory() as tmpdirname:
                        # Define yt-dlp options to save in the temporary directory
                        ydl_opts = {
                            'format': 'best',  # Choose the best quality format
                            'outtmpl': os.path.join(tmpdirname, 'downloaded_video.mp4'),
                        }

                        # Download the video using yt-dlp
                        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                            ydl.download([video_url])

                        # Get the full path of the downloaded video
                        video_path = os.path.join(tmpdirname, 'downloaded_video.mp4')

                        # Notify the user that the download is complete
                        st.success("Video has been downloaded successfully!")

                        # Provide a link to download the video
                        with open(video_path, 'rb') as f:
                            st.download_button('SAVE', f, file_name='dTube_Downloader.mp4')

            except Exception as e:
                st.error(f"An error occurred: {e}")

        else:
            st.error("Please enter a valid YouTube URL")

elif selected == "dTube":
    dTube.run()  # This will run the code from youtube.py

elif selected == "News":
    news.run()

elif selected == "About":
    about.run()  # This will run the code from about.py
