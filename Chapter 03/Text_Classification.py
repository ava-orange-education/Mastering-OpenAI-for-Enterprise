import openai
openai.api_key = 'your-api-key'
product_review = "The product met my expectations."
prompt=f"Review \n{product_review}\n Sentiment (Postive, Negative, or Neutral)"
conversation =[{"role": "system", "content": "You are a Product Reviewer."},
                   {"role": "user",
                    "content": prompt
                   }]   

response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=conversation
)
print(response.choices[0].message.content)
