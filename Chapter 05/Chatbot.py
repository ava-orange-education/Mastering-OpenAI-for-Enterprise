import openai
# Replace 'your-api-key' with your OpenAI API key
openai.api_key = 'your-api-key'

def chat_with_gpt(messages):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Chatbot: Hello! I'm your assistant. Ask me anything.")
    conversation = [{"role": "system", "content": "You are a helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("Chatbot: Goodbye!")
            break
        # Add user message to the conversation history
        conversation.append({"role": "user", "content": user_input})
        
        # Get the chatbot's response
        bot_response = chat_with_gpt(conversation)
        # Add the chatbot response to the conversation history
        conversation.append({"role": "assistant", "content": bot_response})
        print(f"Chatbot: {bot_response}")
