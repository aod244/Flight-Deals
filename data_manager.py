import requests

SHEETY_API_ENDPOINT = "Your own sheety api endpoint"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_data(self):
        response = requests.get(url=SHEETY_API_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_API_ENDPOINT}/{city['id']}",
                json=new_data)