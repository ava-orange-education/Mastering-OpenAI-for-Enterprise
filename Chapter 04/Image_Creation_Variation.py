from typing import *
import sys
import openai
import requests # type: ignore
from openai import OpenAI
from PIL import Image, ImageDraw

# Set your OpenAI API key
openai.api_key = 'your-api-key-here'

def generate_image(prompt, n=1, size="1024x1024"):
    model = "dall-e-3"
    try:        
        response = openai.images.generate(prompt=prompt, model=model) 
        imageurl = response.data[0].url                
        return imageurl
    
    except Exception as e:
        print(f"An error occurred while creating image: {e}")        

def edit_image(image_path, mask_path, prompt, n=1, size="1024x1024"):
    
    try:
        response = openai.images.edit(
            model = "dall-e-2",
            image=open(image_path, "rb"),
            mask=open(mask_path, "rb"),
            prompt=prompt,            
            n=n,
            size=size
        )        
        image_url = response.data[0].url       
        return image_url    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def create_image_variation(image_path, n=1, size="1024x1024"):
    try:
        response = openai.images.create_variation(
            model="dall-e-2",
            image=open(image_path, "rb"),
            n=n,
            size=size
        )
        
        image_url = response.data[0].url               
        return image_url    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def download_image(image_url, save_path):
    """Download an image from a URL and save it to a local file."""
    
    # Send an HTTP GET request to the URL
    response = requests.get(image_url, stream=True)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Open a local file with write-binary mode
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)  # Write the content of the request to the file in chunks
        print("Image downloaded successfully.")
    else:
        print(f"Failed to download the image. HTTP Status Code: response.status_code")