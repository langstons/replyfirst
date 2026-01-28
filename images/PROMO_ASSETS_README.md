# ReplyFirst Chrome Web Store Promotional Assets

This directory contains all promotional images for the ReplyFirst Chrome extension listing on the Chrome Web Store.

## Brand Identity

- **Brand Color**: Purple (#8B5CF6)
- **Color Palette**:
  - Primary: #8B5CF6
  - Dark: #7C3AED
  - Light: #A78BFA
- **Logo**: List icon with upward arrow (represents reversed conversation order)

## Promotional Images

### 1. Small Promo Tile
- **File**: `promo-small-440x280.png`
- **Dimensions**: 440×280px
- **Purpose**: Small promotional tile for Chrome Web Store sections
- **Design Features**:
  - Purple gradient background
  - ReplyFirst logo centered
  - Clear tagline: "Newest Replies First"
  - "for Gmail" subtitle
  - Clean, minimal design optimized for small display size

### 2. Marquee Promo Tile
- **File**: `promo-marquee-1400x560.png`
- **Dimensions**: 1400×560px
- **Purpose**: Large featured banner for Chrome Web Store homepage
- **Design Features**:
  - Wide banner format with purple gradient
  - "ReplyFirst" branding prominently displayed on left
  - Visual demonstration of reversed email order on right
  - Email conversation preview showing newest reply first
  - Key benefit highlighted: "See newest replies first in Gmail"
  - Bottom tagline: "Never scroll to find the latest message"
  - Professional, eye-catching design

## Screenshots

### 3. Screenshot 2 - Popup Interface
- **File**: `screenshot-2-popup-1280x800.png`
- **Dimensions**: 1280×800px
- **Purpose**: Showcase the extension popup and user interface
- **Design Features**:
  - Clean popup interface with purple gradient header
  - Toggle switch showing active status
  - Clear instructions on how the extension works
  - Annotated with "Simple Toggle Control" callout
  - Demonstrates ease of use

### 4. Screenshot 3 - Before State
- **File**: `screenshot-3-before-1280x800.png`
- **Dimensions**: 1280×800px
- **Purpose**: Illustrate the problem that ReplyFirst solves
- **Design Features**:
  - Gmail conversation in default oldest-first order
  - Latest reply highlighted at bottom with red annotation
  - "Problem: Latest reply at bottom" label
  - Scroll indicator showing user must scroll down
  - Clearly demonstrates the pain point

### 5. Screenshot 4 - After State
- **File**: `screenshot-4-after-1280x800.png`
- **Dimensions**: 1280×800px
- **Purpose**: Show the solution and benefits
- **Design Features**:
  - Gmail conversation with newest-first order
  - "ReplyFirst Active" badge in header
  - Latest reply highlighted at top with green annotation
  - Green checkmark for latest message
  - "Solution: Latest reply at top" label
  - Feature callouts at bottom: "Instant access", "No scrolling", "Auto-reverse"
  - Demonstrates the value proposition

## Design Guidelines

All promotional images follow these design principles:

1. **Consistent Branding**: Purple (#8B5CF6) used throughout all assets
2. **Professional Aesthetic**: Clean, modern design with Gmail-authentic styling
3. **Clear Communication**: Text is readable with high contrast
4. **User-Centered**: Focus on problem-solving and benefits
5. **Visual Hierarchy**: Important information prominently displayed
6. **Accessibility**: High contrast colors for visibility

## Technical Specifications

- **Format**: PNG (24-bit RGB)
- **Color Space**: RGB
- **Compression**: Non-interlaced
- **Suitable For**: Chrome Web Store listing requirements

## Usage

These images are ready to upload to the Chrome Web Store Developer Dashboard:

1. Navigate to your extension's store listing
2. Upload promotional images in the "Store listing" section
3. Use small promo tile for featured sections
4. Use marquee for main banner display
5. Add all screenshots to showcase functionality

## File Sizes

- `promo-small-440x280.png`: ~9.6 KB
- `promo-marquee-1400x560.png`: ~44 KB
- `screenshot-2-popup-1280x800.png`: ~27 KB
- `screenshot-3-before-1280x800.png`: ~52 KB
- `screenshot-4-after-1280x800.png`: ~56 KB

All file sizes are optimized for web delivery while maintaining high visual quality.

## Generation

These images were generated programmatically using Python with PIL/Pillow to ensure:
- Precise dimensions and color accuracy
- Consistent branding across all assets
- Easy regeneration if updates are needed
- Version control and reproducibility

To regenerate images, run:
```bash
python3 generate_promos.py
```
