from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os

def generate_ramadan_calendar(city, data):
    # Dimensions for high-quality image
    width, height = 1000, 1600
    
    # Premium Background: Deep Midnight Blue Gradient
    image = Image.new('RGB', (width, height), color=(15, 23, 42))
    draw = ImageDraw.Draw(image)
    
    # Add subtle decorative background elements (Gradient effect)
    for i in range(height):
        r = int(15 + (i / height) * 15)
        g = int(23 + (i / height) * 15)
        b = int(42 + (i / height) * 15)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    # Fonts
    try:
        title_font = ImageFont.truetype("arialbd.ttf", 65)
        header_font = ImageFont.truetype("arialbd.ttf", 35)
        table_font = ImageFont.truetype("arial.ttf", 30)
        footer_font = ImageFont.truetype("arial.ttf", 25)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        table_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    # Draw Title Area with Gold Accents
    # Glow effect for title
    draw.text((width/2, 80), f"RAMAZON TAQVIMI", fill=(234, 179, 8), font=title_font, anchor="mm")
    draw.text((width/2, 160), city.upper(), fill=(255, 255, 255), font=header_font, anchor="mm")
    draw.line([(width/2 - 200, 210), (width/2 + 200, 210)], fill=(234, 179, 8), width=3)

    # Table Header Design
    start_y = 260
    header_bg = (30, 41, 59)
    draw.rounded_rectangle([80, start_y, 920, start_y + 70], radius=15, fill=header_bg)
    
    headers = ["KUN", "SAHARLIK", "IFTORLIK"]
    draw.text((150, start_y + 35), headers[0], fill=(234, 179, 8), font=header_font, anchor="mm")
    draw.text((width/2, start_y + 35), headers[1], fill=(234, 179, 8), font=header_font, anchor="mm")
    draw.text((800, start_y + 35), headers[2], fill=(234, 179, 8), font=header_font, anchor="mm")

    # Draw Data with improved readability
    y = start_y + 90
    row_height = 42
    
    for i, day in enumerate(data):
        # Format times (strip timezone)
        fajr = day['timings']['Fajr'].split(' ')[0]
        maghrib = day['timings']['Maghrib'].split(' ')[0]
        
        # Row background
        if i % 2 == 0:
            draw.rounded_rectangle([70, y - 5, 930, y + row_height - 5], radius=10, fill=(30, 41, 59, 100))
        
        # Text alignment
        draw.text((150, y + row_height/2 - 5), str(i+1), fill=(255, 255, 255), font=table_font, anchor="mm")
        draw.text((width/2, y + row_height/2 - 5), fajr, fill=(255, 255, 255), font=table_font, anchor="mm")
        draw.text((800, y + row_height/2 - 5), maghrib, fill=(255, 255, 255), font=table_font, anchor="mm")
        
        y += row_height
        
        if y > height - 120:
            break

    # Footer
    footer_text = "Namoz.bot tomonidan taqdim etildi | @namoz_bot"
    draw.text((width/2, height - 60), footer_text, fill=(148, 163, 184), font=footer_font, anchor="mm")

    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    output_path = f"data/ramadan_{city}.png"
    image.save(output_path)
    return output_path
