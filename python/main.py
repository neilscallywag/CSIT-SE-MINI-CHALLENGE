from flask import Flask, Blueprint, jsonify, request


from utils.config import *
from domain.repository.flight import FlightRouteRepository
from domain.repository.hotel import HotelRepository
from infrastructure.blueprints.csit import create_csit_blueprint
from infrastructure.Database import DatabaseConnection


database_connection = DatabaseConnection(MONGO_URL, DB_NAME)
flight_repository = FlightRouteRepository(database_connection, COLLECTION_FLIGHTS)
hotel_repository = HotelRepository(database_connection, COLLECTION_HOTELS)


app = Flask(__name__)
app.register_blueprint(
    create_csit_blueprint("flights", flight_repository, hotel_repository),
)
# SWAGGER_URL = "/swagger"
# API_URL = "/swagger.json"

# swaggerui_blueprint = get_swaggerui_blueprint(
#     SWAGGER_URL, API_URL, config={"app_name": "Your Flask App"}
# )


# @app.route("/swagger.json")
# def swagger_json():
#     # Replace with your Swagger/OpenAPI specification file path
#     with open("swagger.json", "r") as f:
#         spec_file_content = f.read()
#     return jsonify(spec_file_content)
# app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
