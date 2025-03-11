from generate_content import generate_content

import openai
def generate_code(prompt):    
    conversation =[{"role": "system", "content": "You are a software developer."},
                   {"role": "user",
                    "content": prompt
                   }]      
    return generate_content(conversation)
# Example usage
prompt = "Write a Python function to sort a list of dictionaries by a specific key"
generated_code = generate_code(prompt)

def analyze_code(code_snippet):    
    prompt=f"Analyze the following code for potential issues:\n\n{code_snippet}"
    conversation =[{"role": "system", "content": "You are an experienced software developer reviewing code."},
                   {"role": "user",
                    "content": prompt
                   }] 
    return generate_content(conversation)  

def it_support_chatbot(user_query):   
    prompt=f"Troubleshoot the following incident:\n\n{user_query}"
    conversation =[{"role": "system", "content": "You are an IT Support person."},
                   {"role": "user",
                    "content": prompt
                   }]   
    return generate_content(conversation)


