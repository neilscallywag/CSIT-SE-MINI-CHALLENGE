# Table of Contents

- [Table of Contents](#table-of-contents)
- [CSIT SE Mini-Challenge: Python backend](#csit-se-mini-challenge-python-backend)
  - [Endpoints](#endpoints)
    - [Request payload:](#request-payload)
    - [Response payload:](#response-payload)
      - [`200 OK`](#200-ok)
      - [`400 Bad Request`](#400-bad-request)
    - [Request payload:](#request-payload-1)
    - [Response payload:](#response-payload-1)
      - [`200 OK`](#200-ok-1)
      - [`400 Bad Request`](#400-bad-request-1)

# CSIT SE Mini-Challenge: Python backend

This is the python version for the backend submitted for CSIT SE challenge 2023. Other verions can be found [here](https://github.com/neilscallywag/CSIT-SE-MINI-CHALLENGE). They will be made public after the submission deadline.

`.env` file is not added into the `.dockerignore` file and is included in this image for ease of use. 

## Endpoints

1. ### `GET` **/flight**

   Description: Get a list of return flights at the cheapest price, given the destination city, departure date, and arrival date.

   ### Request payload:

   ```
   {
       "departureDate":"<departuredate>",
       "returnDate":"<returndate>",
       "destination":"<destination>",
   }
   ```

   ### Response payload:

   #### `200 OK`

   ```
   [
   {
    "City": "Frankfurt",
    "Departure Date": "2023-12-10",
    "Departure Airline": "US Airways",
    "Departure Price": 1766,
    "Return Date": "2023-12-16",
    "Return Airline": "US Airways",
    "Return Price": 716
   }
   ]
   ```

   #### `400 Bad Request`

   ```
   {
    "error":"All parameters (departureDate, returnDate, destination) must be provided"
    }
   ```

2. ### `GET` **/hotel**

   Description: Get a list of hotels providing the cheapest price, given the destination city, check-in date, and check-out date.

   ### Request payload:

   ```
   {
       "checkInDate": "<checkInDate>",
       "checkOutDate": "<checkOutDate>",
       "destination": "<destination>"
   }
   ```

   ### Response payload:

   #### `200 OK`

   ```
   [
   {
    "City": "Frankfurt",
    "Check In Date": "2023-12-10",
    "Check Out Date": "2023-12-16",
    "Hotel": "Hotel J",
    "Price": 2959
   }
   ]
   ```

   #### `400 Bad Request`

   ```
   {"error":"All parameters (checkInDate, checkOutDate, destination) must be provided"}
   ```
