import os
import sqlite3
from dotenv import load_dotenv
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from slack_notifications import send_slack_notification

# Load environment variables
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Setup device for model execution
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")

# Load model and tokenizer
model_path = "./t5_nlp"
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=True)
model = AutoModelForSeq2SeqLM.from_pretrained(model_path).to(device)

# Database setup
db_name = 'news_data.db'
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Fetch latest news articles
cursor.execute("SELECT title FROM news_articles LIMIT 3")  # Process only 3 articles
news_articles = cursor.fetchall()

def estimate_severity(news_article):
    """Estimate severity based on keywords in the news article."""
    high_impact_areas = ["Idukki", "Wayanad", "Kerala"]
    low_impact_areas = ["Alappuzha", "Ernakulam", "Kannur", "Kasaragod"]

    severe_events = ["flood", "drought", "landslide"]
    normal_events = ["Heavy rains", "Mild flooding", "Pest outbreaks"]

    news_lower = news_article.lower()

    if any(area.lower() in news_lower for area in high_impact_areas):
        if any(event in news_lower for event in severe_events):
            return "High Severity"
        elif any(event in news_lower for event in normal_events):
            return "Moderate Severity"
    elif any(area.lower() in news_lower for area in low_impact_areas):
        if any(event in news_lower for event in severe_events):
            return "Moderate Severity"
        elif any(event in news_lower for event in normal_events):
            return "Low Severity"

for article in news_articles:
    news_article = article[0]

    inputs = tokenizer(f"Classify Sentiment: {news_article}", return_tensors="pt").to(device)
    outputs = model.generate(inputs.input_ids, max_length=150, num_beams=8, early_stopping=True)

    sentiment = tokenizer.decode(outputs[0], skip_special_tokens=True)

    if sentiment == "negative":
        severity = estimate_severity(news_article)

        if severity:
            send_slack_notification(f"Potential supply chain disruption detected!\nSeverity: {severity}\nNews: {news_article}")

conn.close()
