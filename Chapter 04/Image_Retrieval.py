import torch
import clip
from PIL import Image
import os

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Function to encode images
def encode_images(image_paths):
    encoded_images = []
    for img_path in image_paths:
        image = preprocess(Image.open(img_path)).unsqueeze(0).to(device)
        with torch.no_grad():
            image_features = model.encode_image(image)
        encoded_images.append(image_features)
    return torch.cat(encoded_images)

# Encode all images in a directory
image_dir = "path/to/image/directory"
image_paths = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
encoded_images = encode_images(image_paths)

# Function to retrieve images based on text query
def retrieve_images(text_query, encoded_images, image_paths, top_k=5):
    text = clip.tokenize([text_query]).to(device)
    with torch.no_grad():
        text_features = model.encode_text(text)
    
    # Compute similarities
    similarities = (100.0 * encoded_images @ text_features.T).softmax(dim=0)
    
    # Get top-k results
    values, indices = similarities.topk(top_k)
    return [(image_paths[idx], val.item()) for val, idx in zip(values, indices)]
