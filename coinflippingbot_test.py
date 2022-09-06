from slack_sdk import WebClient
from coinflippingbot import CoinFlippingBot
import os
import ssl
import certifi

# add this line to point to your certificate path
ssl_context = ssl.create_default_context(cafile=certifi.where())

# Create a slack client
slack_web_client = WebClient(
    token = os.environ.get("SLACK_TOKEN"),
    base_url = "https://www.slack.com/api/",
    ssl = ssl_context
)

# Get a new CoinBot
coin_bot = CoinFlippingBot("#general")

# Get the onboarding message payload
message = coin_bot.get_message_payload()

# Post the onboarding message in Slack
slack_web_client.chat_postMessage(**message)

#this exercise needs a server or computer with a public IP address for development before
#it can be completed
