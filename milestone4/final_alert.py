from news_analysis import estimate_severity
from slack_notifications import send_slack_notification

# Example news article
news_article = "Heavy floods predicted in Idukki in the upcoming days."

severity = estimate_severity(news_article)

if severity == "High Severity":
    send_slack_notification(f"🚨 High Alert! Severe supply chain disruption detected.\nSeverity: HIGH\nNews: {news_article}")
elif severity == "Moderate Severity":
    send_slack_notification(f"⚠️ Moderate Alert! Possible supply chain impact.\nSeverity: MODERATE\nNews: {news_article}")
elif severity == "Low Severity":
    send_slack_notification(f"🔔 Low Alert! Minor supply chain disturbance.\nSeverity: LOW\nNews: {news_article}")
