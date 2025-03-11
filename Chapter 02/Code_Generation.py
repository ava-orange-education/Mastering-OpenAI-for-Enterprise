import openai
openai.api_key = 'your-api-key'
prompt = f"Write a Python function to sort a list of dictionaries by a specific key."
conversation =[{"role": "system", "content": "You are a Software Developer."},
                   {"role": "user",
                    "content": prompt
                   }]   

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
)
print(response.choices[0].message.content)
