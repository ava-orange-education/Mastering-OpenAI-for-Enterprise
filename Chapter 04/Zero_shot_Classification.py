import torch
from PIL import Image
import clip
# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Prepare the image
image = preprocess(Image.open("generated.jpg")).unsqueeze(0).to(device)

# Prepare text descriptions
text_descriptions = "sun", "moon", "trees", "sky"]
text = clip.tokenize(text_descriptions).to(device)

# Generate predictions
with torch.no_grad():
    image_features = model.encode_image(image)
    text_features = model.encode_text(text)
    
    logits_per_image, logits_per_text = model(image, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

# Print results
for i, description in enumerate(text_descriptions):
    print(f"{description}: {probs[0][i]:.2%}")
