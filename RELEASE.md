# Release Process

This document describes the release process for ReplyFirst Chrome extension.

## Prerequisites

### Self-Hosted Runner Requirements

The GitHub Actions workflow requires a self-hosted runner with the following tools installed:

- **Node.js** (v18 or later) - For running build scripts
- **jq** - For JSON manipulation in scripts
- **openssl** - For CRX signing and extension ID generation
- **zip** - For creating Chrome Web Store packages
- **crx** (npm package) - Installed automatically by workflow: `npm install -g crx`

### GitHub Secrets

The following secrets must be configured in the GitHub repository:

1. **CRX_PRIVATE_KEY** (Required for enterprise CRX builds)
   - RSA private key in PEM format for signing the CRX file
   - See "Generating CRX Private Key" section below
   - Without this secret, only ZIP files will be built

2. **GITHUB_TOKEN** (Auto-provided)
   - Automatically provided by GitHub Actions
   - Used for creating releases and deploying to GitHub Pages

## Generating CRX Private Key

The CRX private key is used to sign the extension for enterprise deployment. This key must be kept secure and should only be generated once.

### Generate the key:

```bash
# Generate a new RSA private key
openssl genrsa -out replyfirst.pem 2048

# Display the private key (copy this to GitHub secrets)
cat replyfirst.pem
```

### Add to GitHub Secrets:

1. Go to: https://github.com/privatelinkio/replyfirst/settings/secrets/actions
2. Click "New repository secret"
3. Name: `CRX_PRIVATE_KEY`
4. Value: Paste the entire contents of `replyfirst.pem`
5. Click "Add secret"

**IMPORTANT:**
- Keep this key secure and backed up
- The extension ID is derived from this key
- If you lose the key and generate a new one, the extension ID will change
- Never commit the `.pem` file to git (it's in `.gitignore`)

## Release Methods

### Method 1: Tag-Based Release (Recommended)

Create a git tag to trigger the release:

```bash
# Create and push a version tag
git tag v1.0.0
git push origin v1.0.0
```

The workflow will automatically:
- Extract version from the tag (removes 'v' prefix)
- Update manifest.json version
- Build ZIP and CRX files
- Create GitHub Release
- Deploy updates.xml to GitHub Pages

### Method 2: Manual Workflow Dispatch

Trigger a release manually from GitHub Actions:

1. Go to: https://github.com/privatelinkio/replyfirst/actions/workflows/release.yml
2. Click "Run workflow"
3. Enter version number (e.g., `1.0.0`)
4. Click "Run workflow"

This method is useful for:
- Testing the release process
- Creating releases without pushing tags
- Re-releasing a version with fixes

## Release Checklist

### Pre-Release

- [ ] Update version in `manifest.json` locally (will be overwritten by workflow)
- [ ] Update `CHANGELOG.md` with new version changes
- [ ] Test extension locally in Chrome
- [ ] Test in Gmail with conversation view enabled
- [ ] Verify all icons display correctly
- [ ] Check console for errors
- [ ] Test toggle on/off functionality

### Release

- [ ] Commit all changes to main branch
- [ ] Create version tag: `git tag v1.0.0`
- [ ] Push tag: `git push origin v1.0.0`
- [ ] Monitor GitHub Actions workflow
- [ ] Verify release artifacts (ZIP and CRX)
- [ ] Test manual installation from ZIP
- [ ] Verify GitHub Pages updates.xml is deployed

### Post-Release

- [ ] Download and test the released ZIP file
- [ ] Verify extension ID in release notes (if CRX built)
- [ ] Update Chrome Web Store listing (if published there)
- [ ] Announce release (if applicable)
- [ ] Document any breaking changes

## Build Outputs

Each release produces the following artifacts:

### 1. Chrome Web Store ZIP (`replyfirst-VERSION.zip`)
- Contains extension files without `update_url`
- Used for Chrome Web Store submission
- Can be manually installed in developer mode

### 2. Enterprise CRX (`replyfirst-VERSION.crx`)
- Signed package with `update_url` pointing to GitHub Pages
- Used for enterprise deployment via policy
- Enables automatic updates from GitHub releases
- Only built if `CRX_PRIVATE_KEY` secret is configured

### 3. Updates XML (`updates.xml`)
- Deployed to GitHub Pages at: https://privatelinkio.github.io/replyfirst/updates.xml
- Contains latest version and CRX download URL
- Used by Chrome for auto-updating enterprise installations
- Only deployed if CRX is built

## Deployment Methods

### Chrome Web Store

1. Download `replyfirst-VERSION.zip` from GitHub release
2. Go to [Chrome Web Store Developer Dashboard](https://chrome.google.com/webstore/devconsole)
3. Upload new ZIP file
4. Update store listing if needed
5. Submit for review

### Enterprise Deployment

Deploy the CRX file via Chrome enterprise policies:

```json
{
  "ExtensionSettings": {
    "EXTENSION_ID_HERE": {
      "installation_mode": "force_installed",
      "update_url": "https://privatelinkio.github.io/replyfirst/updates.xml"
    }
  }
}
```

Replace `EXTENSION_ID_HERE` with the extension ID from the release notes.

### Manual Installation

Users can install the extension manually:

1. Download `replyfirst-VERSION.zip`
2. Extract the ZIP file
3. Open `chrome://extensions`
4. Enable "Developer mode"
5. Click "Load unpacked"
6. Select the extracted folder

## Versioning

ReplyFirst follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version: Incompatible API changes or major rewrites
- **MINOR** version: New functionality in a backwards-compatible manner
- **PATCH** version: Backwards-compatible bug fixes

Example: `1.2.3` = Major.Minor.Patch

## Troubleshooting

### Workflow Fails on Self-Hosted Runner

Check that all prerequisites are installed:

```bash
node --version  # Should be v18+
jq --version
openssl version
zip --version
crx --version  # May need: npm install -g crx
```

### CRX Not Building

- Verify `CRX_PRIVATE_KEY` secret is configured
- Check workflow logs for "has_key=false" message
- Ensure PEM key is valid: `openssl rsa -in replyfirst.pem -check`

### GitHub Pages Not Deploying

- Verify repository has Pages enabled
- Check that workflow has `pages: write` permission
- Ensure `deploy-pages` job runs successfully
- GitHub Pages URL: https://privatelinkio.github.io/replyfirst/

### Extension ID Changed

If you regenerated the private key, the extension ID will change. This means:
- Enterprise deployments need to update their policy
- Users will see it as a different extension
- Previous auto-updates will not work

**Solution:** Always backup and reuse the same private key.

## Support

For issues with the release process:
- Check [GitHub Actions logs](https://github.com/privatelinkio/replyfirst/actions)
- Review workflow file: `.github/workflows/release.yml`
- Open an issue: https://github.com/privatelinkio/replyfirst/issues
