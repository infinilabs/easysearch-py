# Easysearch Python Client - 示例代码

本目录包含 Easysearch Python 客户端的示例代码和测试脚本。

## 📁 目录结构

```
examples/
├── README.md           # 本文件
├── basic_usage.py      # 基础同步客户端示例
├── async_usage.py      # 异步客户端示例
├── quick_test.sh       # 快速测试脚本
└── run_tests.sh        # 完整测试脚本
```

## 🚀 快速开始

### 1. 安装客户端

**基础安装（同步客户端）：**
```bash
pip install git+https://github.com/infinilabs/easysearch-py.git@v0.1.0
```

**带异步支持的安装：**
```bash
pip install "git+https://github.com/infinilabs/easysearch-py.git@v0.1.0#egg=easysearch[async]"
```

### 2. 配置 Easysearch 服务器

确保你有一个运行的 Easysearch 实例：
- 地址: `https://localhost:9200`
- 用户: `admin`
- 密码: 根据你的配置修改

### 3. 运行示例

#### 基础同步客户端示例

```bash
python examples/basic_usage.py
```

**示例内容：**
- 连接到 Easysearch
- 创建索引和文档
- 搜索文档
- 更新和删除文档
- 批量操作

#### 异步客户端示例

```bash
python examples/async_usage.py
```

**示例内容：**
- 异步连接和操作
- 并发请求
- 异步批量操作

## 📝 修改配置

所有示例默认连接到 `https://localhost:9200`。如果你的配置不同，请修改示例文件中的连接参数：

```python
# 在 basic_usage.py 或 async_usage.py 中修改
es = Easysearch(
    ['https://your-host:9200'],           # 修改地址
    http_auth=('your-user', 'your-pass'), # 修改认证
    use_ssl=True,
    verify_certs=False,  # 生产环境建议改为 True
    ssl_show_warn=False
)
```

## 🧪 测试脚本

### quick_test.sh - 快速测试

快速验证客户端是否正常工作：

```bash
cd examples
./quick_test.sh
```

### run_tests.sh - 完整测试

运行完整的测试套件（需要 pytest）：

```bash
cd examples
./run_tests.sh
```

## 📚 更多示例

### 基础操作

```python
from easysearch import Easysearch

# 创建客户端
es = Easysearch(['http://localhost:9200'])

# 索引文档
es.index(index='test', id=1, body={'message': 'Hello'})

# 搜索
result = es.search(index='test', body={'query': {'match_all': {}}})
print(result['hits']['hits'])

# 获取文档
doc = es.get(index='test', id=1)
print(doc['_source'])

# 删除文档
es.delete(index='test', id=1)
```

### 批量操作

```python
from easysearch.helpers import bulk

actions = [
    {
        '_index': 'test',
        '_id': i,
        '_source': {'message': f'Message {i}'}
    }
    for i in range(100)
]

success, failed = bulk(es, actions)
print(f'成功: {success}, 失败: {failed}')
```

### 异步操作

```python
import asyncio
from easysearch import AsyncEasysearch

async def main():
    es = AsyncEasysearch(['http://localhost:9200'])
    
    # 异步索引
    await es.index(index='test', id=1, body={'message': 'Async'})
    
    # 异步搜索
    result = await es.search(index='test', body={'query': {'match_all': {}}})
    print(result)
    
    await es.close()

asyncio.run(main())
```

## ❓ 常见问题

### Q: ImportError: cannot import name 'AsyncEasysearch'

**A:** 需要安装异步依赖：
```bash
pip install aiohttp
# 或者重新安装
pip install "git+https://github.com/infinilabs/easysearch-py.git@v0.1.0#egg=easysearch[async]"
```

### Q: ConnectionError: Connection refused

**A:** 检查 Easysearch 是否正在运行：
```bash
curl -k https://localhost:9200
```

### Q: SSLError: certificate verify failed

**A:** 测试环境可以禁用证书验证（已在示例中配置）：
```python
es = Easysearch(['https://localhost:9200'], verify_certs=False)
```

## 🔗 相关文档

- [安装指南](../INSTALL.md)
- [测试指南](../TESTING_GUIDE.md)
- [项目 README](../README.rst)
- [GitHub 仓库](https://github.com/infinilabs/easysearch-py)
- [Easysearch 官网](https://easysearch.cn)

## 💡 提示

- 生产环境请使用有效的 SSL 证书并启用 `verify_certs=True`
- 敏感信息（如密码）建议使用环境变量
- 大量数据操作建议使用批量 API (bulk helpers)
- 异步客户端适合高并发场景

## 🤝 贡献

欢迎提交更多示例代码！请通过 Pull Request 贡献你的示例。
