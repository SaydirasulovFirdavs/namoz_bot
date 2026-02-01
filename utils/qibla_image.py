from PIL import Image, ImageDraw, ImageFont
import math
import os

def generate_qibla_compass(angle):
    # Create background (transparent)
    size = 500
    image = Image.new('RGBA', (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    
    center = size // 2
    radius = 200
    
    # Draw Compass Circle
    draw.ellipse([center - radius, center - radius, center + radius, center + radius], outline=(255, 255, 255), width=5)
    
    # Draw Cardinal Points (N, S, E, W)
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except:
        font = ImageFont.load_default()
        
    draw.text((center, center - radius - 30), "N", fill=(255, 255, 255), font=font, anchor="mm") # North
    draw.text((center, center + radius + 30), "S", fill=(255, 255, 255), font=font, anchor="mm") # South
    draw.text((center + radius + 30, center), "E", fill=(255, 255, 255), font=font, anchor="mm") # East
    draw.text((center - radius - 30, center), "W", fill=(255, 255, 255), font=font, anchor="mm") # West
    
    # Draw Qibla Arrow
    # Angle in degrees, 0 is North, clockwise.
    # We need to convert to radians and adjust for PIL coordinate system (0 is East)
    rad = math.radians(angle - 90)
    
    arrow_len = radius - 20
    end_x = center + arrow_len * math.cos(rad)
    end_y = center + arrow_len * math.sin(rad)
    
    # Draw the main arrow line
    draw.line([center, center, end_x, end_y], fill=(234, 179, 8), width=8) # Golden color
    
    # Draw Arrow Head (Kaaba simple icon or just a triangle)
    head_size = 20
    # Triangle points
    p1 = (end_x, end_y)
    p2 = (end_x - head_size * math.cos(rad - 0.5), end_y - head_size * math.sin(rad - 0.5))
    p3 = (end_x - head_size * math.cos(rad + 0.5), end_y - head_size * math.sin(rad + 0.5))
    draw.polygon([p1, p2, p3], fill=(234, 179, 8))
    
    # Draw a small Kaaba box at the tip or just a dot
    draw.rectangle([end_x-10, end_y-10, end_x+10, end_y+10], fill=(0, 0, 0), outline=(234, 179, 8))

    # Add background layer for contrast
    bg = Image.new('RGB', (size, size), (15, 23, 42))
    bg.paste(image, (0, 0), image)
    
    output_path = "data/qibla_direction.png"
    if not os.path.exists("data"):
        os.makedirs("data")
    bg.save(output_path)
    return output_path
