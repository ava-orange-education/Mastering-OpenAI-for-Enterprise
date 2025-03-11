from Interacting_With_ChatGPT_Basic import chat_with_gpt

def handle_conversation(conversation, user_input, state):
    if state == "awaiting_name":
        response = f"Nice to meet you, {user_input}! How can I help you?"
        state = "default"
    elif state == "awaiting_feedback":
        response = f"Thank you for your feedback: {user_input}"
        state = "default"
    else:
        conversation.append({"role": "user", "content": user_input})
        response = chat_with_gpt(conversation)
    return response, state

if __name__ == "__main__":
    print("Chatbot: Welcome! What is your name?")
    state = "awaiting_name"
    
    conversation = [{"role": "system", "content": "You are a friendly assistant."}]    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Chatbot: Goodbye!")
            break

        response, state = handle_conversation(conversation, user_input, state)
        print(f"Chatbot: {response}")
        
        if len(conversation) > 10:
            conversation.pop(1)
