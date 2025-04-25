import os

# Mushroom types and restaurant assignments
MUSHROOM_TYPES = {
    1: "Blue Oyster",
    2: "Lion's Mane"
}

RESTAURANT_ASSIGNMENTS = {
    1: "Restaurant A",
    2: "Restaurant B",
    3: "Restaurant C"
}

# Mock values for Square API (not needed in mock mode but kept for compatibility)
SQUARE_ACCESS_TOKEN = "mock_token"
SQUARE_LOCATION_ID = "mock_location"
SQUARE_ORDER_ID = "mock_order"
SQUARE_CUSTOMER_ID = "mock_customer"

# Dynamic toggle: Read from environment variable
USE_MOCK_SQUARE = os.getenv("USE_MOCK_SQUARE", "1") == "1"  # Defaults to mock mode
