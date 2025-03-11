import openai
openai.api_key = 'your-api-key'
article = "Apple has announced a new line of MacBooks with groundbreaking performance improvements."
prompt=f"Categorize \n{article}\nCategory (Business, Technology, Health, Sports, Education, Or Other)"
conversation =[{"role": "system", "content": "You are an Expert."},
                   {"role": "user",
                    "content": prompt
                   }]   

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
)
print(response.choices[0].message.content)
