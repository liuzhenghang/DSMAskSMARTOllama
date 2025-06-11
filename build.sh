#!/bin/bash

# 构建Docker镜像
docker build -t dsm-ask-ollama .

# 运行容器
# 可以通过环境变量覆盖默认设置
# 例如：docker run -d -p 3322:3322 -e OLLAMA_BASE_URL=http://ollama-server:11434 -e OLLAMA_MODEL=llama2 dsm-ask-ollama

echo "例如：docker run -d -p 3322:3322 -e OLLAMA_BASE_URL=http://127.0.0.1:11434 -e OLLAMA_MODEL=qwen3:4b dsm-ask-ollama"