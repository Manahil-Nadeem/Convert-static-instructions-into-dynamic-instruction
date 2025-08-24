import re

HOTELS = ["sannata", "moonlight"]

def extract_hotel_name(user_input):
    user_input = user_input.lower()
    for hotel in HOTELS:
        pattern = rf"(hotel\s+)?{hotel}|{hotel}\s+hotel"
        if re.search(pattern, user_input):
            return f"hotel {hotel}"
    return None
