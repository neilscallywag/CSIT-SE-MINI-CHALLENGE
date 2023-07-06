from dataclasses import dataclass
from datetime import datetime


@dataclass
class HotelResponseDTO:
    checkInDate: datetime
    checkOutDate: datetime
    city: str
    hotel: str
    price: str

    def to_dict(self):
        return {
            "City": self.city,
            "Check In Date": self.checkInDate.strftime("%Y-%m-%d"),
            "Check Out Date": self.checkOutDate.strftime("%Y-%m-%d"),
            "Hotel": self.hotel,
            "Price": self.price,
        }
