#!/usr/bin/env python3
"""
Generate ReplyFirst Chrome Extension Icons
Creates all required icon sizes with inactive and active states
"""

from PIL import Image, ImageDraw
import os

# Color scheme
INACTIVE_COLOR = "#9CA3AF"  # Gray
ACTIVE_GRADIENT_START = "#8B5CF6"  # Purple
ACTIVE_GRADIENT_END = "#7C3AED"  # Darker purple
BACKGROUND = (0, 0, 0, 0)  # Transparent

def create_gradient_vertical(draw, x, y, width, height, color_start, color_end):
    """Create a vertical gradient fill"""
    # Convert hex to RGB
    r1, g1, b1 = int(color_start[1:3], 16), int(color_start[3:5], 16), int(color_start[5:7], 16)
    r2, g2, b2 = int(color_end[1:3], 16), int(color_end[3:5], 16), int(color_end[5:7], 16)

    for i in range(height):
        ratio = i / height
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line([(x, y + i), (x + width - 1, y + i)], fill=(r, g, b, 255))

def hex_to_rgba(hex_color, alpha=255):
    """Convert hex color to RGBA tuple"""
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return (r, g, b, alpha)

def draw_stacked_bars_icon(size, active=False):
    """
    Draw the stacked bars with arrow icon

    Args:
        size: Icon size (16, 19, 38, or 128)
        active: True for active state (purple), False for inactive (gray)
    """
    img = Image.new('RGBA', (size, size), BACKGROUND)
    draw = ImageDraw.Draw(img)

    # Scale factors for different sizes
    if size == 16:
        bar_height = 2
        bar_spacing = 2
        arrow_width = 4
        padding = 2
    elif size in [19, 38]:
        bar_height = int(size * 0.12)  # 2-4px
        bar_spacing = int(size * 0.11)  # 2-4px
        arrow_width = int(size * 0.21)  # 4-8px
        padding = int(size * 0.11)  # 2-4px
    else:  # 128
        bar_height = 16
        bar_spacing = 14
        arrow_width = 26
        padding = 14

    # Calculate positions
    total_bars_height = (bar_height * 3) + (bar_spacing * 2)
    start_y = (size - total_bars_height) // 2

    # Bar positions (3 bars)
    bar_y_positions = [
        start_y,
        start_y + bar_height + bar_spacing,
        start_y + (bar_height + bar_spacing) * 2
    ]

    # Draw the three horizontal bars (email threads)
    bar_width = size - (padding * 2) - arrow_width - (padding // 2)

    if active:
        # Use gradient for active state
        for i, bar_y in enumerate(bar_y_positions):
            # Top bar is emphasized
            if i == 0:
                # Slightly wider or more prominent
                create_gradient_vertical(
                    draw,
                    padding,
                    bar_y,
                    bar_width,
                    bar_height,
                    ACTIVE_GRADIENT_START,
                    ACTIVE_GRADIENT_END
                )
            else:
                # Other bars slightly more transparent
                create_gradient_vertical(
                    draw,
                    padding,
                    bar_y,
                    bar_width,
                    bar_height,
                    ACTIVE_GRADIENT_START,
                    ACTIVE_GRADIENT_END
                )
    else:
        # Solid gray for inactive state
        color = hex_to_rgba(INACTIVE_COLOR)
        for i, bar_y in enumerate(bar_y_positions):
            draw.rectangle(
                [padding, bar_y, padding + bar_width, bar_y + bar_height],
                fill=color
            )

    # Draw upward arrow on the right
    arrow_x = size - padding - arrow_width
    arrow_center_y = size // 2

    if size == 16:
        # Simple arrow for smallest size
        arrow_points = [
            (arrow_x + arrow_width // 2, arrow_center_y - 3),  # Top point
            (arrow_x, arrow_center_y + 1),  # Bottom left
            (arrow_x + arrow_width, arrow_center_y + 1),  # Bottom right
        ]
    else:
        # More detailed arrow for larger sizes
        arrow_tip_y = arrow_center_y - (arrow_width // 2)
        arrow_base_y = arrow_center_y + (arrow_width // 2)
        arrow_shaft_width = max(2, arrow_width // 3)

        # Arrow as polygon (triangle on top, rectangle shaft)
        arrow_points = [
            (arrow_x + arrow_width // 2, arrow_tip_y),  # Tip
            (arrow_x, arrow_tip_y + arrow_width // 2),  # Left wing
            (arrow_x + arrow_width // 2 - arrow_shaft_width // 2, arrow_tip_y + arrow_width // 2),  # Left shaft top
            (arrow_x + arrow_width // 2 - arrow_shaft_width // 2, arrow_base_y),  # Left shaft bottom
            (arrow_x + arrow_width // 2 + arrow_shaft_width // 2, arrow_base_y),  # Right shaft bottom
            (arrow_x + arrow_width // 2 + arrow_shaft_width // 2, arrow_tip_y + arrow_width // 2),  # Right shaft top
            (arrow_x + arrow_width, arrow_tip_y + arrow_width // 2),  # Right wing
        ]

    if active:
        arrow_color = hex_to_rgba(ACTIVE_GRADIENT_END)
    else:
        arrow_color = hex_to_rgba(INACTIVE_COLOR)

    draw.polygon(arrow_points, fill=arrow_color)

    return img

def generate_all_icons(output_dir):
    """Generate all required icon sizes"""

    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Icon specifications: (filename, size, active_state)
    icons = [
        ('icon-16.png', 16, False),
        ('icon-19.png', 19, False),
        ('icon-19-on.png', 19, True),
        ('icon-38.png', 38, False),
        ('icon-38-on.png', 38, True),
        ('icon-128.png', 128, False),
    ]

    for filename, size, active in icons:
        print(f"Generating {filename} ({size}x{size}, {'active' if active else 'inactive'})...")
        icon = draw_stacked_bars_icon(size, active)
        filepath = os.path.join(output_dir, filename)
        icon.save(filepath, 'PNG')
        print(f"  Saved to {filepath}")

    print("\nAll icons generated successfully!")

if __name__ == "__main__":
    output_dir = "/Users/brent.langston/git/replyfirst/images"
    generate_all_icons(output_dir)
