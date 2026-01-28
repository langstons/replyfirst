# Changelog

All notable changes to the ReplyFirst Chrome extension will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release preparation
- CI/CD pipeline with self-hosted runners
- Dual packaging strategy (ZIP for Chrome Web Store, CRX for enterprise)
- Automated GitHub Pages deployment for update manifest

## [1.0.0] - TBD

### Added
- Reverse Gmail conversation thread order to show newest messages first
- Simple toggle to enable/disable functionality
- Clean, modern user interface matching Gmail aesthetics
- CSS-based flexbox reversal (non-invasive, performant)
- Storage API for persisting user preferences
- Internationalization support (i18n) with English locale
- Icon set with multiple sizes (16px, 19px, 38px, 128px)
- Manifest V3 compliance
- Content Security Policy implementation

### Features
- Works with Gmail's conversation view
- No external dependencies
- Privacy-focused: no tracking or data collection
- Only requests minimal permissions (storage)
- Only runs on Gmail pages (https://mail.google.com/*)
- Service worker background script
- Content script with CSS injection

### Technical
- Manifest V3 architecture
- Vanilla JavaScript (no frameworks)
- CSS Flexbox for visual reversal
- Web-accessible resources for Gmail integration
- All frames support for Gmail's iframe structure

[Unreleased]: https://github.com/langstons/replyfirst/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/langstons/replyfirst/releases/tag/v1.0.0
