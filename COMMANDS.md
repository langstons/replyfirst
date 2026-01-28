# Quick Command Reference

Fast access to common commands for the ReplyFirst project.

## Initial Setup

```bash
# Generate CRX private key (do this once)
cd /Users/brent.langston/git/replyfirst
openssl genrsa -out replyfirst.pem 2048

# View the key to copy to GitHub secrets
cat replyfirst.pem

# Verify key is valid
openssl rsa -in replyfirst.pem -check
```

## Creating Releases

```bash
# Tag-based release (recommended)
git tag v1.0.0
git push origin v1.0.0

# Watch the workflow run
gh run watch

# List all releases
gh release list

# View specific release
gh release view v1.0.0
```

## Manual Workflow Dispatch

```bash
# Trigger release workflow manually
gh workflow run release.yml -f version=1.0.1

# Or use the GitHub UI:
# https://github.com/privatelinkio/replyfirst/actions/workflows/release.yml
```

## Development

```bash
# Load extension in Chrome for testing
open chrome://extensions

# View manifest
cat manifest.json | jq .

# Check version
cat manifest.json | jq -r .version

# Run in different directory
cd /Users/brent.langston/git/replyfirst
```

## Repository Management

```bash
# View repository
gh repo view privatelinkio/replyfirst

# Open in browser
gh repo view privatelinkio/replyfirst --web

# View issues
gh issue list

# Create issue
gh issue create
```

## GitHub Actions

```bash
# List workflow runs
gh run list

# Watch latest run
gh run watch

# View specific run
gh run view <run-id>

# View workflow logs
gh run view <run-id> --log

# Cancel a run
gh run cancel <run-id>

# Re-run failed jobs
gh run rerun <run-id>
```

## Secrets Management

```bash
# List secrets (names only)
gh secret list

# Set a secret (interactive)
gh secret set CRX_PRIVATE_KEY < replyfirst.pem

# View secrets in browser
open https://github.com/privatelinkio/replyfirst/settings/secrets/actions
```

## GitHub Pages

```bash
# Check Pages status
gh api repos/privatelinkio/replyfirst/pages

# View updates.xml
curl https://privatelinkio.github.io/replyfirst/updates.xml

# Open Pages settings
open https://github.com/privatelinkio/replyfirst/settings/pages
```

## Testing Releases

```bash
# Download latest release
gh release download

# Download specific version
gh release download v1.0.0

# Extract and test ZIP
unzip replyfirst-1.0.0.zip -d test-extension
open chrome://extensions
```

## Checking Prerequisites

```bash
# Check Node.js
node --version

# Check jq
jq --version

# Check openssl
openssl version

# Check zip
zip --version

# Check crx
crx --version || npm install -g crx
```

## Git Operations

```bash
# Check status
git status

# View commits
git log --oneline -10

# View tags
git tag -l

# Delete local tag
git tag -d v1.0.0

# Delete remote tag
git push origin --delete v1.0.0

# Pull latest
git pull
```

## Troubleshooting

```bash
# View workflow file
cat .github/workflows/release.yml

# Check for private key file (should NOT exist in repo)
ls -la *.pem

# Verify .gitignore excludes build artifacts
cat .gitignore

# Check remote
git remote -v

# View GitHub config
gh config list

# Check GitHub authentication
gh auth status
```

## Extension Testing

```bash
# Open Chrome extensions page
open chrome://extensions

# Open Gmail for testing
open https://mail.google.com

# Check Chrome version
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --version
```

## URL Quick Access

```bash
# Open repository
open https://github.com/privatelinkio/replyfirst

# Open Actions
open https://github.com/privatelinkio/replyfirst/actions

# Open Releases
open https://github.com/privatelinkio/replyfirst/releases

# Open Settings
open https://github.com/privatelinkio/replyfirst/settings

# Open Secrets
open https://github.com/privatelinkio/replyfirst/settings/secrets/actions

# Open Pages
open https://github.com/privatelinkio/replyfirst/settings/pages

# View updates.xml
open https://privatelinkio.github.io/replyfirst/updates.xml
```

## Documentation

```bash
# View documentation files
ls -1 *.md

# Read specific doc
cat SETUP_INSTRUCTIONS.md
cat RELEASE.md
cat SECRETS.md

# Edit documentation
code README.md  # VSCode
vim README.md   # Vim
```

## Versioning

```bash
# Current version
cat manifest.json | jq -r .version

# Update version manually (before creating tag)
VERSION=1.0.1
jq --arg v "$VERSION" '.version = $v' manifest.json > manifest.tmp && mv manifest.tmp manifest.json

# Commit version update
git add manifest.json
git commit -m "Bump version to $VERSION"
git push
```

## Build Locally (Testing)

```bash
# Create ZIP manually
VERSION=1.0.0
zip -r "replyfirst-${VERSION}.zip" \
  manifest.json \
  images/ \
  pages/ \
  scripts/ \
  styles/ \
  _locales/ \
  -x "*.DS_Store"

# List ZIP contents
unzip -l replyfirst-1.0.0.zip
```

## Monitoring

```bash
# Watch for new releases
watch -n 30 'gh release list'

# Monitor workflow runs
watch -n 10 'gh run list --limit 5'

# Check GitHub Pages deployment
watch -n 30 'curl -s https://privatelinkio.github.io/replyfirst/updates.xml | grep version'
```

## Cleanup

```bash
# Remove local build artifacts
rm -f *.zip *.crx *.pem

# Clean Git untracked files (careful!)
git clean -fd

# Remove old release downloads
rm -rf replyfirst-*
```

## Self-Hosted Runner

```bash
# Check runner status (if configured on this machine)
cd ~/actions-runner && ./run.sh --check

# View runner logs
tail -f ~/actions-runner/_diag/*.log

# Restart runner
cd ~/actions-runner && ./svc.sh restart
```

## Chrome Web Store

```bash
# Open Chrome Web Store Developer Dashboard
open https://chrome.google.com/webstore/devconsole

# Download current Web Store package for comparison
# (Manual - no CLI available)
```

---

## Most Common Workflow

```bash
# 1. Make changes to extension
# 2. Test locally
# 3. Create release

cd /Users/brent.langston/git/replyfirst

# Commit changes
git add .
git commit -m "Description of changes"
git push

# Create release tag
git tag v1.0.1
git push origin v1.0.1

# Monitor build
gh run watch

# Verify release
gh release view v1.0.1

# Download and test
gh release download v1.0.1
unzip replyfirst-1.0.1.zip -d test
```

---

For detailed explanations, see:
- [SETUP_INSTRUCTIONS.md](SETUP_INSTRUCTIONS.md) - Complete setup guide
- [RELEASE.md](RELEASE.md) - Release process details
- [SECRETS.md](SECRETS.md) - GitHub secrets configuration
- [README.md](README.md) - Extension documentation
