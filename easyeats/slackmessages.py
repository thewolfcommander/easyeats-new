import os
from datetime import datetime
from slacker import Slacker
from django.conf import settings

slack = Slacker(settings.SLACK_CLIENT_SECRET)
TEST_CHANNEL = os.environ.get('TEST_SLACK_CHANNEL', None)
channel_details = {
    "#general": {
    "username": 'manoj',
    "icon_url": None,
    "icon_emoji": ":email:"
    },
    "@manoj": {},
}


def post_to_slack(message, channel, username=None):
    try:
        channel = "#general"
        slack.chat.post_message(
            channel=channel,
            text=message,
            username='manoj'
        )
    except Exception as e:
        print("Error")
 

def send_notification(message, channel):
    try:
        post_to_slack(message, channel)
    except Exception as e:
        print("Error")