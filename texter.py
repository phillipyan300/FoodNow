#Allows us to create a client object to send a request to server
from twilio.rest import Client
from dotenv import load_dotenv
import os


class Texter:
    def __init__(self):
        load_dotenv()
        self.accountSid = os.getenv("ACCOUNT_SID")
        self.accountToken = os.getenv("ACCOUNT_TOKEN")
        self.twilioNumber = os.getenv("TWILIO_NUMBER")

        self.client = Client(self.accountSid, self.accountToken)

    #Template for a single text
    def text(self, bodyText: str, number: str):
        message = self.client.messages.create(
            from_ = self.twilioNumber,
            body = bodyText,
            to = number
        )
        print(message.sid)


if __name__ == "__main__":
    texter = Texter()
    texter.text("New Formatting!", "16092169075")



