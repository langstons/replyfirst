# GitHub Secrets Configuration

This document describes the secrets required for the ReplyFirst CI/CD pipeline.

## Required Secrets

### CRX_PRIVATE_KEY (Required for CRX builds)

**Purpose:** RSA private key used to sign the Chrome extension CRX file for enterprise deployment.

**Format:** PEM-encoded RSA private key (2048-bit or higher)

**How to Generate:**

```bash
# Generate a new 2048-bit RSA private key
openssl genrsa -out replyfirst.pem 2048

# View the key (copy the entire output including headers)
cat replyfirst.pem
```

**Expected Output Format:**
```
-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...
(multiple lines of base64-encoded key data)
...
-----END PRIVATE KEY-----
```

**How to Add to GitHub:**

1. Navigate to: https://github.com/privatelinkio/replyfirst/settings/secrets/actions
2. Click "New repository secret"
3. Name: `CRX_PRIVATE_KEY`
4. Value: Paste the **entire** contents of `replyfirst.pem` (including BEGIN/END lines)
5. Click "Add secret"

**Important Notes:**

- **Backup this key securely** - If lost, you cannot recreate the same extension ID
- The extension ID is cryptographically derived from this key
- Regenerating a new key will create a different extension ID
- Store the key in a secure password manager or encrypted vault
- Never commit the `.pem` file to git (it's in `.gitignore`)
- The key is only used during the build process and is never exposed

**What Happens Without This Secret:**

If `CRX_PRIVATE_KEY` is not configured:
- The workflow will still run successfully
- Only the ZIP file will be built (for Chrome Web Store)
- CRX file will not be created
- updates.xml will not be deployed to GitHub Pages
- Enterprise auto-update functionality will not be available

### GITHUB_TOKEN (Auto-Provided)

**Purpose:** Used for creating GitHub releases and deploying to GitHub Pages.

**Configuration:** This secret is automatically provided by GitHub Actions - no manual setup required.

**Permissions Required:**
- `contents: write` - Create releases and upload artifacts
- `pages: write` - Deploy to GitHub Pages
- `id-token: write` - Authentication for Pages deployment

These permissions are configured in the workflow file and do not require manual setup.

## Verifying Secrets

### Check if CRX_PRIVATE_KEY is Configured

The workflow automatically checks for the presence of the secret:

```yaml
- name: Check for CRX secret
  id: check_secret
  run: |
    if [ -n "${{ secrets.CRX_PRIVATE_KEY }}" ]; then
      echo "has_key=true" >> $GITHUB_OUTPUT
    else
      echo "has_key=false" >> $GITHUB_OUTPUT
    fi
```

### Test Your Private Key

Before adding to GitHub, verify the key is valid:

```bash
# Check if the key is valid
openssl rsa -in replyfirst.pem -check

# Extract the public key (for verification)
openssl rsa -in replyfirst.pem -pubout

# View key details
openssl rsa -in replyfirst.pem -text -noout
```

## Extension ID Derivation

The extension ID is derived from the public key using this algorithm:

1. Extract the public key from the private key
2. Convert to DER format
3. Calculate SHA-256 hash
4. Take first 16 bytes
5. Convert to lowercase letters a-p (Chrome's alphabet)

This is handled automatically by the workflow:

```bash
EXTENSION_ID=$(openssl rsa -in replyfirst.pem -pubout -outform DER 2>/dev/null | \
  openssl dgst -sha256 -binary | \
  head -c 16 | \
  xxd -p | \
  sed 's/./\n&/g' | \
  tail -n +2 | \
  while read -r char; do
    dec=$((16#$char))
    printf "\\$(printf '%03o' $((dec + 97)))"
  done)
```

The extension ID is included in the GitHub release notes for reference.

## Security Best Practices

### Key Management

1. **Generate Once:** Create the private key once and reuse it for all releases
2. **Backup Securely:** Store the key in an encrypted vault (e.g., 1Password, Bitwarden)
3. **Limit Access:** Only repository administrators should have access to the key
4. **Never Commit:** Ensure `.pem` files are in `.gitignore`
5. **Rotate Carefully:** If compromised, rotating the key will change the extension ID

### GitHub Secrets Security

- GitHub secrets are encrypted and only exposed to workflow runs
- Secrets are not visible in logs or to unauthorized users
- Secrets are redacted in workflow output
- Only workflows with appropriate permissions can access secrets

### Self-Hosted Runner Considerations

Since this project uses self-hosted runners:

1. **Runner Security:**
   - Ensure the runner machine is secure and up-to-date
   - Limit access to the runner machine
   - Use a dedicated user account for the runner
   - Keep runner software updated

2. **Temporary Files:**
   - The workflow creates `replyfirst.pem` during the build
   - The key is deleted immediately after CRX creation
   - Ensure runner cleanup is configured properly

3. **Build Artifacts:**
   - CRX files are signed but not encrypted
   - Treat release artifacts as public
   - Do not include sensitive data in the extension

## Troubleshooting

### "CRX_PRIVATE_KEY secret not found" Warning

If you see this warning in the workflow logs:
1. Check that the secret is added to the repository
2. Verify the secret name is exactly `CRX_PRIVATE_KEY` (case-sensitive)
3. Ensure you have admin access to the repository
4. Try re-adding the secret

### "Invalid Private Key" Error

If the workflow fails with key validation errors:
1. Verify the key format includes BEGIN/END lines
2. Check for any extra whitespace or newlines
3. Ensure the key is PEM format, not DER
4. Regenerate the key if corrupted:
   ```bash
   openssl genrsa -out replyfirst.pem 2048
   ```

### Extension ID Mismatch

If the extension ID changes between releases:
1. Verify you're using the same private key
2. Check that the key wasn't regenerated
3. Restore the key from backup if lost
4. Update enterprise policies with new extension ID

## Reference Links

- [GitHub Encrypted Secrets Documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets)
- [Chrome Extension CRX Format](https://developer.chrome.com/docs/extensions/mv3/linux_hosting/)
- [OpenSSL RSA Documentation](https://www.openssl.org/docs/man1.1.1/man1/rsa.html)
- [Chrome Enterprise Extension Deployment](https://support.google.com/chrome/a/answer/9296680)
