import streamlit as st
import yt_dlp
import os

# Title of the app
st.title("dTube - YouTube Video Downloader")

# Input for the YouTube URL
video_url = st.text_input("Enter the YouTube video URL")

# Input for the directory to save the video
save_path = st.text_input("Enter the directory path to save the video (e.g., C:/Users/YourName/Downloads)")

# Button to download the video
if st.button("Download Video"):
    if video_url and save_path:
        # Check if the directory exists
        if not os.path.isdir(save_path):
            st.error("The specified directory does not exist. Please enter a valid directory.")
        else:
            try:
                # Inform the user that the download is in progress
                with st.spinner('Downloading... Please wait...'):
                    # Define yt-dlp options
                    ydl_opts = {
                        'format': 'best',  # Choose the best quality format
                        'outtmpl': os.path.join(save_path, 'downloaded_video.mp4'),  # Path for the downloaded video
                    }

                    # Download the video using yt-dlp
                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        ydl.download([video_url])

                    # Notify the user that the download is complete
                    st.success(f"Video has been downloaded successfully to {save_path}!")

                    # Provide a link to download the video (for convenience if needed)
                    video_path = os.path.join(save_path, 'downloaded_video.mp4')
                    with open(video_path, 'rb') as f:
                        st.download_button('Download the video', f, file_name='downloaded_video.mp4')

            except Exception as e:
                st.error(f"An error occurred: {e}")

    elif not video_url:
        st.error("Please enter a valid YouTube URL.")
    elif not save_path:
        st.error("Please enter a valid directory path to save the video.")
