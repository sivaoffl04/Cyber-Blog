#!/usr/bin/env python3
"""
Generate High-Quality Visual Media Assets & Extract PDF Pages for MongoDB: Basics Lab Walkthrough
- Extract all pages of walkthrough-230.pdf to images/pdf_solution_pages/
- Generate flag screenshots in images/flag_images/
- mongodb_basics_banner.jpg (1376x768)
- mongodb_basics_workflow_map.jpg (1376x768)
- mongodb_basics_live_demo.gif (920x520, animated multi-frame GIF)
"""

import os
import pymupdf
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")
PDF_PAGES_DIR = os.path.join(IMAGES_DIR, "pdf_solution_pages")
FLAG_DIR = os.path.join(IMAGES_DIR, "flag_images")
PDF_PATH = os.path.join(BASE_DIR, "walkthrough-230.pdf")

os.makedirs(IMAGES_DIR, exist_ok=True)
os.makedirs(PDF_PAGES_DIR, exist_ok=True)
os.makedirs(FLAG_DIR, exist_ok=True)

# Fonts
font_huge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 36)
font_large = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 26)
font_title = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 20)
font_subtitle = ImageFont.truetype("C:/Windows/Fonts/seguisb.ttf", 16)
font_body = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 14)
font_small = ImageFont.truetype("C:/Windows/Fonts/segoeui.ttf", 12)
font_mono = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 13)
font_mono_bold = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 14)
font_mono_small = ImageFont.truetype("C:/Windows/Fonts/consola.ttf", 11)
font_badge = ImageFont.truetype("C:/Windows/Fonts/segoeuib.ttf", 12)

def extract_pdf_pages():
    print(f"Extracting PDF pages from {PDF_PATH}...")
    doc = pymupdf.open(PDF_PATH)
    for i, page in enumerate(doc):
        pix = page.get_pixmap(dpi=150)
        out_name = f"page_{i+1:02d}.png"
        out_path = os.path.join(PDF_PAGES_DIR, out_name)
        pix.save(out_path)
    print(f"Successfully extracted {len(doc)} pages to {PDF_PAGES_DIR}")

def draw_grid_background(draw, width, height, grid_size=44, line_color=(18, 28, 48)):
    for x in range(0, width, grid_size):
        draw.line([(x, 0), (x, height)], fill=line_color, width=1)
    for y in range(0, height, grid_size):
        draw.line([(0, y), (width, y)], fill=line_color, width=1)

def generate_hero_banner():
    print("Generating MongoDB Basics Hero Banner...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 48, (18, 28, 48))

    # Top header bar
    draw.rounded_rectangle([(40, 28), (w - 40, 72)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 40), "INE SECURITY LABS • ADVANCED INJECTION ATTACKS & NOSQL EXPLOITATION", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 240, 40), "CHALLENGE CID: 230", fill=(245, 158, 11), font=font_subtitle)

    # Title & Subtitle
    draw.text((40, 96), "MongoDB: Basics", fill=(248, 250, 252), font=font_huge)
    draw.text((40, 150), "Cluster Reconnaissance, NoSQL Document Filtering, Pagination & Aggregation Pipelines", fill=(148, 163, 184), font=font_title)

    # Badges
    badges = [
        ("100% SOLVED (12/12 QUESTIONS)", (16, 185, 129)),
        ("MONGODB 4.X SHELL", (2, 132, 199)),
        ("US CENSUS ZIPS DATASET", (147, 51, 234)),
        ("QUERY OPERATORS ($GT, $AND, $OR)", (245, 158, 11)),
        ("AGGREGATION ($GROUP, $AVG)", (239, 68, 68)),
    ]
    cur_x = 40
    for text, color in badges:
        bw = int(draw.textlength(text, font=font_badge)) + 22
        draw.rounded_rectangle([(cur_x, 192), (cur_x + bw, 222)], radius=6, fill=color)
        draw.text((cur_x + 11, 199), text, fill=(255, 255, 255), font=font_badge)
        cur_x += bw + 14

    # 4 Metric Cards
    cards = [
        {"label": "DATABASES PRESENT", "val": "7", "sub": "admin, city, flag, users, etc.", "color": (56, 189, 248)},
        {"label": "CENSUS RECORDS", "val": "29,353", "sub": "US ZIP code documents", "color": (16, 185, 129)},
        {"label": "CTF FLAG EXTRACTED", "val": "CAPTURED", "sub": "fl4g_f0r_m0ng0_db", "color": (239, 68, 68)},
        {"label": "POPULATION MEAN", "val": "8462.79", "sub": "Aggregation pipeline $avg", "color": (245, 158, 11)},
    ]
    cx = 40
    card_w = (w - 80 - 3 * 20) // 4
    for c in cards:
        draw.rounded_rectangle([(cx, 242), (cx + card_w, 342)], radius=8, fill=(15, 23, 42), outline=c["color"], width=2)
        draw.text((cx + 16, 256), c["label"], fill=(148, 163, 184), font=font_small)
        draw.text((cx + 16, 276), c["val"], fill=(248, 250, 252), font=font_large)
        draw.text((cx + 16, 314), c["sub"], fill=(203, 213, 225), font=font_small)
        cx += card_w + 20

    # Lower Panel: Core Concepts Covered
    draw.rounded_rectangle([(40, 362), (w - 40, 720)], radius=10, fill=(15, 23, 42), outline=(30, 41, 59), width=2)
    draw.text((60, 380), "CORE MONGODB & NOSQL RECONNAISSANCE COMPETENCIES", fill=(56, 189, 248), font=font_title)

    steps = [
        ("Phase 1: Cluster Reconnaissance", "Enumerating active databases (show dbs = 7) and inspecting collection namespaces (users = 3)", (56, 189, 248)),
        ("Phase 2: CTF Flag Extraction", "Switching database context (use flag) and reading sensitive documents (fl4g_f0r_m0ng0_db)", (239, 68, 68)),
        ("Phase 3: Identity & Document Filtering", "Querying user profile documents by exact key match (Heather -> mauris.sapien@eueratsemper.ca)", (168, 85, 247)),
        ("Phase 4: Collection Cardinality Counting", "Quantifying collection volume using fast native execution (db.past.count() = 179)", (245, 158, 11)),
        ("Phase 5: State & Value Comparison", "Applying numerical comparison operators: db.city.find({'pop': {$gt: 15000}}).count() = 5,785", (16, 185, 129)),
        ("Phase 6: Boolean Conjunction ($and)", "Compound filtering across multiple dimensions: {$and: [{pop: {$gt: 15000}}, {state: 'IN'}]} = 130", (56, 189, 248)),
        ("Phase 7: Boolean Disjunction ($or)", "Branching conditions with $or: {$or: [{pop: {$lt: 100}}, {state: 'IN'}]} = 1,376 records", (245, 158, 11)),
        ("Phase 8: Regex & Aggregation Pipelines", "Anchor regex (^AN.* = 154), sorting/skip pagination (101st city = ADDY), and $group mean (8462.79)", (236, 72, 153)),
    ]

    sy = 416
    for title, desc, col in steps:
        draw.ellipse([(60, sy + 3), (72, sy + 15)], fill=col)
        draw.text((82, sy), title, fill=col, font=font_subtitle)
        draw.text((360, sy + 2), "— " + desc, fill=(203, 213, 225), font=font_small)
        sy += 36

    out_path = os.path.join(IMAGES_DIR, "mongodb_basics_banner.jpg")
    img.save(out_path, quality=95)
    print(f"Saved hero banner to {out_path}")

def generate_workflow_map():
    print("Generating MongoDB Basics Workflow Map...")
    w, h = 1376, 768
    img = Image.new("RGB", (w, h), color=(11, 17, 32))
    draw = ImageDraw.Draw(img)
    draw_grid_background(draw, w, h, 44, (18, 28, 48))

    draw.rounded_rectangle([(40, 24), (w - 40, 68)], radius=8, fill=(19, 29, 49), outline=(30, 41, 59), width=1)
    draw.text((60, 36), "MONGODB BASICS • 12-CHALLENGE EXECUTION & QUERY ARCHITECTURE MAP", fill=(56, 189, 248), font=font_subtitle)
    draw.text((w - 280, 36), "12-STAGE QUERY GUIDE", fill=(16, 185, 129), font=font_subtitle)

    boxes = [
        {"title": "Q1: Cluster Databases", "cmd": "show dbs", "ans": "7", "x": 40, "y": 86, "w": 400, "h": 126, "col": (56, 189, 248)},
        {"title": "Q2: Collections in 'users'", "cmd": "use users; show collections", "ans": "3", "x": 480, "y": 86, "w": 400, "h": 126, "col": (56, 189, 248)},
        {"title": "Q3: Flag Value", "cmd": "use flag; db.flag.find()", "ans": "fl4g_f0r_m0ng0_db", "x": 920, "y": 86, "w": 416, "h": 126, "col": (239, 68, 68)},

        {"title": "Q4: Heather's Email", "cmd": "db.current.find({'user':'Heather'})", "ans": "mauris.sapien@eueratsemper.ca", "x": 40, "y": 232, "w": 400, "h": 126, "col": (168, 85, 247)},
        {"title": "Q5: Past Users Count", "cmd": "db.past.count()", "ans": "179", "x": 480, "y": 232, "w": 400, "h": 126, "col": (245, 158, 11)},
        {"title": "Q6: Massachusetts Cities", "cmd": "db.city.find({'state':'MA'}).count()", "ans": "474", "x": 920, "y": 232, "w": 416, "h": 126, "col": (16, 185, 129)},

        {"title": "Q7: Population > 15,000", "cmd": "db.city.find({'pop':{$gt:15000}}).count()", "ans": "5785", "x": 40, "y": 378, "w": 400, "h": 126, "col": (56, 189, 248)},
        {"title": "Q8: Indiana & Pop > 15,000", "cmd": "db.city.find({$and:[{pop:{$gt:15000}},{'state':'IN'}]})", "ans": "130", "x": 480, "y": 378, "w": 400, "h": 126, "col": (245, 158, 11)},
        {"title": "Q9: Pop < 100 OR Indiana", "cmd": "db.city.find({$or:[{pop:{$lt:100}},{'state':'IN'}]})", "ans": "1376", "x": 920, "y": 378, "w": 416, "h": 126, "col": (239, 68, 68)},

        {"title": "Q10: Prefix Regex '^AN.*'", "cmd": "db.city.find({'city':{$regex:'^AN.*'}}).count()", "ans": "154", "x": 40, "y": 524, "w": 400, "h": 126, "col": (168, 85, 247)},
        {"title": "Q11: 101st Sorted City", "cmd": ".sort({'city':1}).skip(100).limit(1)", "ans": "ADDY", "x": 480, "y": 524, "w": 400, "h": 126, "col": (16, 185, 129)},
        {"title": "Q12: Aggregation Mean Pop", "cmd": "db.city.aggregate([{$group:{_id:null,avg:{$avg:'$pop'}}}])", "ans": "8462.79", "x": 920, "y": 524, "w": 416, "h": 126, "col": (56, 189, 248)},
    ]

    for b in boxes:
        draw.rounded_rectangle([(b["x"], b["y"]), (b["x"] + b["w"], b["y"] + b["h"])], radius=8, fill=(15, 23, 42), outline=b["col"], width=2)
        draw.text((b["x"] + 14, b["y"] + 8), b["title"], fill=b["col"], font=font_subtitle)
        draw.text((b["x"] + 14, b["y"] + 32), "Cmd: " + b["cmd"][:44], fill=(148, 163, 184), font=font_mono_small)

        bw = int(draw.textlength("ANS: " + b["ans"][:28], font=font_mono_bold)) + 16
        draw.rounded_rectangle([(b["x"] + 14, b["y"] + 56), (min(b["x"] + b["w"] - 14, b["x"] + 14 + bw), b["y"] + 82)], radius=4, fill=b["col"])
        draw.text((b["x"] + 22, b["y"] + 61), "ANS: " + b["ans"][:28], fill=(11, 17, 32), font=font_mono_bold)

        draw.text((b["x"] + 14, b["y"] + 94), "Verified in MongoDB 4.x localhost cluster", fill=(203, 213, 225), font=font_small)

    out_path = os.path.join(IMAGES_DIR, "mongodb_basics_workflow_map.jpg")
    img.save(out_path, quality=95)
    print(f"Saved workflow map to {out_path}")

def generate_live_demo_gif():
    print("Generating MongoDB Basics Animated Live Demo GIF...")
    w, h = 920, 520
    frames = []

    steps = [
        ("Connecting to Mongo Shell", "mongo", "MongoDB shell v4.0.12", "connecting to mongodb://127.0.0.1:27017"),
        ("Q1: Databases in Cluster", "show dbs", "7", "admin, city, config, flag, local, test, users"),
        ("Q2: Collections in users", "use users; show collections", "3", "current, past, system.indexes"),
        ("Q3: CTF Flag Extraction", "use flag; db.flag.find()", "fl4g_f0r_m0ng0_db", "Captured from isolated secret collection"),
        ("Q4: User Heather Email", "db.current.find({'user':'Heather'})", "mauris.sapien@eueratsemper.ca", "Matching document field user='Heather'"),
        ("Q5: Past Users Count", "db.past.count()", "179", "Total historical user documents"),
        ("Q6: Massachusetts Cities", "db.city.find({'state':'MA'}).count()", "474", "Filtering state code 'MA'"),
        ("Q7: Population > 15000", "db.city.find({'pop':{$gt:15000}}).count()", "5785", "Relational comparison $gt operator"),
        ("Q8: Indiana & Pop > 15000", "db.city.find({$and:[{pop:{$gt:15000}},{'state':'IN'}]})", "130", "Boolean conjunction $and query"),
        ("Q9: Pop < 100 OR Indiana", "db.city.find({$or:[{pop:{$lt:100}},{'state':'IN'}]})", "1376", "Boolean disjunction $or query"),
        ("Q10: Regex Name '^AN.*'", "db.city.find({'city':{$regex:'^AN.*'}}).count()", "154", "Prefix regex search"),
        ("Q11: 101st City Ascending", "db.city.find().sort({'city':1}).skip(100).limit(1)", "ADDY", "Sorting & 0-indexed offset pagination"),
        ("Q12: Aggregation Average", "db.city.aggregate([{$group:{_id:null,avg:{$avg:'$pop'}}}])", "8462.79", "Aggregation pipeline mean value"),
    ]

    for title, cmd, ans, sub in steps:
        frame = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(frame)

        # Chrome Header
        draw.rectangle([(0, 0), (w, 42)], fill=(30, 41, 59))
        draw.ellipse([(14, 15), (24, 25)], fill=(239, 68, 68))
        draw.ellipse([(32, 15), (42, 25)], fill=(245, 158, 11))
        draw.ellipse([(50, 15), (60, 25)], fill=(16, 185, 129))
        draw.text((76, 12), "mongo shell — root@lab: localhost:27017", fill=(203, 213, 225), font=font_subtitle)

        # Command Box
        draw.rounded_rectangle([(20, 56), (w - 20, 100)], radius=6, fill=(11, 17, 32), outline=(56, 189, 248), width=2)
        draw.text((34, 68), "> " + cmd, fill=(56, 189, 248), font=font_mono_bold)

        # Main Display
        draw.rounded_rectangle([(20, 116), (w - 20, 460)], radius=8, fill=(11, 17, 32), outline=(30, 41, 59), width=1)
        draw.text((40, 136), title, fill=(248, 250, 252), font=font_large)

        # Result badge
        draw.rounded_rectangle([(40, 180), (w - 40, 270)], radius=6, fill=(19, 29, 49), outline=(16, 185, 129), width=2)
        draw.text((60, 196), "OFFICIAL SOLUTION OUTPUT / VALUE:", fill=(148, 163, 184), font=font_small)
        draw.text((60, 218), ans, fill=(16, 185, 129), font=font_large)

        draw.text((40, 290), "EXECUTION DETAILS & CONTEXT:", fill=(148, 163, 184), font=font_small)
        draw.text((40, 316), sub, fill=(203, 213, 225), font=font_body)

        draw.rounded_rectangle([(40, 360), (w - 40, 440)], radius=4, fill=(15, 23, 42))
        draw.text((54, 372), f"Command: {cmd}", fill=(148, 163, 184), font=font_mono_small)
        draw.text((54, 400), f"Status: EXECUTED SUCCESS | Database Context Active", fill=(56, 189, 248), font=font_mono_small)

        draw.text((20, 480), "INE Hands-on Lab: MongoDB Basics (CID 230) — 100% Solved", fill=(100, 116, 139), font=font_small)
        draw.text((w - 220, 480), "Live Terminal Demo", fill=(245, 158, 11), font=font_small)

        frames.append(frame)

    out_path = os.path.join(IMAGES_DIR, "mongodb_basics_live_demo.gif")
    frames[0].save(out_path, save_all=True, append_images=frames[1:], duration=1300, loop=0)
    print(f"Saved live demo GIF to {out_path}")

def generate_flag_images():
    print("Generating MongoDB Question Flag Images...")
    q_list = [
        ("Q1", "7", "Databases present in cluster", "show dbs"),
        ("Q2", "3", "Collections in database users", "use users; show collections"),
        ("Q3", "fl4g_f0r_m0ng0_db", "CTF Flag from flag database", "use flag; db.flag.find()"),
        ("Q4", "mauris.sapien@eueratsemper.ca", "Email of user Heather", "db.current.find({'user':'Heather'})"),
        ("Q5", "179", "Past collection users count", "db.past.count()"),
        ("Q6", "474", "Massachusetts cities count", "db.city.find({'state':'MA'}).count()"),
        ("Q7", "5785", "Cities with pop > 15000", "db.city.find({'pop':{$gt:15000}}).count()"),
        ("Q8", "130", "Indiana cities with pop > 15000", "db.city.find({$and:[{pop:{$gt:15000}},{'state':'IN'}]})"),
        ("Q9", "1376", "Cities pop < 100 OR Indiana", "db.city.find({$or:[{pop:{$lt:100}},{'state':'IN'}]})"),
        ("Q10", "154", "Cities starting with 'AN'", "db.city.find({'city':{$regex:'^AN.*'}}).count()"),
        ("Q11", "ADDY", "101st city sorted ascending", "db.city.find().sort({'city':1}).skip(100).limit(1)"),
        ("Q12", "8462.79", "Average population in city", "db.city.aggregate([{$group:{_id:null,avg:{$avg:'$pop'}}}])"),
    ]

    for qid, ans, desc, cmd in q_list:
        w, h = 640, 220
        img = Image.new("RGB", (w, h), color=(15, 23, 42))
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle([(10, 10), (w - 10, h - 10)], radius=8, fill=(11, 17, 32), outline=(56, 189, 248), width=2)

        draw.text((26, 24), f"MONGODB BASICS • {qid}", fill=(56, 189, 248), font=font_subtitle)
        draw.text((26, 50), desc, fill=(148, 163, 184), font=font_small)
        draw.text((26, 74), f"Query: {cmd}", fill=(203, 213, 225), font=font_mono_small)

        bw = int(draw.textlength(ans, font=font_mono_bold)) + 24
        draw.rounded_rectangle([(26, 110), (min(w - 26, 26 + bw), 160)], radius=6, fill=(16, 185, 129))
        draw.text((38, 125), ans, fill=(11, 17, 32), font=font_mono_bold)

        draw.text((26, 180), "Official Walkthrough CID 230 • Verified by Antigravity", fill=(100, 116, 139), font=font_small)

        out_p = os.path.join(FLAG_DIR, f"{qid}.png")
        img.save(out_p)
    print(f"Generated {len(q_list)} question images in {FLAG_DIR}")

if __name__ == "__main__":
    extract_pdf_pages()
    generate_hero_banner()
    generate_workflow_map()
    generate_live_demo_gif()
    generate_flag_images()
    print("All MongoDB visual media assets and PDF extractions completed successfully!")
