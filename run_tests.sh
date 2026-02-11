#!/bin/bash
# 测试脚本

# 激活虚拟环境
source venv/bin/activate

echo "==============================================="
echo "安装测试依赖..."
echo "==============================================="
pip install pytest pytest-cov requests pyyaml aiohttp mock coverage --quiet

echo ""
echo "==============================================="
echo "测试 1: 基本连接测试"
echo "==============================================="
python test_connection.py

echo ""
echo "==============================================="
echo "测试 2: 异步客户端测试"
echo "==============================================="
python << 'PYEOF'
import asyncio
from easysearch import AsyncEasysearch

async def test():
    es = AsyncEasysearch(
        ['https://localhost:9200'],
        http_auth=('admin', '&ltQKnezgClmkgA&=oI%azGE'),
        use_ssl=True,
        verify_certs=False,
        ssl_show_warn=False
    )
    try:
        print("连接异步客户端...")
        info = await es.info()
        print(f"✅ 异步连接成功!")
        print(f"集群: {info['cluster_name']}")
        print(f"版本: {info['version']['number']}")
        
        # 测试异步索引
        await es.index(index='test_async', id=1, body={'msg': 'async test'})
        print("✅ 异步索引成功")
        
        # 测试异步搜索
        result = await es.search(index='test_async', body={'query': {'match_all': {}}})
        print(f"✅ 异步搜索成功: {result['hits']['total']['value']} 个文档")
        
        # 清理
        await es.indices.delete(index='test_async', ignore=[404])
        print("✅ 清理完成")
        
    finally:
        await es.close()

asyncio.run(test())
PYEOF

echo ""
echo "==============================================="
echo "测试 3: 单元测试（不需要服务器）"
echo "==============================================="
python -m pytest test_easysearch/test_connection.py -v --tb=short || true

echo ""
echo "==============================================="
echo "测试 4: 客户端单元测试"
echo "==============================================="
python -m pytest test_easysearch/test_client/test_utils.py -v --tb=short || true

echo ""
echo "==============================================="
echo "所有测试完成!"
echo "==============================================="
