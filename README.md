# CSIT-SE-MINI-CHALLENGE
This is my submission for the 2023 CSIT Software Engineering Mini challenge. Each folder contains its own README as a guide. 
The Python folder was used as the submission. 
# Table Of Contents
- [CSIT-SE-MINI-CHALLENGE](#csit-se-mini-challenge)
- [Table Of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installations](#installations)
      - [Installing Make on Ubuntu](#installing-make-on-ubuntu)
        - [1. Update apt Database](#1-update-apt-database)
        - [2. Install Make](#2-install-make)
        - [3. Test Make installation](#3-test-make-installation)
      - [Installing Make on Windows](#installing-make-on-windows)
        - [1. Run Powershell as an administrator](#1-run-powershell-as-an-administrator)
        - [2. Check output of `Get-ExecutionPolicy`](#2-check-output-of-get-executionpolicy)
        - [3. Install `chocolatey`](#3-install-chocolatey)
        - [4. Install `Make`](#4-install-make)
        - [5. Test Make installation](#5-test-make-installation)
        - [6. Reset Execution Policy](#6-reset-execution-policy)
    - [Deployment Guide](#deployment-guide)
      - [1. Fill in the necessary credentials](#1-fill-in-the-necessary-credentials)
      - [2. Build Images](#2-build-images)
      - [3. Deploy Containers](#3-deploy-containers)
      - [4. Tearing Down Deployment](#4-tearing-down-deployment)
  - [Endpoints](#endpoints)
    - [Request payload:](#request-payload)
    - [Response payload:](#response-payload)
      - [`200 OK`](#200-ok)
      - [`400 Bad Request`](#400-bad-request)
    - [Request payload:](#request-payload-1)
    - [Response payload:](#response-payload-1)
      - [`200 OK`](#200-ok-1)
      - [`400 Bad Request`](#400-bad-request-1)


## Getting Started

To run the the REST API on your local machine, follow these steps:

### Prerequisites
1. [Docker](https://docs.docker.com/engine/install/)
2. [Docker Compose](https://docs.docker.com.zh.xy2401.com/v17.12/compose/install/)
3. [Make](https://www.gnu.org/software/make/manual/make.html)

### Installations
1. [For Ubuntu](#installing-make-on-ubuntu)
2. [For Windows](#installing-make-on-windows)

#### Installing Make on Ubuntu
##### 1. Update apt Database
```
$ sudo apt update
```

##### 2. Install Make
```
$ sudo apt -y install make
```

##### 3. Test Make installation
```
$ make -version
```

#### Installing Make on Windows
`Make` is a little bit of a hassle to install on Windows, but is definitely worth it.

##### 1. Run Powershell as an administrator
Windows Search > Windows Powershell > Right Click > Run as Administrator

##### 2. Check output of `Get-ExecutionPolicy`
If `Get-ExecutionPolicy` returns `Restricted`, run the following command.
```
$ Set-ExecutionPolicy AllSigned
```
If it is already unrestricted, then you can skip this step.

##### 3. Install `chocolatey`
```
$ Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

##### 4. Install `Make`
```
$ choco install make
```

##### 5. Test Make installation
```
$ make -version
```

##### 6. Reset Execution Policy
```
$ Set-ExecutionPolicy Restricted
```

### Deployment Guide
Ensure that the above steps have been done before proceeding with deployment.
#### 1. Fill in the necessary credentials
Fill in the necessary credentials in the `.env` and `{language}\.env` file. The main .env file contains env variables used in the docker compose while the in directory .env contains env variables for the backend  container. 

#### 2. Build Images
```
$ make build
```

#### 3. Deploy Containers
```
$ make up
```

#### 4. Tearing Down Deployment
```
$ make down
```

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
