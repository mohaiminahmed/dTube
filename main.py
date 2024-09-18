import streamlit as st
import yt_dlp
import tempfile
import os

# Title of the app
st.title("dTube - YouTube Video Downloader")

# Input for the YouTube URL
video_url = st.text_input("Enter the YouTube video URL")

# Button to download the video
if st.button("Process Download"):
    if video_url:
        try:
            # Inform the user that the download is in progress
            with st.spinner('Downloading... Please wait...'):
                # Create a temporary directory on the cloud server
                with tempfile.TemporaryDirectory() as tmpdirname:
                    # Define yt-dlp options to save in the temporary directory
                    ydl_opts = {
                        'format': 'best',  # Choose the best quality format
                        'outtmpl': os.path.join(tmpdirname, 'downloaded_video.mp4'),  # Path for the downloaded video
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

# Add a credit line at the bottom of the app
st.markdown("---")  # Add a horizontal line for separation
st.markdown("<h5 style='text-align: center;'>Created by Mohaimin</h5>", unsafe_allow_html=True)

