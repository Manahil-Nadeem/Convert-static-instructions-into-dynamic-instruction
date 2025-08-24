from agents import input_guardrail, RunContextWrapper, GuardrailFunctionOutput, Runner
from guardrial_agents import guardrial_agent 
from dynamic_instruction_builder import build_dynamic_hotel_instruction
from hotel_utils import extract_hotel_name

HOTEL_CONTEXT_KEY = "hotel_data"

@input_guardrail
async def guardrial_input_function(ctx: RunContextWrapper, agent, user_input):
    context = ctx.context or {}
    hotel_context = context.get(HOTEL_CONTEXT_KEY, {})
    hotel_name = hotel_context.get("name")
    hotel_data = hotel_context.get("data")

    if not hotel_name:
        hotel_name = extract_hotel_name(user_input)

    instructions = build_dynamic_hotel_instruction(hotel_name, hotel_data)

    result = await Runner.run(
        guardrial_agent,  
        input=user_input,
        context=ctx.context,
        instructions=instructions
    )

    updated_hotel_data = hotel_data  
    new_context = dict(context)
    if hotel_name:
        new_context[HOTEL_CONTEXT_KEY] = {
            "name": hotel_name,
            "data": updated_hotel_data
        }

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=False,
        new_context=new_context
    )
