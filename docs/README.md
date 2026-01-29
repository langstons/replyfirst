# ReplyFirst Marketing Page

This directory contains the GitHub Pages marketing website for ReplyFirst.

## Live Site

Visit: https://privatelink.io/

## Structure

```
docs/
├── index.html          # Main marketing landing page
├── images/             # Image assets for the website
│   ├── icon-128.png
│   ├── store-screenshot-1280x800.png
│   ├── promo-marquee-1400x560.png
│   ├── screenshot-2-popup-1280x800.png
│   ├── screenshot-3-before-1280x800.png
│   └── screenshot-4-after-1280x800.png
└── README.md          # This file
```

## Features

- Responsive single-page design
- Purple gradient branding (#8B5CF6)
- SEO optimized with meta tags
- Open Graph and Twitter Card support
- Mobile-friendly layout
- Fast loading with inline CSS
- Accessible HTML5 semantic structure

## Development

To test locally, simply open `index.html` in a browser or use a local server:

```bash
# Using Python
cd docs
python -m http.server 8000

# Using Node.js
npx http-server docs -p 8000
```

Then visit: http://localhost:8000

## Deployment

This site is automatically served by GitHub Pages from the `/docs` directory on the `main` branch.

No build process is required - GitHub Pages serves the static HTML directly.

## Updates

To update the marketing page:

1. Edit `docs/index.html`
2. Commit and push to the `main` branch
3. Changes will appear at https://privatelink.io/ within minutes

## Image Assets

Images are copied from the `/images` directory in the repository root. To update:

```bash
# From repository root
cp images/[filename].png docs/images/
```

## Notes

- The `docs/` directory is separate from the extension release artifacts
- The existing `updates.xml` at the repository root is not affected
- GitHub Actions workflows for releases continue to work independently
