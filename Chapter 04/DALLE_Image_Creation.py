import openai
import requests
from PIL import Image
import io

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

def generate_image(prompt, n=1, size="1024x1024"):
    """
    Generate an image using DALL-E based on the given prompt.
    
    :param prompt: Text description of the image to generate
    :param model: Name of the DALLE model to use: dall-e, dall-e-2, or dall-e 3	 
    :param n: Number of images to generate (default 1)
    :param size: Size of the image (default "1024x1024")
    :return: URL of the generated image(s)
    """
    try:
        response = openai.images.create(
            prompt=prompt,
            n=n,
            size=size
        )        
        image_url = response.data[0].url                
        return image_url
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
