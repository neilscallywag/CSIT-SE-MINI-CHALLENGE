from typing import Optional, List
from collections import defaultdict
from datetime import datetime
from pymongo import ASCENDING

from domain.dto.HotelRequestDTO import HotelRequestDTO
from domain.dto.HotelResponseDTO import HotelResponseDTO
from infrastructure.Database import DatabaseConnection


class HotelRepository:
    def __init__(self, database: DatabaseConnection, collection_name: str):
        self.database = database
        self.collection = self.database.db[collection_name]

    def get_hotels(self, hotel_request: HotelRequestDTO) -> List[HotelResponseDTO]:
        checkInDate = datetime.strptime(hotel_request.checkInDate, "%Y-%m-%d")
        checkOutDate = datetime.strptime(hotel_request.checkOutDate, "%Y-%m-%d")

        hotels = list(
            self.collection.find(
                {
                    "city": hotel_request.destination.title(),
                    "date": {"$gte": checkInDate, "$lte": checkOutDate},
                }
            )
        )

        # Aggregate prices for each hotel
        hotel_prices = defaultdict(int)
        for hotel in hotels:
            hotel_prices[hotel["hotelName"]] += hotel["price"]

        # Sort hotels by total price
        sorted_hotels = sorted(hotel_prices.items(), key=lambda x: x[1])

        if not sorted_hotels:  # Return empty list if there are no hotels
            return []

        hotel_dto_list = []
        min_price = sorted_hotels[0][1]  # Store the minimum price

        for hotel_name, total_price in sorted_hotels:
            if (
                total_price != min_price
            ):  # Stop adding hotels when the price exceeds the minimum
                break
            hotel_dto = HotelResponseDTO(
                city=hotel_request.destination.title(),
                checkInDate=checkInDate.date(),
                checkOutDate=checkOutDate.date(),
                hotel=hotel_name,
                price=total_price,
            )
            hotel_dto_list.append(hotel_dto)

        return hotel_dto_list
