from hotel_assistant import handle_user_query

if __name__ == "__main__":
    print("Hotel Assistant Chat (type 'exit' to quit)")
    context = None
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = handle_user_query(user_input, context=context)
        
        print("Agent:", response)
