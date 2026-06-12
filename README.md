# flask-ping-hello

一个简单的 Flask 应用，提供 `/ping` 和 `/hello` 接口。

## 安装

确保已安装 Python 3.6+ 和 pip。

```bash
pip install -r requirements.txt
```

## 运行

```bash
python app.py
```

访问 http://127.0.0.1:5000/ping 返回 `pong`，访问 http://127.0.0.1:5000/hello 返回 `Hello World`。

## 测试

```bash
pytest tests.py -v
```

测试会验证正常请求（状态码200，返回内容正确）和 404 情况。
