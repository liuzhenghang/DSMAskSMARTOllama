# DSM Ask Ollama

一个用于解析群晖SMART报告的Flask API服务，通过Ollama API提供分析结果。

## 功能

- 提供 `/askSMART` 接口，接收SMART报告内容
- 使用Ollama分析SMART报告，生成表格总结和健康状态评估
- 自动清理返回内容中的`<think></think>`标签
- 支持通过环境变量配置Ollama服务地址和模型

## 使用方法

### 直接运行

1. 安装依赖:
```
pip install -r requirements.txt
```

2. 设置环境变量(可选):
```
export OLLAMA_BASE_URL=http://your-ollama-server:11434
export OLLAMA_MODEL=your-model-name
```

3. 运行服务:
```
python app.py
```

### 使用Docker

1. 构建并运行:
```
chmod +x build.sh
./build.sh
```

2. 自定义配置(可选):
```
docker run -d -p 3322:3322 \
  -e OLLAMA_BASE_URL=http://your-ollama-server:11434 \
  -e OLLAMA_MODEL=your-model-name \
  dsm-ask-ollama
```

## API接口

### POST /askSMART

请求体:
```json
{
  "content": "SMART报告内容..."
}
```

成功响应:
```json
{
  "response": "分析结果..."
}
```

错误响应:
```json
{
  "error": "错误信息"
}
``` 