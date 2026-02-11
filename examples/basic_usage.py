#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  Copyright 2021-2026 INFINI Labs
#
#  This file is part of Easysearch Python Client, which is derived from
#  Elasticsearch Python Client.
#  Copyright 2013-2020 Elasticsearch B.V.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""
简单的连接测试脚本
用于验证 Easysearch Python 客户端与本地 Easysearch 服务的连接
"""

from easysearch import Easysearch

def test_connection():
    """测试与本地 Easysearch 的连接"""
    
    # 连接到本地 Easysearch (HTTPS + 认证)
    es = Easysearch(
        ['https://localhost:9200'],
        http_auth=('admin', '&ltQKnezgClmkgA&=oI%azGE'),
        use_ssl=True,
        verify_certs=False,  # 跳过证书验证（开发环境）
        ssl_show_warn=False  # 不显示 SSL 警告
    )
    
    print("正在连接 Easysearch...")
    
    try:
        # 获取集群信息
        info = es.info()
        
        print("\n✅ 连接成功!")
        print("\n集群信息:")
        print(f"  名称: {info.get('cluster_name', 'N/A')}")
        print(f"  版本: {info['version']['number']}")
        print(f"  Lucene: {info['version'].get('lucene_version', 'N/A')}")
        
        # 获取集群健康状态
        health = es.cluster.health()
        print(f"\n集群健康:")
        print(f"  状态: {health['status']}")
        print(f"  节点数: {health['number_of_nodes']}")
        print(f"  数据节点: {health['number_of_data_nodes']}")
        
        # 测试索引操作
        print("\n测试索引操作...")
        test_index = 'test_easysearch_py'
        
        # 创建测试文档
        doc = {
            'message': 'Hello from Easysearch Python Client!',
            'timestamp': '2026-02-11',
            'version': '1.0.0'
        }
        
        result = es.index(index=test_index, id=1, body=doc)
        print(f"  索引文档: {result['result']}")
        
        # 刷新索引
        es.indices.refresh(index=test_index)
        
        # 搜索文档
        search_result = es.search(
            index=test_index,
            body={'query': {'match_all': {}}}
        )
        
        print(f"  搜索结果: 找到 {search_result['hits']['total']['value']} 个文档")
        
        # 获取文档
        get_result = es.get(index=test_index, id=1)
        print(f"  获取文档: {get_result['_source']['message']}")
        
        # 清理测试索引
        es.indices.delete(index=test_index, ignore=[404])
        print(f"  清理测试索引: 完成")
        
        print("\n🎉 所有测试通过!")
        return True
        
    except Exception as e:
        print(f"\n❌ 连接失败!")
        print(f"错误: {type(e).__name__}: {e}")
        print("\n请检查:")
        print("  1. Easysearch 服务是否正在运行")
        print("  2. 连接地址是否正确 (默认: localhost:9200)")
        print("  3. 是否需要认证")
        return False

if __name__ == '__main__':
    test_connection()
