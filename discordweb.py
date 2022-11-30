import requests
from discord_webhooks import DiscordWebhooks

webhook_url = input("WebhookUrl: ")
title = input("Title: ")
desc = input("Description: ")
message = input("Message: ")
amount = int(input("Amount: "))


webhook = DiscordWebhooks(webhook_url)
webhook.set_content(content=message, title=title, description=desc, \
  url='https://discord.gg/Nuu7EXSQvG', color=0x00000)


for i in range(amount):
    webhook.send()
    print("Spam Webhook Succes ✓")
