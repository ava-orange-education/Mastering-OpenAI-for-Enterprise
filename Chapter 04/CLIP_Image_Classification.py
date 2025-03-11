import torch
import clip
from PIL import Image
import requests
from io import BytesIO

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

def classify_image(image_url, categories):
    # Download and preprocess the image
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    image_input = preprocess(image).unsqueeze(0).to(device)

    # Prepare text inputs
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {c}") for c in categories]).to(device)

    # Generate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Calculate similarities
    similarities = (100.0 * image_features @ text_features.T).softmax(dim=-1)

    # Return results
    return list(zip(categories, similarities[0].tolist()))

# Example usage
image_url = "https://example.com/path/to/image.jpg"
categories = ["dog", "cat", "bird", "fish", "rabbit"]

results = classify_image(image_url, categories)

print("Classification Results:")
for category, score in sorted(results, key=lambda x: x[1], reverse=True):
    print(f"{category}: {score:.2%}")
