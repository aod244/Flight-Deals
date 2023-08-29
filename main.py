from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_data()

if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])

    data_manager.destination_data = sheet_data
    data_manager.update_data()

for city in sheet_data:
    current_city = FlightData(city["iataCode"])
    flight_search = FlightSearch()
    notification = NotificationManager()
    city_data = current_city.set_data_for_city()
    flight = flight_search.flight_search(city_data, city['city'])
    print(flight)
    if flight is not False:
        if flight['price'] < city['lowestPrice']:
            notification.send_sms(flight)
