from PIL import Image, ImageDraw, ImageFont
import os

def generate_ramadan_calendar(city, data):
    # Dimensions for horizontal readability
    width, height = 1400, 1100
    
    # Premium Background: Emerald / Deep Green Gradient
    image = Image.new('RGB', (width, height), color=(2, 44, 34))
    draw = ImageDraw.Draw(image)
    
    # Simple Gradient for depth
    for i in range(height):
        r = int(2 + (i / height) * 10)
        g = int(44 + (i / height) * 20)
        b = int(34 + (i / height) * 10)
        draw.line([(0, i), (width, i)], fill=(r, g, b))

    # Fonts - Using larger sizes for clarity
    try:
        # Standard fonts on windows
        title_font = ImageFont.truetype("arialbd.ttf", 90)
        header_font = ImageFont.truetype("arialbd.ttf", 45)
        table_font = ImageFont.truetype("arialbd.ttf", 36)
        footer_font = ImageFont.truetype("arial.ttf", 30)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        table_font = ImageFont.load_default()
        footer_font = ImageFont.load_default()

    # Draw Title Area (Gold & White)
    draw.text((width/2, 80), "RAMAZON TAQVIMI - 2026", fill=(251, 191, 36), font=title_font, anchor="mm")
    draw.text((width/2, 170), f"Hudud: {city.upper()}", fill=(255, 255, 255), font=header_font, anchor="mm")
    draw.line([(width/2 - 300, 220), (width/2 + 300, 220)], fill=(251, 191, 36), width=5)

    # Table Setup (2 Columns)
    col_width = (width - 150) // 2
    row_height = 45
    start_y = 280
    
    headers = ["KUN", "SAHAR", "IFTOR"]
    
    def draw_table_side(x_offset, days_data):
        # Header BG
        draw.rounded_rectangle([x_offset, start_y, x_offset + col_width, start_y + 80], radius=15, fill=(6, 78, 59))
        # Header Text
        draw.text((x_offset + 70, start_y + 40), headers[0], fill=(251, 191, 36), font=header_font, anchor="mm")
        draw.text((x_offset + col_width/2 + 20, start_y + 40), headers[1], fill=(251, 191, 36), font=header_font, anchor="mm")
        draw.text((x_offset + col_width - 90, start_y + 40), headers[2], fill=(251, 191, 36), font=header_font, anchor="mm")
        
        y = start_y + 100
        for i, day in enumerate(days_data):
            fajr = day['timings']['Fajr'].split(' ')[0]
            maghrib = day['timings']['Maghrib'].split(' ')[0]
            day_num = day['date']['hijri']['day']
            
            # Row Background
            if i % 2 == 0:
                draw.rounded_rectangle([x_offset - 10, y-5, x_offset + col_width + 10, y + row_height - 5], radius=8, fill=(13, 84, 68))
            
            # Text
            draw.text((x_offset + 70, y + row_height/2 - 5), str(day_num), fill=(255, 255, 255), font=table_font, anchor="mm")
            draw.text((x_offset + col_width/2 + 20, y + row_height/2 - 5), fajr, fill=(255, 255, 255), font=table_font, anchor="mm")
            draw.text((x_offset + col_width - 90, y + row_height/2 - 5), maghrib, fill=(251, 191, 36), font=table_font, anchor="mm")
            y += row_height

    # Split data into 1-15 and 16-30
    left_data = data[:15]
    right_data = data[15:30]
    
    draw_table_side(50, left_data)
    draw_table_side(width/2 + 25, right_data)

    # Footer
    footer_text = "Namoz.bot tomonidan taqdim etildi | @namoz_bot"
    draw.text((width/2, height - 60), footer_text, fill=(167, 139, 250), font=footer_font, anchor="mm")

    os.makedirs("data", exist_ok=True)
    output_path = f"data/ramadan_{city}.png"
    image.save(output_path)
    return output_path
