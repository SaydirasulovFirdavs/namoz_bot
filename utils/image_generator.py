from PIL import Image, ImageDraw, ImageFont
import os

def generate_ramadan_calendar(city, data):
    # HD Dimensions for vertical scrolling readability
    # Width 1200, Height 2400 for crystal clear text on any device
    width, height = 1200, 2400
    
    # Premium Deep Emerald Background
    base_color = (2, 44, 34)
    image = Image.new('RGB', (width, height), color=base_color)
    draw = ImageDraw.Draw(image)
    
    # Subtle gradient for premium feel
    for i in range(height):
        alpha = i / height
        r = int(base_color[0] + alpha * 10)
        g = int(base_color[1] + alpha * 15)
        b = int(base_color[2] + alpha * 10)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    # Load high-quality font (Arial or similar standard)
    # Using much larger sizes for elderly users
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 95)
        region_font = ImageFont.truetype("arialbd.ttf", 60)
        header_font = ImageFont.truetype("arialbd.ttf", 45)
        table_font = ImageFont.truetype("arialbd.ttf", 42)
        footer_font = ImageFont.truetype("arial.ttf", 35)
    except:
        title_font = ImageFont.load_default()
        region_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        table_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    # 1. Header Area
    draw.text((width/2, 100), "RAMAZON TAQVIMI - 2026", fill=(251, 191, 36), font=title_font, anchor="mm")
    draw.text((width/2, 185), f"HUDUD: {city.upper()}", fill=(255, 255, 255), font=region_font, anchor="mm")
    
    # Decorative line
    draw.line([(width/2 - 400, 230), (width/2 + 400, 230)], fill=(251, 191, 36), width=6)

    # 2. Table Headers (Vertical single list for maximum text size)
    start_y = 280
    row_height = 62 # Increased for breathing space
    
    # Header Background
    draw.rounded_rectangle([60, start_y, width-60, start_y + 85], radius=20, fill=(6, 78, 59))
    
    headers = ["KUN", "SANA", "SAHAR", "IFTOR"]
    # Adjust spacing for 4 columns
    cols = [150, 420, 720, 1020]
    
    for i, h in enumerate(headers):
        draw.text((cols[i], start_y + 42), h, fill=(251, 191, 36), font=header_font, anchor="mm")

    # 3. Draw Data Rows
    y = start_y + 110
    
    for i, day in enumerate(data):
        # Alternating row background for easier trackability
        if i % 2 == 0:
            draw.rounded_rectangle([70, y - 5, width - 70, y + row_height - 5], radius=12, fill=(13, 84, 68))
        
        # Column 1: Kun (Day)
        draw.text((cols[0], y + row_height/2 - 5), str(day['day']), fill=(255, 255, 255), font=table_font, anchor="mm")
        
        # Column 2: Sana (Date) - e.g. "2-mart"
        draw.text((cols[1], y + row_height/2 - 5), day['date'], fill=(255, 255, 255), font=table_font, anchor="mm")
        
        # Column 3: Sahar (Suhoor)
        draw.text((cols[2], y + row_height/2 - 5), day['sahar'], fill=(255, 255, 255), font=table_font, anchor="mm")
        
        # Column 4: Iftor (Iftar) - Highlighted in Gold
        draw.text((cols[3], y + row_height/2 - 5), day['iftor'], fill=(251, 191, 36), font=table_font, anchor="mm")
        
        y += row_height

    # 4. Footer with credits
    footer_text = "Namoz.bot rasmiy taqvimi | @namoz_bot\nO'zbekiston Musulmonlari idorasi ma'lumotlari asosida"
    draw.multiline_text((width/2, height - 100), footer_text, fill=(167, 139, 250), font=footer_font, anchor="mm", align="center")

    # Save logic
    os.makedirs("data", exist_ok=True)
    output_path = f"data/ramadan_hd_{city.lower()}.png"
    image.save(output_path, quality=95) # High quality save
    return output_path
