from dataclasses import dataclass
from datetime import datetime


@dataclass
class FlightRequestDTO:
    destination: str
    departure_date: datetime
    return_date: datetime
