import streamlit as st


def run():
    # Custom CSS for design
    st.markdown(
        """
        <style>
        /* Large quote section */
        .large-quote {
            font-size: 2.5rem;
            font-weight: 600;
            color: #ffffff;
            text-align: center;
            margin-top: 50px;
        }

        /* Container for service description */
        .services-section {
            display: flex;
            justify-content: space-between;
            margin-top: 40px;
        }

        /* Individual service items */
        .service-item {
            width: 45%;
            background-color: #111;
            padding: 20px;
            color: #dddddd;
            font-size: 1.1rem;
            border-radius: 10px;
        }

        /* Heading for services */
        .service-title {
            font-size: 1.5rem;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Adjust font sizes for smaller screens */
        @media (max-width: 768px) {
            .large-quote {
                font-size: 1.8rem;
            }

            .service-item {
                width: 100%;
                margin-bottom: 20px;
            }

            .services-section {
                flex-direction: column;
            }
        }

        /* Style for the copyright at the bottom */
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            text-align: center;
            padding: 10px 0;
            background-color: #111;
            color: #888888;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add large quote
    st.markdown(
        """
        <div class="large-quote">
            Your one-stop solution for downloading YouTube videos, streaming content, and staying up to date with the latest news.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add service descriptions
    st.markdown(
        """
        <div class="services-section">
            <div class="service-item">
                <div class="service-title">YouTube Video Downloader</div>
                <p>
                    With our powerful YouTube downloader, you can easily download your favorite videos in the highest quality. 
                    Simple, fast, and effective – it's never been easier to save your favorite content.
                </p>
            </div>
            <div class="service-item">
                <div class="service-title">Stream Latest Videos</div>
                <p>
                    In addition to downloading, you can stream the videos directly from our platform.
                    Stay entertained with the latest and greatest videos at your fingertips.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add additional content for latest news
    st.markdown(
        """
        <div class="services-section">
            <div class="service-item">
                <div class="service-title">Latest News</div>
                <p>
                    Stay informed with our latest news feature. From tech updates to entertainment and global events, 
                    get the news that matters, all in one place.
                </p>
            </div>
            <div class="service-item">
                <div class="service-title">User-Friendly Interface</div>
                <p>
                    Our platform is designed with simplicity in mind. Whether you're downloading videos, streaming content, 
                    or reading the news, our interface is easy to navigate, ensuring a smooth user experience.
                </p>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add copyright footer at the bottom
    st.markdown(
        """
        <div class="footer">
            © 2024 Mohaimin
        </div>
        """,
        unsafe_allow_html=True
    )
