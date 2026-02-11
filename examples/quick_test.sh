#!/bin/bash
source venv/bin/activate
pip install pytest pytest-cov requests pyyaml aiohttp --quiet
python test_connection.py
