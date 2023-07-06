from flask import Blueprint, request, jsonify

from domain.dto.FlightRequestDTO import FlightRequestDTO
from domain.dto.HotelRequestDTO import HotelRequestDTO


def create_csit_blueprint(blueprint_name, flight_repository, hotel_repository):
    bp = Blueprint(blueprint_name, __name__)

    @bp.route("/flight", methods=["GET"])
    def get_flights():
        departure_date = request.args.get("departureDate")
        return_date = request.args.get("returnDate")
        destination = request.args.get("destination")

        if not departure_date or not return_date or not destination:
            return (
                jsonify(
                    {
                        "error": "All parameters (departureDate, returnDate, destination) must be provided"
                    }
                ),
                400,
            )

        flight_request = FlightRequestDTO(
            departure_date=departure_date,
            return_date=return_date,
            destination=destination,
        )
        try:
            flights = flight_repository.get_flights(flight_request)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        if flights:
            return jsonify([flight.to_dict() for flight in flights])
        else:
            return jsonify([]), 200

    @bp.route("/hotel", methods=["GET"]) 
    def get_hotels():
        checkInDate = request.args.get("checkInDate")
        checkOutDate = request.args.get("checkOutDate")
        destination = request.args.get("destination")

        if not checkInDate or not checkOutDate or not destination:
            return (
                jsonify(
                    {
                        "error": "All parameters (checkInDate, checkOutDate, destination) must be provided"
                    }
                ),
                400,
            )

        hotel_request = HotelRequestDTO(
            checkInDate=checkInDate, checkOutDate=checkOutDate, destination=destination
        )
        try:
            hotels = hotel_repository.get_hotels(hotel_request)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400

        if hotels:
            for hotel in hotels:
                print(hotel.to_dict())
            return jsonify([hotel.to_dict() for hotel in hotels])
        else:
            return jsonify([]), 200

    return bp
