from dataclasses import dataclass
from datetime import datetime


@dataclass
class HotelRequestDTO:
    checkInDate: datetime
    checkOutDate: datetime
    destination: str
