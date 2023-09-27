import os
from twilio.rest import Client
from script import get_hottest_post

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

def send_sms(text):
    try:
        client.messages.create(
            from_=os.environ.get('TWILIO_PHONE_NUMBER'),
            to=os.environ.get('CELL_PHONE_NUMBER'),
            body=text
        )
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    post = get_hottest_post()
    send_sms(post)