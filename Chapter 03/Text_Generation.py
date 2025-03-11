import openai
openai.api_key = 'your-api-key'
story_line = "Once upon a time in a magical forest, there lived a small rabbit named Theo."
prompt=f"Generate a short story based on the prompt below:\n\n{story_line}"
conversation =[{"role": "system", "content": "You are a Writer."},
                   {"role": "user",
                    "content": prompt
                   }]   

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
)
print("Generated Story\n")
print(response.choices[0].message.content)
