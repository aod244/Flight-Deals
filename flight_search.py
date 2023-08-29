import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "Tequila api key"
HEADERS = {"apikey": TEQUILA_API_KEY}


class FlightSearch:

    def __init__(self):
        self.query = ""
        self.data = ""

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=HEADERS, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def flight_search(self, flight_data, current_city):
        search_endpoint = f"{TEQUILA_ENDPOINT}/v2/search"
        self.query = flight_data
        response = requests.get(url=search_endpoint, headers=HEADERS, params=self.query)
        self.data = response.json()
        try:
            city = self.data['data'][0]['cityTo']
            price = self.data['data'][0]['price']
            print(f"{city}: {price} £")
            return self.data['data'][0]
        except IndexError:
            print(f"No flights found to {current_city}")
            return False
