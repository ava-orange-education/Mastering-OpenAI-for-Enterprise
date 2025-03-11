import openai
openai.api_key = 'your-api-key'
prompt = "Generate an image to visualize a crispy fall evening in Seattle"
model = "dall-e-3"
response = openai.images.generate(prompt=prompt, model=model) 
imageurl = response.data[0].url          
print(imageurl)
