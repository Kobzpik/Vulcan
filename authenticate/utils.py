import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
#~~ Also add your own twilio account_sid and auth_token ~~
account_sid = str(os.getenv('account_sid'))
auth_token =str(os.getenv('auth_token'))
client = Client(account_sid, auth_token)

def send_sms(user_code,phone_number):
    message = client.messages \
                .create(
                     body=f"Hi! Your User and verification code is {user_code}",
                     from_='+19034626264',
                     to=f'{phone_number}'
                 )

    print(message.sid)

#SECRET_KEY = str(os.getenv('SECRET_KEY'))