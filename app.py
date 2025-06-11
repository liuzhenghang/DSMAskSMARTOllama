import os
import re
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# 获取环境变量
OLLAMA_BASE_URL = os.environ.get('OLLAMA_BASE_URL', 'http://127.0.0.1:11434')
OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'llama2')

@app.route('/askSMART', methods=['POST'])
def ask_smart():
    # 获取请求内容
    data = request.json
    if not data or 'content' not in data:
        return jsonify({"error": "必须提供content字段"}), 400

    content = data['content']
    try:
        
        # 构造 Ollama 请求
        prompt = f"这是群晖系统的SMART报告，请翻译成中文，并评估健康状态。\n\n{content}"
        
        # 请求 Ollama API
        response = requests.post(
            f"{OLLAMA_BASE_URL}/api/generate",
            json={
                "model": OLLAMA_MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=300  # 设置超时时间为5分钟
        )
        
        if response.status_code != 200:
            return jsonify({"error": f"Ollama API 请求失败: {response.text}"}), 500
        
        # 获取回答并处理
        answer = response.json().get('response', '')
        
        # 移除 <think>...</think> 标签内的内容
        clean_answer = re.sub(r'<think>.*?</think>', '', answer, flags=re.DOTALL)
        
        return clean_answer
    
    except requests.Timeout:
        return content, 504
    except Exception as e:
        return content, 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3322, debug=False)