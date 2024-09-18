import streamlit as st
import yt_dlp
import tempfile
import os

# Title of the app
st.title("dTube - YouTube Video Downloader")

# Input for the YouTube URL
video_url = st.text_input("Enter the YouTube video URL")

# Button to download the video
if st.button("Download Video"):
    if video_url:
        try:
            # Inform the user that the download is in progress
            with st.spinner('Downloading... Please wait...'):
                # Create a temporary directory on the Streamlit cloud server
                with tempfile.TemporaryDirectory() as tmpdirname:
                    # Define yt-dlp options to save in the temporary directory
                    ydl_opts = {
                        'format': 'best',
                        'outtmpl': os.path.join(tmpdirname, 'downloaded_video.mp4'),  # Save to the temp directory
                    }

                    # Download the video using yt-dlp
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_url])

                    # Get the full path of the downloaded video
                    video_path = os.path.join(tmpdirname, 'downloaded_video.mp4')

                    # Notify the user that the download is complete
                    st.success(f"Video downloaded successfully!")

                    # Provide a link to download the video from the cloud to their local machine
                    with open(video_path, 'rb') as f:
                        st.download_button('Download the video', f, file_name='downloaded_video.mp4')

        except Exception as e:
            st.error(f"An error occurred: {e}")

    else:
        st.error("Please enter a valid YouTube URL")
