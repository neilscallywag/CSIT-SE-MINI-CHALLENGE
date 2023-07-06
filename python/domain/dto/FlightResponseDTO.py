from dataclasses import dataclass
from datetime import datetime


@dataclass
class FlightResponseDTO:
    city: str
    departure_date: datetime
    departure_airline: str
    departure_price: int
    return_date: datetime
    return_airline: str
    return_price: int

    def to_dict(self):
        return {
            "City": self.city,
            "Departure Date": self.departure_date.strftime("%Y-%m-%d"),
            "Departure Airline": self.departure_airline,
            "Departure Price": self.departure_price,
            "Return Date": self.return_date.strftime("%Y-%m-%d"),
            "Return Airline": self.return_airline,
            "Return Price": self.return_price,
        }
