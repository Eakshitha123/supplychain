import requests
import os
from dotenv import load_dotenv

# Load environment variables (optional, if you want to keep your API key secure in .env)
load_dotenv()
API_KEY = "8f0c6c1305ad4992a325957e93a9c669"  # Your NewsAPI key

# URL for NewsAPI
url = "https://newsapi.org/v2/everything"
params = {
    "apiKey": API_KEY,
    "q": "supply chain",  # Query for news articles about supply chain
    "language": "en",  # Language of the articles
    "pageSize": 5  # Limit the number of articles
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    for article in data.get("articles", []):
        title = article.get("title", "No title found")
        content = article.get("description", "No content found")  # Using 'description' instead of 'content'
        print(f"Title: {title}")
        print(f"Content: {content}\n")
else:
    print(f"Error fetching news: {response.status_code}")
