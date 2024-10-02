import streamlit as st
import requests

# Define the NewsAPI key for US news
newsapi_key = 'f8c4f524fa2c4ff39d9ff6e2e5f26b06'

# Define the Mediastack API key for Bangladesh, Canada, and United Kingdom
mediastack_api_key = 'ef428460a8cafa651282b4799965b525'

# Define available countries and the corresponding APIs to use
country_options = {
    'United States': 'us',
    'Bangladesh': 'bd',
    'Canada': 'ca',
    'United Kingdom': 'gb'
}

# Function to fetch top news from NewsAPI for the United States
def get_top_news_from_newsapi(country_code):
    url = f"https://newsapi.org/v2/top-headlines?country={country_code}&apiKey={newsapi_key}&pageSize=10"
    response = requests.get(url)
    
    if response.status_code != 200:
        st.error(f"Error fetching news from NewsAPI: {response.status_code} - {response.text}")
        return None
    return response.json()

# Function to fetch top news from Mediastack API for Bangladesh, Canada, and United Kingdom
def get_top_news_from_mediastack(country_code):
    url = f"http://api.mediastack.com/v1/news?access_key={mediastack_api_key}&countries={country_code}&limit=10"
    response = requests.get(url)

    if country_code == 'bd':
        if response.json().get('count', 0) == 0:
            st.warning("No news available for Bangladesh at the moment.")
    
    if response.status_code != 200:
        st.error(f"Error fetching news from Mediastack: {response.status_code} - {response.text}")
        return None
    return response.json()

# Streamlit app
def run():
    # Create a dropdown for country selection
    selected_country = st.sidebar.selectbox("Select a Country", list(country_options.keys()))

    # Fetch news based on the selected country
    if selected_country == 'United States':
        news_data = get_top_news_from_newsapi('us')  # Use NewsAPI for US news
    else:
        country_code = country_options[selected_country]
        news_data = get_top_news_from_mediastack(country_code)  # Use Mediastack for other countries

    # Display the news
    if news_data:
        if selected_country == 'United States':
            if news_data.get('status') == 'ok' and news_data.get('totalResults', 0) > 0:
                st.title(f"Top 10 News in {selected_country}")
                articles = news_data['articles']
                for i, article in enumerate(articles):
                    st.subheader(f"{i + 1}. {article['title']}")
                    st.write(article['description'] if article['description'] else "No description available")
                    st.write(f"Source: {article['source']['name']}")
                    st.write(f"[Read more]({article['url']})")
                    st.write("---")
            else:
                st.write("No news found for the United States.")
        else:
            if 'data' in news_data and len(news_data['data']) > 0:
                st.title(f"Top 10 News in {selected_country}")
                articles = news_data['data']
                for i, article in enumerate(articles):
                    st.subheader(f"{i + 1}. {article['title']}")
                    st.write(article['description'] if article['description'] else "No description available")
                    st.write(f"Source: {article['source']}")
                    st.write(f"[Read more]({article['url']})")
                    st.write("---")
            else:
                st.write(f"No news found for {selected_country}.")
    else:
        st.write("Error retrieving the news.")

# Run the app
if __name__ == "__main__":
    run()
