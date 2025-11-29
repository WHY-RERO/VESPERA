#!/usr/bin/env python3


from PIL import Image, ImageDraw, ImageFont
import os

def create_vespera_banner_simple():
    """Hızlı Vespera banner oluşturur"""
    
    width, height = 1920, 1080
    img = Image.new('RGB', (width, height), '#000000')
    draw = ImageDraw.Draw(img)
    
    
    for y in range(height):
        ratio = y / height
        r = int(5 * ratio)
        g = int(15 * ratio)
        b = int(25 * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    
    try:
        font_large = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 200)
        font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 60)
    except:
        font_large = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    
    
    text = "VESPERA"
    subtext = "Anlık Konum Takip Sistemi"
    
    
    center_x = width // 2
    text_y = height // 2 - 50
    
    
    for offset in range(8, 0, -1):
        alpha = 30 - offset * 3
        draw.text(
            (center_x - 600 + offset, text_y + offset),
            text,
            font=font_large,
            fill=(0, 255, 136)
        )
    
    
    draw.text(
        (center_x - 600, text_y),
        text,
        font=font_large,
        fill=(0, 255, 136)
    )
    
    
    draw.text(
        (center_x - 500, text_y + 250),
        subtext,
        font=font_sub,
        fill=(0, 200, 255)
    )
    
    
    eye_x, eye_y = center_x, text_y - 300
    eye_size = 100
    
    
    draw.ellipse(
        [eye_x - eye_size, eye_y - eye_size//2,
         eye_x + eye_size, eye_y + eye_size//2],
        outline=(0, 255, 136),
        width=5
    )
    
    
    draw.ellipse(
        [eye_x - 30, eye_y - 30,
         eye_x + 30, eye_y + 30],
        fill=(255, 0, 100),
        outline=(255, 50, 150)
    )
    
    #
    output_file = "vespera_banner.png"
    img.save(output_file, quality=95)
    print(f"✅ Banner oluşturuldu: {output_file}")
    return output_file

if __name__ == "__main__":
    create_vespera_banner_simple()

