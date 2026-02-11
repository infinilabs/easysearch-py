# Installation Guide

This guide explains how to install the Easysearch Python Client.

## Table of Contents

- [Install Directly from GitHub (Easiest)](#install-directly-from-github-easiest)
- [Install from GitHub Releases](#install-from-github-releases)
- [Install from Source](#install-from-source)
- [Install from PyPI](#install-from-pypi)
- [Verify Installation](#verify-installation)

---

## Install Directly from GitHub (Easiest)

You can install directly from GitHub using pip, no need to download files manually!

### Install from Latest Code (main branch)

```bash
pip install git+https://github.com/infinilabs/easysearch-py.git
```

### Install from Specific Version Tag

```bash
# Install version 0.1.0
pip install git+https://github.com/infinilabs/easysearch-py.git@v0.1.0

# Install version 0.2.0
pip install git+https://github.com/infinilabs/easysearch-py.git@v0.2.0
```

### Install from Specific Branch

```bash
# Install from develop branch
pip install git+https://github.com/infinilabs/easysearch-py.git@develop
```

### Install from Specific Commit

```bash
pip install git+https://github.com/infinilabs/easysearch-py.git@abc1234
```

### Using requirements.txt

Add to your `requirements.txt`:

```txt
# Latest from main branch
git+https://github.com/infinilabs/easysearch-py.git

# Or specific version
git+https://github.com/infinilabs/easysearch-py.git@v0.1.0

# Or with egg name for reference
git+https://github.com/infinilabs/easysearch-py.git@v0.1.0#egg=easysearch
```

Then install:
```bash
pip install -r requirements.txt
```

### Advantages

✅ **No manual download needed** - pip handles everything  
✅ **Always up-to-date** - install latest or pin specific versions  
✅ **Works in CI/CD** - perfect for automated deployments  
✅ **No PyPI dependency** - works even if PyPI has issues  
✅ **Easy to upgrade** - just change the version tag

---

## Install from GitHub Releases

You can download pre-built packages from [GitHub Releases](https://github.com/infinilabs/easysearch-py/releases), or install directly from release URLs.

### Option A: Install Directly from Release URL (No Download Needed)

```bash
# Install wheel from GitHub Release (recommended)
pip install https://github.com/infinilabs/easysearch-py/releases/download/v0.1.0/easysearch-0.1.0-py2.py3-none-any.whl

# Or install source package
pip install https://github.com/infinilabs/easysearch-py/releases/download/v0.1.0/easysearch-0.1.0.tar.gz
```

Replace `v0.1.0` and `0.1.0` with the version you want.

### Option B: Download and Install Locally

#### Step 1: Download the Package

Visit the [releases page](https://github.com/infinilabs/easysearch-py/releases) and download either:
- `easysearch-X.Y.Z-py2.py3-none-any.whl` (wheel package, recommended)
- `easysearch-X.Y.Z.tar.gz` (source package)

Replace `X.Y.Z` with the version number (e.g., `0.1.0`).

#### Step 2: Install the Downloaded Package

**Option 1: Install wheel package (faster)**
```bash
pip install easysearch-0.1.0-py2.py3-none-any.whl
```

**Option 2: Install source package**
```bash
pip install easysearch-0.1.0.tar.gz
```

#### Step 3: Verify Checksums (Optional but Recommended)

Download the `SHA256SUMS` file from the same release page:

```bash
# Verify the checksum
sha256sum -c SHA256SUMS
```

---

## Install from Source

Clone the repository and install:

```bash
# Clone the repository
git clone https://github.com/infinilabs/easysearch-py.git
cd easysearch-py

# Install in development mode
pip install -e .

# Or build and install
python -m build
pip install dist/easysearch-*.whl
```

---

## Install from PyPI

> **Note:** PyPI package name may differ due to naming conflicts. Check the latest instructions in the README.

```bash
# When available on PyPI
pip install easysearch-py
```

---

## Verify Installation

After installation, verify that the package is installed correctly:

```bash
python -c "from easysearch import Easysearch; print('Easysearch client installed successfully!')"
```

### Quick Test

```python
from easysearch import Easysearch

# Connect to your Easysearch instance
es = Easysearch(['http://localhost:9200'])

# Get cluster information
info = es.info()
print(info)
```

---

## Requirements

- **Python:** 3.6 or higher (Python 2.7 and 3.4+ are supported, but 3.6+ recommended)
- **Dependencies:**
  - `urllib3>=1.21.1,<2`
  - `certifi`
  - `aiohttp>=3` (for async support, Python 3.6+ only)

Dependencies are automatically installed by pip.

---

## Offline Installation

For environments without internet access:

### Step 1: Download packages on a machine with internet

```bash
# Download the package and all dependencies
pip download easysearch -d /path/to/packages/
```

Or download from GitHub Releases manually.

### Step 2: Transfer to offline machine

Copy the packages directory to your offline machine.

### Step 3: Install offline

```bash
pip install --no-index --find-links=/path/to/packages/ easysearch
```

---

## Troubleshooting

### SSL Certificate Verification Errors

If you encounter SSL certificate errors:

```python
from easysearch import Easysearch

es = Easysearch(
    ['https://localhost:9200'],
    use_ssl=True,
    verify_certs=False,  # Disable certificate verification (development only)
    ssl_show_warn=False
)
```

**Warning:** Only disable certificate verification in development environments.

### ImportError

If you get `ImportError: No module named 'easysearch'`:

1. Verify installation: `pip list | grep easysearch`
2. Check Python version: `python --version`
3. Ensure you're using the correct Python environment

### Connection Refused

If you cannot connect to Easysearch:

1. Verify Easysearch is running: `curl http://localhost:9200`
2. Check the host and port in your connection string
3. Verify firewall settings

---

## Uninstallation

To remove the Easysearch Python client:

```bash
pip uninstall easysearch
```

---

## Next Steps

- Read the [Quick Start Guide](README.rst)
- Check [API Documentation](docs/index.asciidoc)
- View [Examples](examples/)
- Report issues on [GitHub](https://github.com/infinilabs/easysearch-py/issues)
