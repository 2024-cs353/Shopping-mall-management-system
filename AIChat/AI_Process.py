import openai

# 设置 OpenAI API 密钥
openai.api_key = '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'


def get_ai_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()
