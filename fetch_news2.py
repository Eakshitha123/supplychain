import requests
import csv

# Your API Key
API_KEY = '8f0c6c1305ad4992a325957e93a9c669'

# NewsAPI URL
url = 'https://newsapi.org/v2/everything'

# Parameters for the API request
params = {
    'q': 'supply chain disruption',  # Search query (you can change this)
    'language': 'en',                # Language filter
    'apiKey': API_KEY                # Your API Key
}

# Send the request to NewsAPI
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract articles from the response
    articles = data['articles']

    # Define the CSV file and the headers
    csv_file = 'news_data.csv'
    csv_headers = ['Title', 'Description', 'Source', 'Published At', 'URL']

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(csv_headers)  # Write headers

        # Write each article's data
        for article in articles:
            writer.writerow([
                article['title'],
                article['description'],
                article['source']['name'],
                article['publishedAt'],
                article['url']
            ])

    print(f"Data successfully saved to {csv_file}")
else:
    print(f"Failed to fetch data: {response.status_code}")
