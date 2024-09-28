import streamlit as st
import requests


def run():
    # Set your NewsAPI key
    api_key = 'f8c4f524fa2c4ff39d9ff6e2e5f26b06'  # Replace with your actual NewsAPI key

    # Define the available countries (NewsAPI uses 2-letter country codes)
    country_options = {
        'United States': 'us',
        'Bangladesh': 'bd'
        # Add more countries if needed
    }

    # Create a dropdown for country selection
    selected_country = st.sidebar.selectbox("Select a Country", list(country_options.keys()))

    # Function to fetch the top news for the selected country
    def get_top_news(country_code):
        url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={api_key}&pageSize=10"
        response = requests.get(url)
        return response.json()

    # Fetch news when a country is selected
    if selected_country:
        st.title(f"Top 10 News in {selected_country}")

        # Get the country code from the selection
        country_code = country_options[selected_country]

        # Fetch top news for the selected country
        news_data = get_top_news(country_code)

        # Check if the response contains articles
        if news_data['status'] == 'ok' and news_data['totalResults'] > 0:
            articles = news_data['articles']

            # Display the top 10 news articles
            for i, article in enumerate(articles):
                st.subheader(f"{i + 1}. {article['title']}")
                st.write(article['description'] if article['description'] else "No description available")
                st.write(f"Source: {article['source']['name']}")
                st.write(f"[Read more]({article['url']})")
                st.write("---")
        else:
            st.write("No news found for the selected country.")
