import openai
from openai import OpenAI

openai.api_key = 'your-api-key'

def summarize_text(text_snippet):
    prompt=f"Summarize the following article into a concise paragraph:\n\n{text_snippet}"
    conversation =[{"role": "system", "content": "You are an Editor."},
                    {"role": "user",
                        "content": prompt
                    }]   

    response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=conversation
    )
    print(response.choices[0].message.content)
