# ReplyFirst - Post-Setup Instructions

## Repository Setup Complete! ✅

The ReplyFirst Chrome extension repository has been successfully created and configured:

**Repository URL:** https://github.com/privatelinkio/replyfirst

**GitHub Pages URL (after first release):** https://privatelinkio.github.io/replyfirst/

## What's Been Done

1. ✅ Git repository initialized and committed
2. ✅ GitHub repository created: `privatelinkio/replyfirst`
3. ✅ Initial commit pushed to main branch
4. ✅ GitHub Actions workflow configured (`.github/workflows/release.yml`)
5. ✅ Documentation created (README.md, RELEASE.md, SECRETS.md, CHANGELOG.md)
6. ✅ .gitignore configured to exclude build artifacts
7. ✅ All extension files committed

## Next Steps

### 1. Generate CRX Private Key (Required for Enterprise Builds)

Generate the signing key for CRX packages:

```bash
cd /Users/brent.langston/git/replyfirst

# Generate 2048-bit RSA private key
openssl genrsa -out replyfirst.pem 2048

# Display the key (you'll need to copy this)
cat replyfirst.pem
```

**IMPORTANT:**
- Backup this key securely (password manager, encrypted vault)
- If lost, you cannot recreate the same extension ID
- Never commit this file to git (it's already in .gitignore)

### 2. Add GitHub Secret (CRX_PRIVATE_KEY)

Add the private key to GitHub repository secrets:

1. Go to: https://github.com/privatelinkio/replyfirst/settings/secrets/actions
2. Click "New repository secret"
3. Name: `CRX_PRIVATE_KEY`
4. Value: Paste the **entire** output from `cat replyfirst.pem` (including BEGIN/END lines)
5. Click "Add secret"

**Without this secret:**
- Only ZIP files will be built (fine for Chrome Web Store)
- CRX files will not be created
- Enterprise auto-update will not be available
- GitHub Pages will not be deployed

### 3. Enable GitHub Pages

Configure GitHub Pages for the updates.xml manifest:

1. Go to: https://github.com/privatelinkio/replyfirst/settings/pages
2. Under "Build and deployment":
   - Source: "GitHub Actions"
3. Save the settings

The workflow will automatically deploy `updates.xml` after the first release.

### 4. Configure Self-Hosted Runner

Ensure your self-hosted runner has the required tools installed:

```bash
# Check prerequisites
node --version    # Should be v18 or later
jq --version      # For JSON manipulation
openssl version   # For key operations
zip --version     # For creating archives

# Install crx tool globally (if not present)
npm install -g crx
```

**Runner Setup (if needed):**
1. Go to: https://github.com/privatelinkio/replyfirst/settings/actions/runners
2. Click "New self-hosted runner"
3. Follow the installation instructions for your platform
4. Start the runner service

### 5. Create Your First Release

Once the above steps are complete, create your first release:

```bash
cd /Users/brent.langston/git/replyfirst

# Create and push version tag
git tag v1.0.0
git push origin v1.0.0
```

**What happens next:**
1. GitHub Actions workflow triggers automatically
2. Workflow updates manifest.json version to `1.0.0`
3. Creates `replyfirst-1.0.0.zip` (for Chrome Web Store)
4. Creates `replyfirst-1.0.0.crx` (for enterprise deployment)
5. Generates `updates.xml` with extension ID
6. Creates GitHub Release with both artifacts
7. Deploys `updates.xml` to GitHub Pages

**Monitor the build:**
- GitHub Actions: https://github.com/privatelinkio/replyfirst/actions

### 6. Verify the Release

After the workflow completes:

1. **Check the release:**
   - Go to: https://github.com/privatelinkio/replyfirst/releases
   - Verify both ZIP and CRX files are attached
   - Note the Extension ID in the release notes

2. **Test the ZIP file:**
   ```bash
   # Download and extract
   unzip replyfirst-1.0.0.zip -d replyfirst-test

   # Load in Chrome
   # 1. Open chrome://extensions
   # 2. Enable "Developer mode"
   # 3. Click "Load unpacked"
   # 4. Select replyfirst-test directory
   ```

3. **Verify GitHub Pages:**
   - Check: https://privatelinkio.github.io/replyfirst/updates.xml
   - Should contain extension ID and CRX download URL

## Optional: Chrome Web Store Submission

To publish on the Chrome Web Store:

1. **Create Developer Account:**
   - Go to: https://chrome.google.com/webstore/devconsole
   - Pay one-time $5 registration fee

2. **Submit Extension:**
   - Click "New Item"
   - Upload `replyfirst-1.0.0.zip` from GitHub release
   - Fill in store listing details:
     - Name: "ReplyFirst"
     - Description: From README.md
     - Screenshots: Create 1280x800 or 640x400 screenshots
     - Category: "Productivity"
     - Language: English
   - Submit for review

3. **Update README:**
   - Add Chrome Web Store link once published
   - Update installation instructions

## Repository Structure

```
replyfirst/
├── .github/
│   └── workflows/
│       └── release.yml           # CI/CD pipeline (self-hosted runners)
├── .gitignore                    # Git ignore rules
├── CHANGELOG.md                   # Version history
├── ICON_DESIGN_SPECS.md          # Icon design documentation
├── IMPLEMENTATION.md              # Technical implementation details
├── INSTALL.md                     # Installation guide
├── README.md                      # Main documentation
├── RELEASE.md                     # Release process guide
├── SECRETS.md                     # GitHub secrets documentation
├── SETUP_INSTRUCTIONS.md         # This file
├── manifest.json                  # Extension manifest (v3)
├── _locales/
│   └── en/
│       └── messages.json         # Internationalization strings
├── images/                        # Icon assets
│   ├── icon-16.png
│   ├── icon-19.png
│   ├── icon-19-on.png
│   ├── icon-38.png
│   ├── icon-38-on.png
│   └── icon-128.png
├── pages/
│   └── popup.html                # Extension popup UI
├── scripts/
│   ├── background.js             # Service worker
│   ├── content.js                # Gmail content script
│   └── popup.js                  # Popup UI logic
└── styles/
    └── content-style.css         # Gmail CSS modifications
```

## Workflow Features

The GitHub Actions workflow includes:

✅ **Self-Hosted Runner Support**
- Uses `runs-on: self-hosted` instead of ubuntu-latest
- Checks for required tools (node, jq, openssl, zip)
- Installs crx package automatically

✅ **Dual Packaging Strategy**
- ZIP: Clean manifest (no update_url) for Chrome Web Store
- CRX: Includes update_url for enterprise auto-updates

✅ **Flexible Triggering**
- Tag push: `git push origin v1.0.0`
- Manual dispatch: Via GitHub Actions UI with version input

✅ **Automated Version Management**
- Extracts version from git tag
- Updates manifest.json automatically
- Creates semantic versioning releases

✅ **Enterprise Features**
- Signs CRX with private key
- Derives extension ID from key
- Generates updates.xml manifest
- Deploys to GitHub Pages

✅ **Security**
- Private key only stored in GitHub secrets
- Key written to disk temporarily during build
- Immediately deleted after signing
- Never exposed in logs

## Troubleshooting

### Workflow Fails: "Prerequisites not satisfied"

Install missing tools on your self-hosted runner:

```bash
# macOS
brew install jq

# Ubuntu/Debian
sudo apt-get install jq openssl zip

# Node.js (if needed)
# Install from https://nodejs.org/
```

### CRX Not Building

Check that `CRX_PRIVATE_KEY` secret is configured:
1. Go to: https://github.com/privatelinkio/replyfirst/settings/secrets/actions
2. Verify `CRX_PRIVATE_KEY` exists
3. If missing, add it following step 2 above

### GitHub Pages 404 Error

After first release, wait a few minutes for Pages to deploy:
- Check: https://github.com/privatelinkio/replyfirst/settings/pages
- Verify "Your site is live at" message appears
- May take 5-10 minutes after first deployment

### Extension ID Changed

If you regenerated the private key:
- Extension ID is derived from the public key
- New key = new extension ID
- Users will see it as a different extension
- **Solution:** Always use the same private key (backup it!)

## Commands Reference

```bash
# Create a new release
git tag v1.0.1
git push origin v1.0.1

# View workflow runs
gh run list --repo privatelinkio/replyfirst

# Watch a workflow run
gh run watch --repo privatelinkio/replyfirst

# View releases
gh release list --repo privatelinkio/replyfirst

# Download release artifacts
gh release download v1.0.0 --repo privatelinkio/replyfirst

# Generate private key
openssl genrsa -out replyfirst.pem 2048

# Verify private key
openssl rsa -in replyfirst.pem -check

# View extension in browser
open chrome://extensions
```

## Support and Resources

- **Repository:** https://github.com/privatelinkio/replyfirst
- **Issues:** https://github.com/privatelinkio/replyfirst/issues
- **Actions:** https://github.com/privatelinkio/replyfirst/actions
- **Releases:** https://github.com/privatelinkio/replyfirst/releases
- **Pages:** https://privatelinkio.github.io/replyfirst/

**Documentation:**
- [RELEASE.md](RELEASE.md) - Detailed release process
- [SECRETS.md](SECRETS.md) - GitHub secrets configuration
- [README.md](README.md) - Extension documentation
- [CHANGELOG.md](CHANGELOG.md) - Version history

## What's Next?

1. ⬜ Generate and configure CRX private key
2. ⬜ Enable GitHub Pages
3. ⬜ Configure self-hosted runner
4. ⬜ Create first release (v1.0.0)
5. ⬜ Test installation from release artifacts
6. ⬜ (Optional) Submit to Chrome Web Store
7. ⬜ (Optional) Set up enterprise deployment

---

**Repository successfully created and configured!**

For questions or issues, refer to the documentation files or open an issue at:
https://github.com/privatelinkio/replyfirst/issues
