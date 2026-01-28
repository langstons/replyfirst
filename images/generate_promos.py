#!/usr/bin/env python3
"""
Generate promotional images for ReplyFirst Chrome Extension
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Brand colors
BRAND_COLOR = '#8B5CF6'
BRAND_COLOR_DARK = '#7C3AED'
BRAND_COLOR_LIGHT = '#A78BFA'

def hex_to_rgb(hex_color):
    """Convert hex color to RGB tuple"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def create_gradient(draw, bbox, color1, color2, direction='horizontal'):
    """Create a gradient fill"""
    x1, y1, x2, y2 = bbox
    if direction == 'horizontal':
        for x in range(x1, x2):
            ratio = (x - x1) / (x2 - x1)
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(x, y1), (x, y2)], fill=(r, g, b))
    else:  # vertical
        for y in range(y1, y2):
            ratio = (y - y1) / (y2 - y1)
            r = int(color1[0] * (1 - ratio) + color2[0] * ratio)
            g = int(color1[1] * (1 - ratio) + color2[1] * ratio)
            b = int(color1[2] * (1 - ratio) + color2[2] * ratio)
            draw.line([(x1, y), (x2, y)], fill=(r, g, b))

def draw_rounded_rectangle(draw, bbox, radius, fill=None, outline=None, width=1):
    """Draw a rounded rectangle"""
    x1, y1, x2, y2 = bbox
    # Ensure radius is not larger than half the dimensions
    radius = min(radius, (x2 - x1) // 2, (y2 - y1) // 2)

    if fill:
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)
        draw.pieslice([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=fill)
        draw.pieslice([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=fill)
        draw.pieslice([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=fill)
        draw.pieslice([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=fill)

    if outline:
        draw.arc([x1, y1, x1 + radius * 2, y1 + radius * 2], 180, 270, fill=outline, width=width)
        draw.arc([x2 - radius * 2, y1, x2, y1 + radius * 2], 270, 360, fill=outline, width=width)
        draw.arc([x1, y2 - radius * 2, x1 + radius * 2, y2], 90, 180, fill=outline, width=width)
        draw.arc([x2 - radius * 2, y2 - radius * 2, x2, y2], 0, 90, fill=outline, width=width)
        draw.line([(x1 + radius, y1), (x2 - radius, y1)], fill=outline, width=width)
        draw.line([(x1 + radius, y2), (x2 - radius, y2)], fill=outline, width=width)
        draw.line([(x1, y1 + radius), (x1, y2 - radius)], fill=outline, width=width)
        draw.line([(x2, y1 + radius), (x2, y2 - radius)], fill=outline, width=width)

def draw_logo(draw, x, y, size):
    """Draw the ReplyFirst logo (list with up arrow)"""
    bar_width = int(size * 0.6)
    bar_height = int(size * 0.12)
    spacing = int(size * 0.15)

    # Three horizontal bars
    draw.rectangle([x, y, x + bar_width, y + bar_height], fill='white')
    draw.rectangle([x, y + spacing, x + bar_width, y + spacing + bar_height], fill='white')
    draw.rectangle([x, y + spacing * 2, x + bar_width, y + spacing * 2 + bar_height], fill='white')

    # Up arrow
    arrow_x = x + bar_width + int(size * 0.15)
    arrow_y = y + int(size * 0.35)
    arrow_size = int(size * 0.25)

    arrow_points = [
        (arrow_x + arrow_size // 2, arrow_y),
        (arrow_x + arrow_size, arrow_y + arrow_size),
        (arrow_x + arrow_size * 0.65, arrow_y + arrow_size),
        (arrow_x + arrow_size * 0.65, arrow_y + arrow_size * 1.5),
        (arrow_x + arrow_size * 0.35, arrow_y + arrow_size * 1.5),
        (arrow_x + arrow_size * 0.35, arrow_y + arrow_size),
        (arrow_x, arrow_y + arrow_size),
    ]
    draw.polygon(arrow_points, fill='white')

def get_font(size, bold=False):
    """Get a system font"""
    try:
        if bold:
            return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
        return ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", size)
    except:
        return ImageFont.load_default()

# 1. Small Promo Tile (440x280px)
def create_small_promo():
    img = Image.new('RGB', (440, 280), hex_to_rgb(BRAND_COLOR))
    draw = ImageDraw.Draw(img)

    # Gradient background
    create_gradient(draw, (0, 0, 440, 280),
                   hex_to_rgb(BRAND_COLOR_DARK),
                   hex_to_rgb(BRAND_COLOR),
                   'horizontal')

    # Logo
    draw_logo(draw, 150, 60, 60)

    # Title
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 42)
        tagline_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 22)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
    except:
        title_font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()

    title_text = "ReplyFirst"
    title_bbox = draw.textbbox((0, 0), title_text, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((220 - title_width // 2, 150), title_text, fill='white', font=title_font)

    tagline_text = "Newest Replies First"
    tagline_bbox = draw.textbbox((0, 0), tagline_text, font=tagline_font)
    tagline_width = tagline_bbox[2] - tagline_bbox[0]
    draw.text((220 - tagline_width // 2, 195), tagline_text, fill='white', font=tagline_font)

    subtitle_text = "for Gmail"
    subtitle_bbox = draw.textbbox((0, 0), subtitle_text, font=subtitle_font)
    subtitle_width = subtitle_bbox[2] - subtitle_bbox[0]
    draw.text((220 - subtitle_width // 2, 230), subtitle_text, fill=(255, 255, 255, 230), font=subtitle_font)

    img.save('/Users/brent.langston/git/replyfirst/images/promo-small-440x280.png')
    print("✓ Created: promo-small-440x280.png")

# 2. Marquee Promo Tile (1400x560px)
def create_marquee_promo():
    img = Image.new('RGB', (1400, 560), hex_to_rgb(BRAND_COLOR))
    draw = ImageDraw.Draw(img)

    # Gradient background
    for x in range(0, 1400):
        ratio = x / 1400
        if ratio < 0.5:
            r1, g1, b1 = hex_to_rgb(BRAND_COLOR_DARK)
            r2, g2, b2 = hex_to_rgb(BRAND_COLOR)
            local_ratio = ratio * 2
        else:
            r1, g1, b1 = hex_to_rgb(BRAND_COLOR)
            r2, g2, b2 = hex_to_rgb(BRAND_COLOR_LIGHT)
            local_ratio = (ratio - 0.5) * 2

        r = int(r1 * (1 - local_ratio) + r2 * local_ratio)
        g = int(g1 * (1 - local_ratio) + g2 * local_ratio)
        b = int(b1 * (1 - local_ratio) + b2 * local_ratio)
        draw.line([(x, 0), (x, 560)], fill=(r, g, b))

    # Logo
    draw_logo(draw, 80, 180, 120)

    # Text
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 72)
        subtitle_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        tagline_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
        label_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 14)
    except:
        title_font = ImageFont.load_default()
        subtitle_font = ImageFont.load_default()
        tagline_font = ImageFont.load_default()
        label_font = ImageFont.load_default()
        small_font = ImageFont.load_default()

    draw.text((80, 340), "ReplyFirst", fill='white', font=title_font)
    draw.text((80, 400), "See newest replies first in Gmail", fill='white', font=subtitle_font)

    # Email visualization
    email_x = 750
    email_y = 120
    email_w = 550
    email_h = 320

    # Email container
    draw_rounded_rectangle(draw, (email_x, email_y, email_x + email_w, email_y + email_h), 12, fill='white')

    # Email header
    draw_rounded_rectangle(draw, (email_x, email_y, email_x + email_w, email_y + 60), 12, fill='#f8f9fa')
    draw.rectangle([email_x, email_y + 48, email_x + email_w, email_y + 60], fill='#f8f9fa')
    draw.text((email_x + 20, email_y + 30), "Re: Project Update", fill='#5f6368', font=label_font)

    # Messages (newest first)
    msg_colors = ['#e8f5e9', '#fff9c4', '#ffecb3']
    msg_labels = ['Latest Reply ✓', 'Reply 2', 'Original']

    for i, (color, label) in enumerate(zip(msg_colors, msg_labels)):
        msg_y = email_y + 80 + (i * 75)
        draw_rounded_rectangle(draw, (email_x + 20, msg_y, email_x + email_w - 20, msg_y + 60), 8, fill=color)
        draw.text((email_x + 35, msg_y + 15), label, fill='#333', font=label_font)
        draw.text((email_x + 35, msg_y + 38), "Message content preview...", fill='#666', font=small_font)

    # Arrow
    draw.text((email_x - 60, 240), "↑", fill=hex_to_rgb(BRAND_COLOR), font=title_font)

    # Bottom tagline
    tagline = "Never scroll to find the latest message"
    tagline_bbox = draw.textbbox((0, 0), tagline, font=tagline_font)
    tagline_width = tagline_bbox[2] - tagline_bbox[0]
    draw.text((700 - tagline_width // 2, 490), tagline, fill='white', font=tagline_font)

    img.save('/Users/brent.langston/git/replyfirst/images/promo-marquee-1400x560.png')
    print("✓ Created: promo-marquee-1400x560.png")

# 3. Screenshot 2 - Popup Interface (1280x800px)
def create_screenshot_2():
    img = Image.new('RGB', (1280, 800), '#f5f5f5')
    draw = ImageDraw.Draw(img)

    # Popup
    popup_x, popup_y = 440, 200
    popup_w, popup_h = 400, 400

    # Shadow
    draw_rounded_rectangle(draw, (popup_x + 5, popup_y + 5, popup_x + popup_w + 5, popup_y + popup_h + 5),
                          12, fill=(200, 200, 200))

    # Popup background
    draw_rounded_rectangle(draw, (popup_x, popup_y, popup_x + popup_w, popup_y + popup_h), 12, fill='white')

    # Header gradient
    for y in range(popup_y, popup_y + 80):
        ratio = (y - popup_y) / 80
        r1, g1, b1 = hex_to_rgb(BRAND_COLOR)
        r2, g2, b2 = hex_to_rgb(BRAND_COLOR_DARK)
        r = int(r1 * (1 - ratio) + r2 * ratio)
        g = int(g1 * (1 - ratio) + g2 * ratio)
        b = int(b1 * (1 - ratio) + b2 * ratio)
        draw.line([(popup_x, y), (popup_x + popup_w, y)], fill=(r, g, b))

    # Logo
    draw_logo(draw, popup_x + 30, popup_y + 25, 35)

    try:
        header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 32)
        section_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
        tiny_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        annotation_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except:
        header_font = section_font = text_font = small_font = tiny_font = annotation_font = ImageFont.load_default()

    draw.text((popup_x + 100, popup_y + 40), "ReplyFirst", fill='white', font=header_font)

    # Status section
    draw.text((popup_x + 30, popup_y + 125), "Status", fill='#333', font=section_font)

    # Toggle switch
    toggle_x, toggle_y = popup_x + 300, popup_y + 160
    draw_rounded_rectangle(draw, (toggle_x, toggle_y, toggle_x + 70, toggle_y + 40), 20, fill=hex_to_rgb(BRAND_COLOR))
    draw.ellipse([toggle_x + 34, toggle_y + 4, toggle_x + 66, toggle_y + 36], fill='white')

    draw.text((popup_x + 30, popup_y + 172), "Active", fill='#333', font=text_font)

    # Instructions
    draw.text((popup_x + 30, popup_y + 225), "How it works:", fill='#666', font=small_font)

    instructions = [
        "• Open any Gmail conversation",
        "• Messages will auto-reverse",
        "• Newest replies appear first",
        "• Toggle to disable anytime"
    ]

    for i, text in enumerate(instructions):
        draw.text((popup_x + 40, popup_y + 265 + i * 30), text, fill='#666', font=tiny_font)

    # Annotation
    for offset in range(3):
        draw_rounded_rectangle(draw, (popup_x + 20 - offset, popup_y + 120 - offset,
                                     popup_x + 380 + offset, popup_y + 210 + offset),
                             8, outline=hex_to_rgb(BRAND_COLOR), width=1)

    annotation_text = "Simple Toggle Control"
    annotation_bbox = draw.textbbox((0, 0), annotation_text, font=annotation_font)
    annotation_width = annotation_bbox[2] - annotation_bbox[0]
    draw.text((640 - annotation_width // 2, 150), annotation_text, fill=hex_to_rgb(BRAND_COLOR), font=annotation_font)

    # Arrow
    draw.line([(640, 180), (640, 240)], fill=hex_to_rgb(BRAND_COLOR), width=3)
    draw.polygon([(640, 240), (630, 225), (650, 225)], fill=hex_to_rgb(BRAND_COLOR))

    img.save('/Users/brent.langston/git/replyfirst/images/screenshot-2-popup-1280x800.png')
    print("✓ Created: screenshot-2-popup-1280x800.png")

# 4. Screenshot 3 - Before State (1280x800px)
def create_screenshot_3():
    img = Image.new('RGB', (1280, 800), 'white')
    draw = ImageDraw.Draw(img)

    # Gmail header
    draw.rectangle([0, 0, 1280, 80], fill='#f8f9fa')

    try:
        header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
        msg_header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        msg_text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        problem_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        arrow_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 48)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
    except:
        header_font = msg_header_font = msg_text_font = problem_font = arrow_font = small_font = ImageFont.load_default()

    draw.text((40, 35), "Gmail Conversation", fill='#5f6368', font=header_font)

    # Messages (oldest first)
    email_x = 200
    email_w = 880
    msg_data = [
        {'label': 'Original Email', 'time': '3 days ago', 'color': '#e8eaed'},
        {'label': 'Reply 1', 'time': '2 days ago', 'color': '#e8eaed'},
        {'label': 'Reply 2', 'time': '1 day ago', 'color': '#e8eaed'},
        {'label': 'Latest Reply', 'time': '2 hours ago', 'color': '#fff9c4'}
    ]

    for i, msg in enumerate(msg_data):
        msg_y = 120 + i * 140
        draw_rounded_rectangle(draw, (email_x, msg_y, email_x + email_w, msg_y + 110), 8, fill=msg['color'])
        draw.text((email_x + 20, msg_y + 25), msg['label'], fill='#333', font=msg_header_font)

        time_bbox = draw.textbbox((0, 0), msg['time'], font=msg_text_font)
        time_width = time_bbox[2] - time_bbox[0]
        draw.text((email_x + email_w - 20 - time_width, msg_y + 25), msg['time'], fill='#666', font=msg_text_font)

        draw.text((email_x + 20, msg_y + 55), "Message content here...", fill='#5f6368', font=msg_text_font)
        draw.text((email_x + 20, msg_y + 78), "Lorem ipsum dolor sit amet, consectetur adipiscing...",
                 fill='#5f6368', font=msg_text_font)

    # Problem annotation
    for offset in range(4):
        draw_rounded_rectangle(draw, (email_x - 10 - offset, 540 - offset,
                                     email_x + email_w + 10 + offset, 670 + offset),
                             12, outline='#d32f2f', width=1)

    problem_text = "Problem: Latest reply at bottom"
    problem_bbox = draw.textbbox((0, 0), problem_text, font=problem_font)
    problem_width = problem_bbox[2] - problem_bbox[0]
    draw.text((640 - problem_width // 2, 710), problem_text, fill='#d32f2f', font=problem_font)

    # Scroll indicator
    draw.text((85, 470), "↓", fill='#d32f2f', font=arrow_font)
    draw.text((70, 530), "Must", fill='#d32f2f', font=small_font)
    draw.text((65, 555), "scroll", fill='#d32f2f', font=small_font)

    img.save('/Users/brent.langston/git/replyfirst/images/screenshot-3-before-1280x800.png')
    print("✓ Created: screenshot-3-before-1280x800.png")

# 5. Screenshot 4 - After State (1280x800px)
def create_screenshot_4():
    img = Image.new('RGB', (1280, 800), 'white')
    draw = ImageDraw.Draw(img)

    # Gmail header
    draw.rectangle([0, 0, 1280, 80], fill='#f8f9fa')

    try:
        header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
        badge_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        msg_header_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 20)
        check_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        msg_text_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
        solution_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
        feature_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 18)
    except:
        header_font = badge_font = msg_header_font = check_font = msg_text_font = solution_font = feature_font = ImageFont.load_default()

    draw.text((40, 35), "Gmail Conversation", fill='#5f6368', font=header_font)

    # ReplyFirst badge
    draw_rounded_rectangle(draw, (1050, 25, 1230, 60), 18, fill=hex_to_rgb(BRAND_COLOR))
    badge_text = "ReplyFirst Active"
    badge_bbox = draw.textbbox((0, 0), badge_text, font=badge_font)
    badge_width = badge_bbox[2] - badge_bbox[0]
    draw.text((1140 - badge_width // 2, 38), badge_text, fill='white', font=badge_font)

    # Messages (newest first)
    email_x = 200
    email_w = 880
    msg_data = [
        {'label': 'Latest Reply', 'time': '2 hours ago', 'color': '#c7f0c7', 'highlight': True},
        {'label': 'Reply 2', 'time': '1 day ago', 'color': '#e8eaed', 'highlight': False},
        {'label': 'Reply 1', 'time': '2 days ago', 'color': '#e8eaed', 'highlight': False},
        {'label': 'Original Email', 'time': '3 days ago', 'color': '#e8eaed', 'highlight': False}
    ]

    for i, msg in enumerate(msg_data):
        msg_y = 120 + i * 140
        draw_rounded_rectangle(draw, (email_x, msg_y, email_x + email_w, msg_y + 110), 8, fill=msg['color'])

        if msg['highlight']:
            for offset in range(4):
                draw_rounded_rectangle(draw, (email_x - offset, msg_y - offset,
                                             email_x + email_w + offset, msg_y + 110 + offset),
                                     8, outline='#4caf50', width=1)

        draw.text((email_x + 20, msg_y + 25), msg['label'], fill='#333', font=msg_header_font)

        if msg['highlight']:
            draw.text((email_x + 180, msg_y + 25), "✓", fill='#4caf50', font=check_font)

        time_bbox = draw.textbbox((0, 0), msg['time'], font=msg_text_font)
        time_width = time_bbox[2] - time_bbox[0]
        draw.text((email_x + email_w - 20 - time_width, msg_y + 25), msg['time'], fill='#666', font=msg_text_font)

        draw.text((email_x + 20, msg_y + 55), "Message content here...", fill='#5f6368', font=msg_text_font)
        draw.text((email_x + 20, msg_y + 78), "Lorem ipsum dolor sit amet, consectetur adipiscing...",
                 fill='#5f6368', font=msg_text_font)

    # Solution annotation
    for offset in range(4):
        draw_rounded_rectangle(draw, (email_x - 10 - offset, 110 - offset,
                                     email_x + email_w + 10 + offset, 240 + offset),
                             12, outline='#4caf50', width=1)

    solution_text = "Solution: Latest reply at top"
    solution_bbox = draw.textbbox((0, 0), solution_text, font=solution_font)
    solution_width = solution_bbox[2] - solution_bbox[0]
    draw.text((640 - solution_width // 2, 690), solution_text, fill='#4caf50', font=solution_font)

    # Feature callouts
    features = [
        ("✓ Instant access", 250),
        ("✓ No scrolling", 520),
        ("✓ Auto-reverse", 790)
    ]

    for text, x in features:
        draw.text((x, 735), text, fill=hex_to_rgb(BRAND_COLOR), font=feature_font)

    img.save('/Users/brent.langston/git/replyfirst/images/screenshot-4-after-1280x800.png')
    print("✓ Created: screenshot-4-after-1280x800.png")

# Main execution
if __name__ == '__main__':
    print("Generating ReplyFirst promotional images...\n")

    create_small_promo()
    create_marquee_promo()
    create_screenshot_2()
    create_screenshot_3()
    create_screenshot_4()

    print("\n✓ All promotional images generated successfully!")
    print("\nGenerated files:")
    print("  • promo-small-440x280.png")
    print("  • promo-marquee-1400x560.png")
    print("  • screenshot-2-popup-1280x800.png")
    print("  • screenshot-3-before-1280x800.png")
    print("  • screenshot-4-after-1280x800.png")
