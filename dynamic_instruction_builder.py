def build_dynamic_hotel_instruction(hotel_name=None, hotel_data=None):
    base_instruction = (
        "You are a hotel assistant that can handle bookings, answer questions, "
        "and update information for multiple hotels."
    )
    if hotel_name and hotel_data:
        hotel_info = f"Current info about {hotel_name}: {hotel_data}"
        dynamic_part = (
            f" Use this context when responding: {hotel_info}. "
            "Provide accurate and helpful answers based on the latest data."
        )
        return base_instruction + dynamic_part
    else:
        return base_instruction + " Ask the user which hotel they are referring to if it's unclear."
