from PIL import Image, ImageDraw, ImageFont
import os

def generate_ramadan_calendar(city, data):
    # Create background
    width, height = 800, 1200
    background_color = (15, 23, 42) # Dark blue/black
    image = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(image)
    
    # Fonts (Try to find a system font or use default)
    try:
        title_font = ImageFont.truetype("arial.ttf", 60)
        header_font = ImageFont.truetype("arial.ttf", 30)
        table_font = ImageFont.truetype("arial.ttf", 24)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        table_font = ImageFont.load_default()

    # Draw Title
    draw.text((width/2, 50), f"Ramazon Taqvimi - 2026", fill=(234, 179, 8), font=title_font, anchor="mm")
    draw.text((width/2, 120), city, fill=(255, 255, 255), font=header_font, anchor="mm")
    
    # Draw Headers
    headers = ["Kun", "Saharlik", "Iftorlik"]
    start_y = 200
    col_widths = [100, 300, 300]
    draw.text((100, start_y), headers[0], fill=(234, 179, 8), font=header_font)
    draw.text((300, start_y), headers[1], fill=(234, 179, 8), font=header_font)
    draw.text((550, start_y), headers[2], fill=(234, 179, 8), font=header_font)
    
    # Draw Data
    y = start_y + 50
    # Limited to first 30 days for display
    for i, day in enumerate(data[:30]):
        hijri_day = day['date']['hijri']['day']
        fajr = day['timings']['Fajr'].split(' ')[0]
        maghrib = day['timings']['Maghrib'].split(' ')[0]
        
        # Zebra striping
        if i % 2 == 0:
            draw.rectangle([50, y-5, 750, y+35], fill=(30, 41, 59))
            
        draw.text((110, y), str(i+1), fill=(255, 255, 255), font=table_font)
        draw.text((310, y), fajr, fill=(255, 255, 255), font=table_font)
        draw.text((560, y), maghrib, fill=(255, 255, 255), font=table_font)
        y += 40
        
        if y > height - 50:
            break

    output_path = f"data/ramadan_{city}.png"
    image.save(output_path)
    return output_path
