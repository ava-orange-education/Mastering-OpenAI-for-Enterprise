import openai
import requests

openai.api_key = 'your-api-key'
def get_weather(city):
    # Replace 'your-weather-api-key' with the actual key
    api_url = f"http://api.weatherapi.com/v1/current.json?key=your-weather-api-key&q={city}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        return f"The weather in {city} is {data['current']['temp_c']}°C."
    return "I couldn't retrieve the weather right now."

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
        
        if "weather" in user_input.lower():
            city = user_input.split()[-1]  # Simple city extraction
            weather = get_weather(city)
            print(f"Chatbot: {weather}")
            continue  
        
        conversation.append({"role": "user", "content": user_input})
        response = chat_with_gpt(conversation)
        print(f"Chatbot: {response}")

        if len(conversation) > 10:
            conversation.pop(1)
