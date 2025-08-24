from agents import Agent
from gemini_config import MODEL, API_KEY
from guardrial_agents import guardrial_agent
from dynamic_instruction_builder import build_dynamic_hotel_instruction
from hotel_utils import extract_hotel_name

def handle_user_query(user_input, context=None):
    hotel_name = None
    hotel_data = None

    if context and "hotel_data" in context:
        hotel_info = context["hotel_data"]
        hotel_name = hotel_info.get("name")
        hotel_data = hotel_info.get("data")

    if not hotel_name:
        hotel_name = extract_hotel_name(user_input)

    instructions = build_dynamic_hotel_instruction(hotel_name, hotel_data)

    hotel_agent = Agent(
        name="Hotel Customer Care",
        instructions=instructions,
        model=MODEL,
        input_guardrails=[guardrial_agent],
        output_guardrails=[]
    )

    response = hotel_agent.run(user_input, context=context)
    return response
