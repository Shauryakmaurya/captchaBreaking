import os
import random
import string
from PIL import Image, ImageDraw, ImageFont
import numpy as np

def generate_text(length=None):
    """Generate a random text string with variable capitalization."""
    length = length or random.randint(4, 7)
    text = ''.join(random.choices(string.ascii_letters, k=length))
    return ''.join(c.upper() if random.random() > 0.5 else c.lower() for c in text)

def generate_image(text, font_path, image_size=(150, 60), background='white', noise=False, reverse=False):
    """Generate an image with given text, font, and background properties."""
    image = Image.new('RGB', image_size, background)
    draw = ImageDraw.Draw(image)
    
    try:
        font = ImageFont.truetype(font_path, 40)
    except:
        font = ImageFont.load_default()
    
    text_size = draw.textbbox((0, 0), text, font=font)
    x = (image_size[0] - text_size[2]) // 2
    y = (image_size[1] - text_size[3]) // 2
    
    if reverse:
        text = text[::-1]
    
    draw.text((x, y), text, fill='black', font=font)
    
    if noise:
        for _ in range(300):
            x, y = random.randint(0, image_size[0] - 1), random.randint(0, image_size[1] - 1)
            image.putpixel((x, y), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    
    return image

def save_dataset(set_type, num_samples=100):
    """Generate and save a dataset of images."""
    os.makedirs(set_type, exist_ok=True)
    fonts = ["arial.ttf", "times.ttf", "cour.ttf"]  # Modify with actual font paths
    
    for i in range(num_samples):
        text = generate_text()
        font_path = random.choice(fonts)
        
        if set_type == "Easy":
            img = generate_image(text, font_path)
        elif set_type == "Hard":
            img = generate_image(text, font_path, noise=True)
        elif set_type == "Bonus":
            bg_color = (0, 255, 0) if random.random() > 0.5 else (255, 0, 0)
            img = generate_image(text, font_path, background=bg_color, noise=True, reverse=(bg_color == (255, 0, 0)))
        else:
            continue
        
        file_name = f"{set_type}/{text}.png"
        img.save(file_name)
        print(f"Saved: {file_name}")

# Generate datasets
save_dataset("Easy", 1000)
save_dataset("Hard", 1000)
save_dataset("Bonus", 1000)
