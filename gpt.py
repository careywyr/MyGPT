import openai
from typing import List
import os


# 定义ModelInput类
class ModelInput:
    def __init__(
            self,
            prompt: str,
            max_tokens: int = 1024,
            temperature: float = 0.5,
            n: int = 1,
            stop: List[str] = None,
            frequency_penalty: float = 0.0,
            presence_penalty: float = 0.0,
            best_of: int = 1,
    ):
        self.prompt = prompt
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.n = n
        self.stop = stop or []
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.best_of = best_of


# 定义ModelOutput类
class ModelOutput:
    def __init__(
            self,
            id: str,
            object: str,
            created: int,
            model: str,
            choices: List[dict],
    ):
        self.id = id
        self.object = object
        self.created = created
        self.model = model
        self.choices = choices


# 生成回复的方法
def generate_reply(prompt: str, chat_history: list) -> str:
    openai.api_key = os.getenv('OPENAI_TOKEN')
    # 将聊天历史记录与当前回复消息组合成prompt
    prompt = f"{chat_history}\nUser: {prompt}\nAI:"
    print(prompt)
    # 实例化ModelInput类
    model_input = ModelInput(
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        n=1,
        stop=["\nUser:", "\nAI:"],
        frequency_penalty=0.0,
        presence_penalty=0.0,
        best_of=1,
    )

    # 调用API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=model_input.prompt,
        max_tokens=model_input.max_tokens,
        temperature=model_input.temperature,
        n=model_input.n,
        stop=model_input.stop,
        frequency_penalty=model_input.frequency_penalty,
        presence_penalty=model_input.presence_penalty,
        best_of=model_input.best_of,
    )

    # 解析响应
    model_output = ModelOutput(
        id=response["id"],
        object=response["object"],
        created=response["created"],
        model=response["model"],
        choices=response["choices"],
    )

    # 提取生成的文本
    generated_text = model_output.choices[0]["text"]

    return generated_text.strip()


# 定义一个用于获取聊天历史记录的方法
def get_chat_history():
    # 此处返回一个字符串列表，包含聊天历史记录中的所有消息
    return ["Hi, how are you?", "I'm fine, thanks. How about you?", "I'm doing well, thanks. What about you?", "I'm sorry to hear that you're busy today. I hope you're still able to get everything done that you need to."]


# 测试生成回复的方法
# chat_history = get_chat_history()
# user_input = "guess their names, A.诺诺, B. 可可, C.垃圾. choose two of options"
# generated_reply = generate_reply(user_input, chat_history)
# print("Generated reply:", generated_reply)
