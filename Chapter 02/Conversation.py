import openai
openai.api_key = 'your-api-key'
user_message = "What is the weather in Seattle today?"
print("Chatbot: Hello! How can I assist you today?")
response = openai.chat.completions.create(
        model=" gpt-4o-min i",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
)    
print(response.choices[0].message.content)
