import streamlit as st
import yt_dlp
import tempfile
import os

def run():
    # Add titles and grid layout for YouTube videos
    st.markdown(
        """
        <style>
        .video-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));  /* Create responsive columns */
            grid-gap: 20px;
            margin-top: 20px;
        }
        .video-item iframe {
            width: 100%;
            height: 200px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # First Row: Islamic Videos
    st.header("Islamic Videos")
    st.markdown(
        """
        <div class="video-grid">
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/nIbnUMqLQ78" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/2SvVxLckOkk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/7kTkaLuFCfk" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Second Row: For Kids
    st.header("Videos For Kids")
    st.markdown(
        """
        <div class="video-grid">
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/yZtXzSJ0Wg0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/ovE8T9e0uyc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/NbIG26OvMRI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Third Row: Educational
    st.header("Educational Videos")
    st.markdown(
        """
        <div class="video-grid">
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/eGguwYPC32I" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/I2O7blSSzpI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
            <div class="video-item">
                <iframe src="https://www.youtube.com/embed/Dx3RpXdJw2k" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
