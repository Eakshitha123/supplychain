import requests
import csv

# Your NewsAPI key
api_key = '8f0c6c1305ad4992a325957e93a9c669'  # Replace with your actual API key

# Define the base URL for NewsAPI
url = 'https://newsapi.org/v2/everything'

# Define the query parameters for the API request
params = {
    'q': 'supply chain disruption',  # Search term
    'apiKey': api_key,               # API key
    'language': 'en',                 # Language filter
    'pageSize': 100,                  # Maximum number of articles per page (up to 100)
    'page': 1                         # Start from page 1
}

# List to store the fetched articles
articles = []

# Loop to fetch multiple pages of data
for page in range(1, 6):  # Fetching 5 pages of data
    params['page'] = page  # Update the page number for each iteration
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for article in data['articles']:
            # Clean up descriptions by removing line breaks
            description = article['description'].replace('\n', ' ').replace('\r', '')
            # Write each article's title, cleaned description, and URL into the list
            articles.append([article['title'], description, article['url']])
        print(f"Page {page} fetched successfully.")
    else:
        print(f"Error fetching page {page}: {response.status_code}")

# Save the fetched data to a CSV file with proper encoding
with open('supply_chain_articles.csv', mode='w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Description', 'URL'])  # Write the header row
    writer.writerows(articles)  # Write the article data

print("\nData saved to 'supply_chain_articles.csv'")
