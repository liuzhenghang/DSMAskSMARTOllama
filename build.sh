#!/bin/bash

# 构建Docker镜像
docker build -t dsm-ask-ollama .

# 运行容器
# 可以通过环境变量覆盖默认设置
# 例如：docker run -d -p 3322:3322 -e OLLAMA_BASE_URL=http://ollama-server:11434 -e OLLAMA_MODEL=llama2 dsm-ask-ollama
docker run -d -p 3322:3322 dsm-ask-ollama

echo "DSM Ollama 服务已启动，监听端口 3322"