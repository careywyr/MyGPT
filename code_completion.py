# -*- coding: utf-8 -*-
"""
@file    : code_completion.py
@date    : 2023-03-21
@author  : carey
"""
import requests
import json
import os

# 请求的 URL
url = "https://api.openai.com/v1/completions"

# 请求参数
payload = {
    "model": "code-davinci-002",
    "prompt": "使用python实现一个简单的http服务器",
    "max_tokens": 200,
    "n": 1,
    "stream": False,
    "logprobs": None,
    "stop": "\n"
}

# 设置请求头，包括 API 密钥
key = os.getenv('OPENAI_TOKEN')
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + key
}

# 发送 POST 请求
response = requests.post(url, headers=headers, data=json.dumps(payload))

# 解析返回结果
if response.status_code == 200:
    result = json.loads(response.text)
    print(result)
else:
    print("请求失败，错误码：", response.status_code)
