from openai import OpenAI
import os

#  设置 OpenAI API 密钥
# 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
openai_api_key = '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'

# # 设置代理 URL 和端口
# proxy_url = 'http://127.0.0.1'
# proxy_port = '8080'  # 请将其替换为你自己的端口

# # 设置 http_proxy 和 https_proxy 环境变量
# os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
# os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'

client = OpenAI(api_key=openai_api_key)


def get_ai_response(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=150,
        top_p=1
    )
    return response.choices[0].message['content'].strip()
