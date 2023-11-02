from twilio.rest import Client

TWILIO_SID = 'AC4570fa63efab1b73363b811aa4673cd3'
TWILIO_AUTH_TOKEN = "211248edecae245b8c6e88ee3907500c"
TWILIO_VIRTUAL_NUMBER ='+17316137912'
TWILIO_VERIFIED_NUMBER ='+918878530091'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
