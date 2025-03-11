import openai
from openai import OpenAI
openai.api_key = 'your-api-key'

def translate_french_to_english(french_text):
    prompt=f"Translate the following French text to English:  \n{french_text}"
    conversation =[{"role": "system", "content": "You are a Language Specialist."},
                    {"role": "user",
                        "content": prompt
                    }]   
    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
    )
    return response.choices[0].message.content
