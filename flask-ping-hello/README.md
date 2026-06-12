# Flask Ping Hello

一个简单的 Flask 应用，提供两个 GET 端点：`/ping` 返回 "pong"，`/hello` 返回 "Hello World"。

## 安装

确保你已安装 Python 3.9 或更高版本。

1. 克隆或下载此项目。
2. 进入项目目录：`cd flask-ping-hello`
3. 创建虚拟环境（可选但推荐）：
   - Windows: `python -m venv venv`，然后 `venv\Scripts\activate`
   - Linux/Mac: `python3 -m venv venv`，然后 `source venv/bin/activate`
4. 安装依赖：`pip install -r requirements.txt`

## 运行

执行以下命令启动应用：

```bash
python app.py
```

应用将在 http://0.0.0.0:5000 上运行。

可使用浏览器或 curl 访问：
- `curl http://localhost:5000/ping` 返回 "pong"
- `curl http://localhost:5000/hello` 返回 "Hello World"
- 未定义路由返回 404 错误。

## 测试

确保已安装 pytest，然后运行：

```bash
pytest
```

测试会覆盖：
- `/ping` 返回 "pong" 和状态码 200
- `/hello` 返回 "Hello World" 和状态码 200
- 未定义路由（如 `/undefined`）返回 404

测试使用 Flask 的 test client 进行集成测试。
