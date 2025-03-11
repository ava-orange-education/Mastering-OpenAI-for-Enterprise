import openai
from openai import OpenAI
openai.api_key = 'your-api-key'

def conversational_assistant(messages):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("VA: Hello! I'm your virtual assistant. Ask me anything.")
    conversation = [{"role": "system", "content": "You are a knowledgeable helpful assistant."}]
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in {"exit", "quit"}:
            print("VA: Goodbye!")
            break
        # Add user message to the conversation history
        conversation.append({"role": "user", "content": user_input})
        
        # Get the VA's response
        bot_response = conversational_assistant(conversation)
        # Add the VA response to the conversation history
        conversation.append({"role": "assistant", "content": bot_response})
        print(f"VA: {bot_response}")
