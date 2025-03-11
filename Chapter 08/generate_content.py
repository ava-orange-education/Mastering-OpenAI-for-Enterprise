import openai
openai.api_key = 'YOUR_API_KEY'

def generate_content(conversation):
    model = "gpt-4o"
    try:
        response = openai.chat.completions.create(
            model = model,
            messages = conversation
        )            
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
    return None

def generate_blog_post(title, keywords, tone):
    prompt = f"Write a blog post titled '{title}'. Use the following keywords: {', '.join(keywords)}. The tone should be {tone}."
    conversation =[{"role": "system", "content": "You are a content specialist."},
                   {"role": "user",
                    "content": prompt
                   }]   
   
    return generate_content(conversation)

