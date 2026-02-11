#!/bin/bash
# 快速测试脚本 - 验证基本功能
cd "$(dirname "$0")"
source ../venv/bin/activate 2>/dev/null || echo "提示: 建议创建虚拟环境"
pip install pytest pytest-cov requests pyyaml aiohttp --quiet
python basic_usage.py
