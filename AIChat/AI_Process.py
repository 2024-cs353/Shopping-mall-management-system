import openai
import os

#  设置 OpenAI API 密钥
openai.api_key = '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'

# # 设置代理 URL 和端口
# proxy_url = 'http://127.0.0.1'
# proxy_port = '8080'  # 请将其替换为你自己的端口

# # 设置 http_proxy 和 https_proxy 环境变量
# os.environ['http_proxy'] = f'{proxy_url}:{proxy_port}'
# os.environ['https_proxy'] = f'{proxy_url}:{proxy_port}'


def get_ai_response(prompt):
    try:
        # 使用新的 Completion API 方式
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # 你可以选择 gpt-4 或其他模型
            prompt=prompt,           # 传入的用户提示
            max_tokens=150,          # 最大 token 数量
            temperature=0.7,         # 控制文本的随机性
        )

        # 返回生成的内容
        return response.choices[0].text.strip()

    except Exception as e:
        return f"Error: {str(e)}"


# 示例：调用 GPT-3.5 来回答问题
if __name__ == "__main__":
    prompt = "Explain the process of photosynthesis."
    response = get_ai_response(prompt)
    print("GPT-3.5 Response: ", response)
