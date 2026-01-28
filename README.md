# ReplyFirst

A Chrome extension that reverses Gmail conversation thread order to show the newest messages first.

## Features

- Reverses Gmail conversation display order using CSS flexbox
- Simple toggle to enable/disable functionality
- Clean, modern user interface
- Works with Gmail's conversation view
- No external dependencies
- Privacy-focused: no tracking or data collection

## Installation

### From Source

1. Clone this repository
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable "Developer mode" in the top right
4. Click "Load unpacked"
5. Select the `replyfirst` directory

## Usage

1. Click the ReplyFirst icon in your Chrome toolbar
2. Enable the toggle switch
3. Open or refresh Gmail
4. Ensure "Conversation View" is enabled in Gmail Settings → General

The extension will automatically reverse the order of messages in your Gmail conversations, showing the newest messages first.

## How It Works

ReplyFirst uses CSS flexbox's `flex-direction: column-reverse` property to reverse the visual order of Gmail conversation threads without modifying the DOM structure. This approach is:

- Lightweight and performant
- Non-invasive to Gmail's functionality
- Easy to toggle on/off

## Installation Options

### Chrome Web Store (Recommended)
*Coming soon* - Install from the Chrome Web Store for automatic updates.

### Manual Installation (Developer Mode)
1. Download the latest `replyfirst-VERSION.zip` from [Releases](https://github.com/privatelinkio/replyfirst/releases)
2. Extract the ZIP file
3. Open Chrome and navigate to `chrome://extensions/`
4. Enable "Developer mode" in the top right
5. Click "Load unpacked"
6. Select the extracted `replyfirst` directory

### Enterprise Deployment
For enterprise environments, download the `replyfirst-VERSION.crx` file and deploy via Chrome enterprise policies:

```json
{
  "ExtensionSettings": {
    "EXTENSION_ID": {
      "installation_mode": "force_installed",
      "update_url": "https://privatelinkio.github.io/replyfirst/updates.xml"
    }
  }
}
```

See the [Release Notes](https://github.com/privatelinkio/replyfirst/releases) for the current extension ID.

## Development

### Project Structure

```
replyfirst/
├── .github/
│   └── workflows/
│       └── release.yml        # CI/CD pipeline
├── manifest.json              # Extension manifest (v3)
├── images/                    # Icon assets
├── pages/
│   └── popup.html            # Extension popup UI
├── scripts/
│   ├── background.js         # Service worker
│   ├── content.js            # Content script for Gmail
│   └── popup.js              # Popup UI logic
├── styles/
│   └── content-style.css     # Gmail conversation reversal CSS
├── _locales/
│   └── en/
│       └── messages.json     # Localization strings
├── README.md                  # This file
├── RELEASE.md                 # Release process documentation
└── CHANGELOG.md               # Version history
```

### Technologies Used

- Manifest V3
- Chrome Extension APIs
- CSS Flexbox
- Vanilla JavaScript
- GitHub Actions (CI/CD)

### Building and Releasing

See [RELEASE.md](RELEASE.md) for detailed instructions on:
- Setting up the build environment
- Generating CRX signing keys
- Creating releases
- Deploying to Chrome Web Store
- Enterprise deployment options

Quick start for creating a release:

```bash
# Create and push a version tag
git tag v1.0.0
git push origin v1.0.0
```

The CI/CD pipeline will automatically build and publish the release.

## Privacy

ReplyFirst:
- Does not collect any user data
- Does not track browsing behavior
- Does not make external network requests
- Only requests `storage` permission for saving user preferences
- Only runs on Gmail pages

## License

MIT License - feel free to use and modify as needed.

## Support

For issues or feature requests, please use the GitHub issue tracker.
