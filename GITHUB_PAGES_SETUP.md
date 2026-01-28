# GitHub Pages Setup Instructions

This document explains how to configure GitHub Pages to serve the ReplyFirst marketing website from the `docs/` directory.

## Overview

The ReplyFirst repository uses GitHub Pages for two purposes:

1. **Marketing Website** - Served from `/docs` directory at https://langstons.github.io/replyfirst/
2. **Update Manifest** - The `updates.xml` file for enterprise CRX auto-updates

## Configuration Steps

### Option 1: Using GitHub Settings (Recommended)

1. Go to your GitHub repository: https://github.com/langstons/replyfirst
2. Click on **Settings** tab
3. Scroll down to **Pages** section in the left sidebar
4. Under **Source**, select:
   - **Source**: Deploy from a branch
   - **Branch**: `main`
   - **Folder**: `/docs`
5. Click **Save**

GitHub Pages will automatically deploy the marketing website from the `/docs` directory within a few minutes.

### Option 2: Using GitHub Actions Workflow

If you prefer to use GitHub Actions for deployment, you can modify the existing `.github/workflows/release.yml` to also deploy the docs directory.

The current workflow deploys `updates.xml` to Pages. To also deploy the docs:

1. Update the "Prepare GitHub Pages" step in `.github/workflows/release.yml`:

```yaml
- name: Prepare GitHub Pages
  if: steps.check_secret.outputs.has_key == 'true'
  run: |
    mkdir -p _site
    cp updates.xml _site/
    cp -r docs/* _site/
```

2. Commit and push the workflow changes

**Note**: The GitHub Actions approach requires more setup and may conflict with the branch-based deployment. Using Option 1 (GitHub Settings) is simpler and recommended.

## Verification

After configuring GitHub Pages:

1. Wait 2-5 minutes for initial deployment
2. Visit: https://langstons.github.io/replyfirst/
3. You should see the professional marketing landing page
4. The `updates.xml` will continue to work at: https://langstons.github.io/replyfirst/updates.xml

## Directory Structure

```
replyfirst/
├── docs/                    # GitHub Pages source (marketing website)
│   ├── index.html          # Landing page
│   ├── images/             # Website images
│   └── README.md
├── updates.xml             # Update manifest (root level, also deployed to Pages)
├── .github/
│   └── workflows/
│       └── release.yml     # CI/CD for releases
└── [extension files]       # Chrome extension source code
```

## Important Notes

1. **Separate Concerns**: The marketing website in `/docs` is independent from extension releases
2. **No Build Required**: The HTML is static - no build process needed
3. **Updates**: Changes to `/docs` are automatically deployed when pushed to `main` branch
4. **Existing Workflow**: The release workflow continues to work without modification
5. **Custom Domain**: You can optionally add a custom domain in GitHub Pages settings

## Updating the Website

To update the marketing page:

```bash
# Edit the landing page
vim docs/index.html

# Commit and push
git add docs/
git commit -m "Update marketing page"
git push origin main
```

GitHub Pages will automatically redeploy within 1-2 minutes.

## Troubleshooting

### Site not loading?

1. Check Settings > Pages to ensure source is set to `main` branch and `/docs` folder
2. Look for deployment status in the "Environments" section of your repository
3. Check Actions tab for any failed deployments

### Updates not appearing?

1. Wait 2-3 minutes after pushing changes
2. Clear your browser cache
3. Check the commit hash in the page footer to verify it updated

### 404 errors?

1. Ensure `index.html` exists in `/docs` directory
2. Verify GitHub Pages is enabled in repository settings
3. Check that the repository is public (or you have GitHub Pro for private pages)

## Custom Domain (Optional)

To use a custom domain:

1. Add a `CNAME` file to `/docs` with your domain:
   ```
   replyfirst.yourdomain.com
   ```

2. Configure DNS records with your domain provider:
   ```
   CNAME  replyfirst  langstons.github.io
   ```

3. Update settings in GitHub Pages section to use custom domain

## Security

- **HTTPS**: GitHub Pages automatically serves sites over HTTPS
- **No Secrets**: The marketing site contains no sensitive information
- **Static Content**: All content is static HTML/CSS/images

## Support

For issues with GitHub Pages configuration:
- GitHub Pages Documentation: https://docs.github.com/en/pages
- Repository Issues: https://github.com/langstons/replyfirst/issues
