from typing import Optional, List
from datetime import datetime
from pymongo import ASCENDING

from domain.dto.FlightResponseDTO import FlightResponseDTO
from domain.dto.FlightRequestDTO import FlightRequestDTO
from infrastructure.Database import DatabaseConnection


class FlightRouteRepository:
    def __init__(self, database: DatabaseConnection, collection_name: str):
        self.database = database
        self.collection = self.database.db[collection_name]

    def get_flights(self, flight_request: FlightRequestDTO) -> List[FlightResponseDTO]:
        departure_date = datetime.strptime(flight_request.departure_date, "%Y-%m-%d")
        return_date = datetime.strptime(flight_request.return_date, "%Y-%m-%d")

        # Find the cheapest flight from Singapore to the destination on the departure date
        out_flights = list(
            self.collection.find(
                {
                    "srccity": "Singapore",
                    "destcity": flight_request.destination,
                    "date": departure_date,
                },
                sort=[("price", ASCENDING)],
            )
        )

        # Find the cheapest flight from the destination back to Singapore on the return date
        in_flights = list(
            self.collection.find(
                {
                    "srccity": flight_request.destination,
                    "destcity": "Singapore",
                    "date": return_date,
                },
                sort=[("price", ASCENDING)],
            )
        )

        if not out_flights or not in_flights:
            return []

        flight_dto_list = []
        min_out_flight_price = out_flights[0]["price"]
        min_in_flight_price = in_flights[0]["price"]

        out_flights = [f for f in out_flights if f["price"] == min_out_flight_price]
        in_flights = [f for f in in_flights if f["price"] == min_in_flight_price]

        for out_flight in out_flights:
            for in_flight in in_flights:
                flight_dto = FlightResponseDTO(
                    city=flight_request.destination,
                    departure_date=departure_date.date(),
                    departure_airline=out_flight["airlinename"],
                    departure_price=out_flight["price"],
                    return_date=return_date.date(),
                    return_airline=in_flight["airlinename"],
                    return_price=in_flight["price"],
                )
                flight_dto_list.append(flight_dto)

        return flight_dto_list
