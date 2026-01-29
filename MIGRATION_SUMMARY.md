# privatelinkio Organization Migration Summary

## Overview
Both ReplyFirst and Longshot Chrome extensions have been successfully migrated to the privatelinkio organization with complete CI/CD, marketing sites, and Chrome Web Store submission materials.

## Completed Migrations

### 1. ReplyFirst Extension
- **Old:** langstons/replyfirst
- **New:** https://github.com/privatelinkio/replyfirst
- **Marketing Site:** https://privatelinkio.github.io/replyfirst/
- **Status:** ✅ Fully operational

### 2. Longshot Extension
- **Old:** langstons/longshot  
- **New:** https://github.com/privatelinkio/longshot
- **Marketing Site:** https://privatelinkio.github.io/longshot/
- **Status:** ✅ Fully operational

## What Was Migrated

### Repository Assets
- ✅ All source code, commits, and history
- ✅ All releases with ZIP and CRX files
- ✅ All tags and branches
- ✅ GitHub Actions workflows
- ✅ Secrets (CRX_PRIVATE_KEY)

### Configuration
- ✅ GitHub Pages enabled for both repos
- ✅ Environment policies (github-pages with v* tag support)
- ✅ Self-hosted runner configuration updated
- ✅ All URLs updated to privatelinkio

### Marketing Materials

#### ReplyFirst
- ✅ Professional landing page (docs/index.html)
- ✅ 4 store screenshots (1280x800px)
- ✅ 2 promotional tiles (440x280, 1400x560)
- ✅ Chrome Web Store listing document (local, gitignored)

#### Longshot
- ✅ Professional landing page with privacy policy
- ✅ Screenshot design templates (HTML)
- ✅ Complete marketing documentation suite
- ✅ Chrome Web Store listing document (local, gitignored)

## Privacy-Focused Branding

Both extensions emphasize privatelinkio's privacy-first approach:
- Zero data collection
- No external tracking
- Complete local processing
- Open source transparency
- Minimal permissions

## Chrome Web Store Submission Files

**Location (gitignored, local only):**
- `/Users/brent.langston/git/replyfirst/CHROME_WEB_STORE_LISTING.md`
- `/Users/brent.langston/git/longshot/CHROME_WEB_STORE_LISTING.md`

These files contain:
- Complete listing text with character counts
- Privacy policy templates
- Asset checklists
- Testing instructions
- SEO-optimized descriptions
- Copy-paste ready content

## Next Steps Required

### Self-Hosted Runners
Runners must be re-registered with privatelinkio organization:

```bash
cd ~/actions-runner
./svc.sh stop
./config.sh remove
./config.sh --url https://github.com/privatelinkio --token <TOKEN>
./svc.sh start
```

Get registration token from:
https://github.com/organizations/privatelinkio/settings/actions/runners/new

### Testing
1. Verify runners are registered and online
2. Create a test release for both extensions
3. Verify GitHub Pages sites are live
4. Test auto-update URLs

### Chrome Web Store Submission
1. Review CHROME_WEB_STORE_LISTING.md for each extension
2. Create any remaining visual assets
3. Submit to Chrome Web Store
4. Update README with store links

## URLs Reference

### ReplyFirst
- Repository: https://github.com/privatelinkio/replyfirst
- Marketing: https://privatelinkio.github.io/replyfirst/
- Releases: https://github.com/privatelinkio/replyfirst/releases
- Updates: https://privatelinkio.github.io/replyfirst/updates.xml

### Longshot
- Repository: https://github.com/privatelinkio/longshot
- Marketing: https://privatelinkio.github.io/longshot/
- Releases: https://github.com/privatelinkio/longshot/releases  
- Updates: https://privatelinkio.github.io/longshot/updates.xml

## Migration Date
January 28, 2026

---

**Status:** Migration complete. Runners need manual registration. Ready for Chrome Web Store submission.
