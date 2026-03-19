# Installation Guide

This guide explains how to install the Easysearch Python Client. 

## Table of Contents

-[Standard Installation (Recommended)](#standard-installation-recommended)
- [Install Directly from GitHub](#install-directly-from-github)
- [Install from GitHub Releases](#install-from-github-releases)
-[Install from Source (For Developers)](#install-from-source-for-developers)
- [Verify Installation](#verify-installation)
- [Offline Installation](#offline-installation)
- [Troubleshooting](#troubleshooting)

---

## Standard Installation (Recommended)

The easiest and recommended way to install the Easysearch client is via pip from PyPI.

### Basic Installation (Synchronous Client)

```bash
pip install easysearch
```

### Async Installation (Recommended for Asyncio users)

If your application uses `async`/`await`, install the package with the `async` extra to automatically pull in required dependencies like `aiohttp`:

```bash
pip install "easysearch[async]"
```

---

## Install Directly from GitHub

You can install directly from the GitHub repository using pip. This is useful if you need unreleased features, specific bug fixes, or want to test a specific commit.

### Install from Latest Code (main branch)

```bash
pip install git+https://github.com/infinilabs/easysearch-py.git
```

### Install from Specific Version or Branch

You can target a specific release tag or branch by appending `@<TAG_OR_BRANCH>`.

```bash
# Target a specific version tag (e.g., v0.1.0)
pip install git+https://github.com/infinilabs/easysearch-py.git@vX.Y.Z

# Target a specific branch (e.g., develop)
pip install git+https://github.com/infinilabs/easysearch-py.git@develop

# Target a specific commit hash
pip install git+https://github.com/infinilabs/easysearch-py.git@abc1234
```

### Using `requirements.txt`

Add the following to your `requirements.txt`:

```txt
# Latest from main branch
git+https://github.com/infinilabs/easysearch-py.git

# Or specific version tag
git+https://github.com/infinilabs/easysearch-py.git@vX.Y.Z#egg=easysearch
```

---

## Install from GitHub Releases

You can download pre-built packages from the [GitHub Releases](https://github.com/infinilabs/easysearch-py/releases) page.

### Option A: Install Directly from Release URL

You can pass the `.whl` URL directly to pip (replace `X.Y.Z` with the actual version):

```bash
# Install wheel from GitHub Release
pip install https://github.com/infinilabs/easysearch-py/releases/download/vX.Y.Z/easysearch-X.Y.Z-py2.py3-none-any.whl
```

### Option B: Download and Install Locally

1. Visit the[releases page](https://github.com/infinilabs/easysearch-py/releases) and download the `.whl` (wheel) or `.tar.gz` (source) file.
2. Install the downloaded package:

```bash
# Install wheel package (faster)
pip install easysearch-X.Y.Z-py2.py3-none-any.whl

# Or install source package
pip install easysearch-X.Y.Z.tar.gz
```

---

## Install from Source (For Developers)

If you plan to contribute to the project or run tests, you should install it in editable mode:

```bash
# 1. Clone the repository
git clone https://github.com/infinilabs/easysearch-py.git
cd easysearch-py

# 2. Install in development/editable mode
pip install -e .

# 3. (Optional) Install with async and testing dependencies
pip install -e ".[async]"
pip install pytest pytest-cov
```

---

## Verify Installation

After installation, verify that the package is installed correctly in your Python environment:

```bash
python -c "import easysearch; print(f'Easysearch client installed successfully! Version: {easysearch.__version__}')"
```

### Quick Test Connection

```python
from easysearch import Easysearch

# Connect to your Easysearch instance (adjust URL and credentials as needed)
es = Easysearch(['https://localhost:9200'],
    http_auth=('admin', 'password'),
    verify_certs=False, # Disable in dev only
    ssl_show_warn=False
)

# Get cluster information
info = es.info()
print(f"Connected to cluster: {info.get('cluster_name')}")
```

---

## Requirements

- **Python:** 3.6 or higher recommended.
- **Dependencies (Automatically installed by pip):**
  - `urllib3>=1.21.1,<2`
  - `certifi`
  - `aiohttp>=3` (Required only for async support)

---

## Offline Installation

For enterprise environments without internet access:

**Step 1: Download packages on a machine with internet access**
```bash
# Download the package and all its dependencies
pip download easysearch -d /path/to/packages/
```

**Step 2: Transfer to the offline machine**
Copy the `/path/to/packages/` directory to your target offline machine.

**Step 3: Install offline**
```bash
pip install --no-index --find-links=/path/to/packages/ easysearch
```

---

## Troubleshooting

### SSL Certificate Verification Errors (`SSLError`)
If you encounter SSL errors when connecting to a local/testing cluster with self-signed certificates, adjust your connection parameters:

```python
es = Easysearch(
    ['https://localhost:9200'],
    use_ssl=True,
    verify_certs=False,  # Set to True in Production!
    ssl_show_warn=False
)
```

### `ImportError: No module named 'easysearch'`
1. Verify the package is listed: `pip list | grep easysearch`
2. Ensure you're installing into the correct Python environment (Virtualenv/Conda).
3. Check your Python version: `python --version`

### Connection Refused
1. Verify Easysearch is actually running: `curl -k https://localhost:9200`
2. Double-check the host, port, and scheme (`http` vs `https`) in your connection string.

---

## Uninstallation

To remove the Easysearch Python client:

```bash
pip uninstall easysearch
```

---

## Next Steps

- Read the [README](README.rst)
- View usage scripts in the [Examples](examples/) directory
- Report issues or contribute on [GitHub](https://github.com/infinilabs/easysearch-py)