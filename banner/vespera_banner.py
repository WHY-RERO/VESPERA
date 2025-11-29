import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math
import os

class VesperaBanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Vespera - Banner Oluşturucu")
        self.root.geometry("1000x800")
        self.root.configure(bg='#000000')
        
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = tk.Frame(self.root, bg='#000000', height=80)
        header.pack(fill=tk.X)
        
        title = tk.Label(
            header,
            text="VESPERA - Anlık Konum Takip Sistemi",
            font=('Arial', 20, 'bold'),
            bg='#000000',
            fg='#00ff88'
        )
        title.pack(pady=25)
        
        # Main container
        main = tk.Frame(self.root, bg='#000000')
        main.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Preview area
        preview_frame = tk.LabelFrame(
            main,
            text="Banner Önizleme",
            font=('Arial', 12, 'bold'),
            bg='#000000',
            fg='#00ff88',
            padx=15,
            pady=15
        )
        preview_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 20))
        
        self.preview_label = tk.Label(
            preview_frame,
            text="Banner oluşturuluyor...",
            bg='#000000',
            fg='#ffffff'
        )
        self.preview_label.pack(expand=True)
        
        # Buttons
        btn_frame = tk.Frame(main, bg='#000000')
        btn_frame.pack(fill=tk.X)
        
        create_btn = tk.Button(
            btn_frame,
            text="🎨 Banner Oluştur",
            font=('Arial', 14, 'bold'),
            bg='#00ff88',
            fg='#000000',
            activebackground='#00cc6a',
            relief=tk.FLAT,
            padx=40,
            pady=15,
            cursor='hand2',
            command=self.create_banner
        )
        create_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        save_btn = tk.Button(
            btn_frame,
            text="💾 Kaydet",
            font=('Arial', 14, 'bold'),
            bg='#0066ff',
            fg='#ffffff',
            activebackground='#0052cc',
            relief=tk.FLAT,
            padx=40,
            pady=15,
            cursor='hand2',
            command=self.save_banner
        )
        save_btn.pack(side=tk.LEFT)
        
        self.banner_image = None
        self.create_banner()
        
    def create_banner(self):
        width, height = 1920, 1080
        img = Image.new('RGB', (width, height), '#000000')
        draw = ImageDraw.Draw(img)
        
        # Gradient background
        for y in range(height):
            ratio = y / height
            r = int(0 + (10 * ratio))
            g = int(0 + (20 * ratio))
            b = int(0 + (30 * ratio))
            draw.line([(0, y), (width, y)], fill=(r, g, b))
        
        # Create glow effect layers
        glow_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        glow_draw = ImageDraw.Draw(glow_img)
        
        center_x, center_y = width // 2, height // 2
        
        # Eye symbol - outer diamond
        diamond_size = 400
        diamond_points = [
            (center_x, center_y - diamond_size),
            (center_x + diamond_size * 0.7, center_y),
            (center_x, center_y + diamond_size),
            (center_x - diamond_size * 0.7, center_y)
        ]
        
        # Draw diamond with gradient
        for i in range(len(diamond_points)):
            p1 = diamond_points[i]
            p2 = diamond_points[(i + 1) % len(diamond_points)]
            
            # Color gradient
            colors = [
                (0, 255, 136, 200),  # Green
                (0, 200, 255, 200),  # Cyan
                (255, 0, 150, 200),  # Pink
                (150, 0, 255, 200)   # Purple
            ]
            
            # Draw thick glowing line
            for thickness in range(15, 0, -2):
                alpha = int(200 * (1 - thickness/15))
                color = tuple(list(colors[i][:3]) + [alpha])
                glow_draw.line([p1, p2], fill=color, width=thickness)
        
        # Eye shape
        eye_width = 250
        eye_height = 120
        eye_left = center_x - eye_width // 2
        eye_top = center_y - eye_height // 2
        eye_right = center_x + eye_width // 2
        eye_bottom = center_y + eye_height // 2
        
        # Draw eye outline with glow
        for thickness in range(20, 0, -1):
            alpha = int(150 * (1 - thickness/20))
            # Top curve
            glow_draw.arc(
                [eye_left, eye_top - 20, eye_right, eye_bottom + 20],
                start=0,
                end=180,
                fill=(0, 255, 136, alpha),
                width=thickness
            )
            # Bottom curve
            glow_draw.arc(
                [eye_left, eye_top - 20, eye_right, eye_bottom + 20],
                start=180,
                end=360,
                fill=(255, 0, 150, alpha),
                width=thickness
            )
        
        # Pupil - glowing circle
        pupil_size = 80
        for size in range(pupil_size + 30, pupil_size - 10, -5):
            alpha = int(200 * (1 - (size - pupil_size) / 30))
            glow_draw.ellipse(
                [center_x - size//2, center_y - size//2, 
                 center_x + size//2, center_y + size//2],
                fill=(255, 0, 100, max(0, alpha)),
                outline=(255, 50, 150, max(0, alpha))
            )
        
        # Network lines from eye to diamond
        for i, point in enumerate(diamond_points):
            # Multiple lines with varying opacity
            for offset in range(-10, 11, 5):
                x1 = center_x + offset
                y1 = center_y
                x2 = point[0] + offset
                y2 = point[1]
                
                alpha = 100 - abs(offset) * 5
                glow_draw.line(
                    [x1, y1, x2, y2],
                    fill=(0, 255, 136, max(0, alpha)),
                    width=2
                )
        
        # Bottom focal point
        focal_y = center_y + diamond_size + 50
        for size in range(30, 0, -2):
            alpha = int(255 * (1 - size/30))
            glow_draw.ellipse(
                [center_x - size, focal_y - size,
                 center_x + size, focal_y + size],
                fill=(255, 200, 0, alpha)
            )
        
        # Apply glow blur
        glow_img = glow_img.filter(ImageFilter.GaussianBlur(radius=3))
        
        # Composite glow onto main image
        img = Image.alpha_composite(img.convert('RGBA'), glow_img).convert('RGB')
        draw = ImageDraw.Draw(img)
        
        # VESPERA text with glow effect
        try:
            font_large = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 180)
            font_sub = ImageFont.truetype("C:/Windows/Fonts/arial.ttf", 50)
        except:
            font_large = ImageFont.load_default()
            font_sub = ImageFont.load_default()
        
        text = "VESPERA"
        subtext = "Anlık Konum Takip Sistemi"
        
        # Text position
        text_y = center_y + 350
        
        # Draw text with multiple layers for glow
        text_img = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        text_draw = ImageDraw.Draw(text_img)
        
        # Main text glow
        for offset in range(10, 0, -1):
            alpha = int(100 * (1 - offset/10))
            text_draw.text(
                (center_x - 500 + offset, text_y + offset),
                text,
                font=font_large,
                fill=(0, 255, 136, alpha)
            )
        
        # Main text
        text_draw.text(
            (center_x - 500, text_y),
            text,
            font=font_large,
            fill=(0, 255, 136, 255)
        )
        
        # Subtext
        bbox = text_draw.textbbox((0, 0), text, font=font_large)
        subtext_x = center_x - 400
        subtext_y = text_y + 200
        
        text_draw.text(
            (subtext_x, subtext_y),
            subtext,
            font=font_sub,
            fill=(0, 200, 255, 200)
        )
        
        # Apply text blur for glow
        text_img = text_img.filter(ImageFilter.GaussianBlur(radius=2))
        
        # Composite text
        img = Image.alpha_composite(img.convert('RGBA'), text_img).convert('RGB')
        
        # Save for preview
        self.banner_image = img
        
        # Resize for preview
        preview_width = 800
        preview_height = int(height * (preview_width / width))
        preview_img = img.resize((preview_width, preview_height), Image.Resampling.LANCZOS)
        
        # Convert to PhotoImage
        from PIL import ImageTk
        photo = ImageTk.PhotoImage(preview_img)
        
        self.preview_label.configure(image=photo, text='')
        self.preview_label.image = photo
        
    def save_banner(self):
        if self.banner_image:
            from tkinter import filedialog
            filename = filedialog.asksaveasfilename(
                defaultextension=".png",
                filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg")]
            )
            if filename:
                self.banner_image.save(filename, quality=95)
                tk.messagebox.showinfo("Başarılı", f"Banner kaydedildi:\n{filename}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VesperaBanner(root)
    root.mainloop()

