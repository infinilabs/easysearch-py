# 测试指南

本目录包含测试脚本，用于验证 Easysearch Python 客户端的功能。

## 前置要求

1. **运行的 Easysearch 服务器**
   - 地址: https://localhost:9200
   - 认证: admin 用户及密码
   - SSL: 启用（测试中禁用证书验证）

2. **安装客户端**

### 基础安装（同步客户端）

```bash
pip install git+https://github.com/infinilabs/easysearch-py.git@v0.1.0
```

### 带异步支持的安装

```bash
# 方式 1: 使用 [async] extra
pip install "git+https://github.com/infinilabs/easysearch-py.git@v0.1.0#egg=easysearch[async]"

# 方式 2: 手动安装依赖
pip install git+https://github.com/infinilabs/easysearch-py.git@v0.1.0
pip install aiohttp
```

## 运行测试

### 1. 测试同步客户端

```bash
python examples/basic_usage.py
```

**预期输出：**
```
正在连接到 Easysearch...
✅ 连接成功!
集群: easysearch
版本: 2.0.3
...
🎉 所有测试通过!
```

### 2. 测试异步客户端

```bash
python examples/async_usage.py
```

**预期输出：**
```
正在测试异步客户端...
✅ 异步连接成功!
集群: easysearch
版本: 2.0.3
...
🎉 所有异步测试通过!
```

## 常见问题

### 问题 1: ModuleNotFoundError: No module named 'urllib3'

**原因：** 基础依赖未安装

**解决：**
```bash
pip install urllib3 certifi
# 或者重新安装客户端
pip install git+https://github.com/infinilabs/easysearch-py.git@v0.1.0
```

### 问题 2: ImportError: cannot import name 'AsyncEasysearch'

**原因：** 缺少异步依赖 aiohttp

**解决：**
```bash
pip install aiohttp
# 或者使用 async extra 重新安装
pip install "git+https://github.com/infinilabs/easysearch-py.git@v0.1.0#egg=easysearch[async]"
```

### 问题 3: ConnectionError: Connection refused

**原因：** Easysearch 服务器未运行或地址不正确

**解决：**
1. 确保 Easysearch 正在运行
2. 验证地址：`curl -k https://localhost:9200`
3. 检查认证信息是否正确

### 问题 4: SSLError: certificate verify failed

**原因：** SSL 证书验证失败

**解决：**
- 测试脚本已禁用证书验证 (`verify_certs=False`)
- 生产环境请使用有效证书或配置 CA 证书

## 修改测试配置

如果你的 Easysearch 服务器配置不同，请修改测试脚本中的连接参数：

```python
es = Easysearch(
    ['https://your-host:9200'],  # 修改地址
    http_auth=('your-user', 'your-password'),  # 修改认证
    use_ssl=True,
    verify_certs=False,  # 生产环境建议改为 True
    ssl_show_warn=False
)
```

## 完整测试套件

要运行完整的测试套件（需要 pytest）：

```bash
# 安装测试依赖
pip install -e .
pip install pytest pytest-cov numpy pandas

# 运行所有测试
pytest test_easysearch/ -v

# 运行特定测试
pytest test_easysearch/test_serializer.py -v
pytest test_easysearch/test_connection_pool.py -v
```

## 更多信息

- [安装指南](INSTALL.md)
- [GitHub 仓库](https://github.com/infinilabs/easysearch-py)
- [Easysearch 官网](https://easysearch.cn)
