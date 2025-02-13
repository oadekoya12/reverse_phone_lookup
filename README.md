# FastAPI Phone Number Lookup

This project is a FastAPI-based service that performs reverse phone number lookups using the NumLookup API.

## Features
- FastAPI framework for efficient API handling
- Integration with NumLookup API for phone number validation
- Dockerized deployment with environment variable support
- Structured logging and improved error handling

## Prerequisites
- Docker
- Docker Compose
- A NumLookup API key

## Setup & Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/phone_lookup.git
   cd phone_lookup
   ```
2. Set up the API key in your environment:
   ```sh
   export NUMAPI_KEY="your_numlookup_api_key"
   ```
3. Build and start the service:
   ```sh
   ./script.sh
   ```

## API Endpoints

### Health Check
```http
GET /
```
_Response:_
```json
{
  "message": "Hello, world!"
}
```

### Lookup Phone Number
```http
GET /lookup/{phone_number}?country_code=US
```
_Example:_
```sh
curl http://localhost:9606/lookup/XXXXXXXXX?country_code=US
```
_Response:_
```json
{
  "valid": true,
  "number": "1XXXXXXXXX",
  "local_format": "XXXXXXXXX",
  "international_format": "+1XXXXXXXXX",
  "country_prefix": "+1",
  "country_code": "US",
  "country_name": "United States of America",
  "location": "Wshngtnzn3",
  "carrier": "T-Mobile USA Inc.",
  "line_type": "mobile"
}
```

## Running in Docker

To run the service inside a Docker container:
```sh
docker-compose up -d --build
```
To check logs:
```sh
docker logs fastapi_app
```

## Stopping the Service
```sh
docker-compose down
```

## License
[Link to the file.](LICENSE)
