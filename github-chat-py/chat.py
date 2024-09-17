import sys
from openai import OpenAI

# 直接在代码中指定 GitHub 访问令牌
token = "yours'GITHUBTOKEN"
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o"

# 初始化 OpenAI 客户端
client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

# 设置系统角色
messages = [
    {
        "role": "system",
        "content": "You are a helpful assistant.",
    }
]

def get_gpt_response(user_input):
    if user_input.lower() == 'exit':
        return "退出程序"

    # 将用户输入的问题添加到对话历史
    messages.append({
        "role": "user",
        "content": user_input,
    })

    # 发送请求到 GPT-4 模型
    response = client.chat.completions.create(
        messages=messages,
        model=model_name,
        temperature=1.0,
        max_tokens=1000,
        top_p=1.0
    )

    # 获取模型的回答
    assistant_response = response.choices[0].message.content

    # 将模型的回答添加到对话历史
    messages.append({
        "role": "assistant",
        "content": assistant_response,
    })

    return assistant_response
