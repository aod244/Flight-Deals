from datetime import datetime, timedelta

FLY_FROM = "WAW"


class FlightData:

    def __init__(self, iataCode):
        self.data = ""
        self.iataCode = iataCode
        self.current_date = datetime.now()
        self.tomorrow = self.current_date + timedelta(days=1)
        self.six_months_span = self.tomorrow + timedelta(days=180)

    def set_data_for_city(self):
        self.data = {
            "fly_from": FLY_FROM,
            "fly_to": self.iataCode,
            "date_from": self.tomorrow.strftime("%d/%m/%Y"),
            "date_to": self.six_months_span.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "curr": "GBP",
            "max_stopovers": 0,
            "limit": "5"
        }
        return self.data
