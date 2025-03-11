import openai

openai.api_key = 'your-api-key'
def chat_with_gpt(conversation):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Chatbot: Goodbye!")
            break

        conversation.append({"role": "user", "content": user_input})
        
        response = chat_with_gpt(conversation)
        
        if "Error" in response:
            response = "I'm sorry, I encountered an issue. Please try again."
        
        print(f"Chatbot: {response}")

        if len(conversation) > 10:
            conversation.pop(1)  # Maintain context size
