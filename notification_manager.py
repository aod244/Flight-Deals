from twilio.rest import Client

ACCOUNT_SID = 'Twilio account SID'
AUTH_TOKEN = 'Twilio account Token'
VIRTUAL_NUMBER = 'Twilio number'
VERIFIED_NUMBER = '+Yours verified number'


class NotificationManager:

    def __init__(self):
        self.client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def send_sms(self, flight_data):
        fly_date = flight_data['local_departure'].split("T")
        back_date = flight_data['route'][1]['local_departure'].split("T")
        message = self.client.messages.create(
            from_=VIRTUAL_NUMBER,
            body=f"Low price alert! Only £{flight_data['price']} to fly from "
                 f"{flight_data['cityFrom']}-{flight_data['flyFrom']} to "
                 f"{flight_data['cityTo']}-{flight_data['flyTo']} from "
                 f"{fly_date[0]} to {back_date[0]}.",
            to=VERIFIED_NUMBER
        )
