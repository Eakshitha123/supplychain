from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import requests
import time
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
slack_token = os.getenv("SLACK_TOKEN")  # Slack bot token
channel_id = os.getenv("CHANNEL_ID")    # Slack channel ID

def send_slack_notification(message):
    """Send a message to a Slack channel."""
    client = WebClient(token=slack_token)

    try:
        response = client.chat_postMessage(channel=channel_id, text=message)
        print("Message sent to Slack:", response)
    except SlackApiError as e:
        print(f"Slack API Error: {e.response['error']}")

def delete_last_n_messages(n=1):
    """Delete the last n messages from the Slack channel."""
    headers = {"Authorization": f"Bearer {slack_token}"}

    response = requests.get(
        "https://slack.com/api/conversations.history",
        headers=headers,
        params={"channel": channel_id, "limit": n}
    )

    if not response.json().get("ok"):
        print(f"Failed to fetch messages: {response.json()}")
        return

    messages = response.json().get("messages", [])
    if not messages:
        print("No messages found to delete.")
        return

    for message in messages:
        ts = message["ts"]  # Timestamp of the message
        delete_response = requests.post(
            "https://slack.com/api/chat.delete",
            headers=headers,
            json={"channel": channel_id, "ts": ts}
        )
        if delete_response.status_code == 200 and delete_response.json().get("ok"):
            print(f"Deleted message with timestamp {ts}")
            time.sleep(1)  # Prevent hitting Slack rate limits
        else:
            print(f"Failed to delete message: {delete_response.json()}")
