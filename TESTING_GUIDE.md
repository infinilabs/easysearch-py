# Testing Guide

This guide will help you quickly verify the connection status of the Easysearch Python client (both synchronous and asynchronous), as well as how to run the complete test suite.

## 📋 Prerequisites

Before running tests, please ensure:

1. **A Running Easysearch Server**
   - Default address: `https://localhost:9200`
   - Default authentication: `admin` user with corresponding password
   - SSL configuration: Should be enabled (certificate verification is disabled by default in local test examples)

2. **Python Environment**
   - Python 3.6+ is recommended

---

## ⚙️ Installing the Client

Choose the installation method that best fits your use case:

### Method 1: Standard Installation (⭐⭐⭐ Recommended for Quick Testing & Production Use)

The simplest way is to install the released version directly via `pip`:

```bash
# Basic installation (synchronous client)
pip install easysearch

# Install with async support (recommended)
pip install "easysearch[async]"
```

### Method 2: Source Installation (For Development & Running Pytest Tests)

If you have cloned this repository and want to modify code or run low-level unit tests, we recommend installing in editable mode from the project root:

```bash
pip install -e .
# Or with async dependencies:
pip install -e ".[async]"
```

---

## 🚀 Running Basic Tests (Verify Connectivity)

If you have cloned this repository, you can directly run the example scripts in the `examples` directory to verify that the client can communicate with Easysearch normally:

### 1. Test Synchronous Client

```bash
python examples/basic_usage.py
```

**Expected Output:**
```text
Connecting to Easysearch...
✅ Connection successful!
Cluster: easysearch
Version: 2.x.x
...
🎉 All tests passed!
```

### 2. Test Asynchronous Client

```bash
python examples/async_usage.py
```

**Expected Output:**
```text
Testing asynchronous client...
✅ Async connection successful!
Cluster: easysearch
...
🎉 All async tests passed!
```

*(Note: If you haven't cloned the repository, you can create a Python file locally and copy the code from `examples/basic_usage.py` in the repository for testing.)*

---

## 🧪 Running the Full Unit Test Suite (Pytest)

> **Note:** This step is only applicable to users who chose **Method 2 (Source Installation)**.

If you want to run the full unit tests and coverage checks, please ensure you have installed all test dependencies:

```bash
# Install test dependencies
pip install pytest pytest-cov numpy pandas

# Run all tests with verbose output
pytest test_easysearch/ -v

# Run tests for a specific module
pytest test_easysearch/test_serializer.py -v
```

---

## 🔧 Modifying Test Configuration

If your Easysearch server is not running locally, or if you have different credentials, please modify the following connection parameters in your test code:

```python
from easysearch import Easysearch

es = Easysearch(
    ['https://your-host:9200'],                # Update to your actual server address
    http_auth=('your-user', 'your-password'),  # Update to your actual credentials
    use_ssl=True,
    verify_certs=False,                        # Recommended to set True in production with proper CA certificates
    ssl_show_warn=False
)
```

---

## ❓ Frequently Asked Questions (FAQ)

### ❌ Issue 1: `ModuleNotFoundError: No module named 'urllib3'`
**Cause:** Core network dependencies were not installed completely.
**Solution:** Re-run `pip install easysearch` to ensure all dependencies are downloaded properly.

### ❌ Issue 2: `ImportError: cannot import name 'AsyncEasysearch'`
**Cause:** Missing async dependencies (e.g., `aiohttp`).
**Solution:** Run `pip install aiohttp` or use `pip install "easysearch[async]"` to install async support.

### ❌ Issue 3: `ConnectionError: Connection refused`
**Cause:** The server is not running, or the connection address/port is incorrect.
**Solution:**
1. Ensure the Easysearch process is running normally.
2. Verify address connectivity: Run `curl -k https://localhost:9200` in terminal.
3. Check that the `http_auth` credentials in your code are accurate.

### ❌ Issue 4: `SSLError: certificate verify failed`
**Cause:** SSL certificate verification failed.
**Solution:** Example scripts typically configure `verify_certs=False` to ignore self-signed certificates. If errors occur in production, set `verify_certs=True` and provide the correct `ca_certs` path.

---

## 📚 More Information

- [Installation Guide](INSTALL.md)
- [GitHub Repository](https://github.com/infinilabs/easysearch-py)
- [INFINI Easysearch Official Website](https://easysearch.cn)