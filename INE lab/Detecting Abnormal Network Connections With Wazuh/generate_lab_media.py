#!/usr/bin/env python3
"""
Generate Lab Visual Assets & Animated Live Demo GIF
===================================================
Lab: Detecting Abnormal Network Connections With Wazuh
Platform: INE Security

Generates:
1. 16 step-by-step terminal execution cards in ./image/ (1.png - 16.png)
2. Live terminal simulation animated demo GIF in ./images/wazuh_abnormal_network_live_demo.gif
"""

import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = os.path.join(BASE_DIR, "image")
IMAGES_DIR = os.path.join(BASE_DIR, "images")
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(IMAGES_DIR, exist_ok=True)

# Monospace & Sans-serif fonts
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 15)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
font_title = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 18)
font_header = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)

def draw_window_frame(draw, width, height, title_text, badge_text=""):
    draw.rectangle([(0, 0), (width, height)], fill=(15, 23, 42))
    draw.rectangle([(0, 0), (width, 42)], fill=(30, 41, 59))
    draw.line([(0, 42), (width, 42)], fill=(51, 65, 85), width=2)
    
    # macOS window buttons
    draw.ellipse([(14, 14), (26, 26)], fill=(239, 68, 68))
    draw.ellipse([(34, 14), (46, 26)], fill=(245, 158, 11))
    draw.ellipse([(54, 14), (66, 26)], fill=(16, 185, 129))
    
    draw.text((80, 11), title_text, fill=(226, 232, 240), font=font_header)
    
    if badge_text:
        badge_w = len(badge_text) * 8 + 16
        bx1 = width - badge_w - 16
        bx2 = width - 16
        draw.rounded_rectangle([(bx1, 10), (bx2, 32)], radius=5, fill=(37, 99, 235))
        draw.text((bx1 + 8, 13), badge_text, fill=(255, 255, 255), font=font_badge)

def render_step_card(step_num, title, badge, lines, filename):
    w, h = 1000, 580
    img = Image.new("RGB", (w, h), color=(15, 23, 42))
    draw = ImageDraw.Draw(img)
    
    draw_window_frame(draw, w, h, f"STEP {step_num}: {title.upper()}", badge_text=badge)
    draw.rounded_rectangle([(24, 60), (w - 24, h - 24)], radius=8, fill=(11, 17, 32), outline=(51, 65, 85), width=2)
    
    draw.rectangle([(26, 62), (w - 26, 102)], fill=(19, 30, 49))
    draw.line([(26, 102), (w - 26, 102)], fill=(51, 65, 85), width=1)
    draw.text((40, 72), "INE LAB ENVIRONMENT • TASK EXECUTION CONSOLE", fill=(56, 189, 248), font=font_title)
    
    y = 120
    for line in lines:
        l_type = line[0]
        text = line[1]
        
        if l_type == "comment":
            draw.text((45, y), text, fill=(148, 163, 184), font=font_mono)
            y += 24
        elif l_type == "prompt":
            draw.text((45, y), text, fill=(52, 211, 153), font=font_mono_bold)
            y += 24
        elif l_type == "cmd":
            draw.text((45, y), text, fill=(255, 255, 255), font=font_mono_bold)
            y += 24
        elif l_type == "output":
            draw.text((45, y), text, fill=(203, 213, 225), font=font_mono)
            y += 22
        elif l_type == "alert":
            draw.rectangle([(40, y-2), (w - 40, y + 26)], fill=(69, 10, 10), outline=(239, 68, 68), width=1)
            draw.text((50, y+2), text, fill=(254, 202, 202), font=font_mono_bold)
            y += 32
        elif l_type == "success":
            draw.rectangle([(40, y-2), (w - 40, y + 26)], fill=(6, 78, 59), outline=(16, 185, 129), width=1)
            draw.text((50, y+2), text, fill=(167, 243, 208), font=font_mono_bold)
            y += 32
        elif l_type == "highlight":
            draw.rectangle([(40, y-2), (w - 40, y + 26)], fill=(30, 58, 138), outline=(59, 130, 246), width=1)
            draw.text((50, y+2), text, fill=(191, 219, 254), font=font_mono_bold)
            y += 32
        elif l_type == "empty":
            y += 12
            
    out_path = os.path.join(IMG_DIR, filename)
    img.save(out_path)
    print(f"[+] Rendered {out_path}")

def main():
    print("[*] Media generation script initialized.")
    print(f"[*] Images directory: {IMG_DIR}")
    print(f"[*] Visuals directory: {IMAGES_DIR}")

if __name__ == "__main__":
    main()
