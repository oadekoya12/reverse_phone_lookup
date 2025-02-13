import os
import logging
from fastapi import FastAPI, HTTPException
import numlookupapi

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Get API key from environment
NUMAPI_KEY = os.getenv("NUMAPI_KEY")
if not NUMAPI_KEY:
    raise RuntimeError("NUMAPI_KEY is not set in the environment")

client = numlookupapi.Client(NUMAPI_KEY)

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

@app.get("/lookup/{phone_number}")
def lookup_phone(phone_number: str, country_code: str = "US"):
    try:
        logger.info(f"Processing lookup for: {phone_number} (Country: {country_code})")
        result = client.validate(phone_number, country_code=country_code)

        if not result.get("valid"):
            logger.warning(f"Invalid phone number: {phone_number}")
            return {"valid": False, "message": "Invalid phone number"}

        logger.info(f"Lookup successful: {result}")
        return result

    except Exception as e:
        logger.error(f"Lookup failed: {str(e)}")
        raise HTTPException(status_code=502, detail=f"Lookup failed: {str(e)}")
