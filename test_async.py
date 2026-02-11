#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""异步客户端测试"""

import asyncio
from easysearch import AsyncEasysearch

async def test_async_client():
    """测试异步 Easysearch 客户端"""
    
    es = AsyncEasysearch(
        ['https://localhost:9200'],
        http_auth=('admin', '&ltQKnezgClmkgA&=oI%azGE'),
        use_ssl=True,
        verify_certs=False,
        ssl_show_warn=False
    )
    
    try:
        print("正在测试异步客户端...")
        
        # 获取集群信息
        info = await es.info()
        print(f"\n✅ 异步连接成功!")
        print(f"集群: {info['cluster_name']}")
        print(f"版本: {info['version']['number']}")
        
        # 测试异步索引
        print("\n测试异步索引操作...")
        await es.index(
            index='test_async', 
            id=1, 
            body={
                'message': 'Hello from AsyncEasysearch!',
                'timestamp': '2026-02-11',
                'test': True
            }
        )
        print("✅ 异步索引成功")
        
        # 刷新索引
        await es.indices.refresh(index='test_async')
        
        # 测试异步搜索
        result = await es.search(
            index='test_async',
            body={'query': {'match_all': {}}}
        )
        count = result['hits']['total']['value']
        print(f"✅ 异步搜索成功: 找到 {count} 个文档")
        
        # 测试异步获取
        doc = await es.get(index='test_async', id=1)
        print(f"✅ 异步获取文档: {doc['_source']['message']}")
        
        # 清理
        await es.indices.delete(index='test_async', ignore=[404])
        print("✅ 清理测试索引完成")
        
        print("\n🎉 所有异步测试通过!")
        
    except Exception as e:
        print(f"\n❌ 测试失败: {type(e).__name__}: {e}")
        
    finally:
        await es.close()

if __name__ == '__main__':
    asyncio.run(test_async_client())
