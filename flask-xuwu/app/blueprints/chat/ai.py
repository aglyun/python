import openai

key = "你chatGPT的秘钥"
openai.api_key = key


# 默认对话模式机器人
class ChatGPT():
    def __init__(self):
        self.lun = []    # 用于存储话轮
        self.text = ""   # 问题

    def ai(self, msg):
        model = "text-davinci-003"
        print("等待ai回答...")
        prompt = self.text + msg  # 拼接问题
        try:
            completions = openai.Completion.create(engine=model, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.9)
            message = completions.choices[0].text
            return message
        except Exception as e:
            return e

    def session_chat(self, msg):
        s = self.ai(msg)
        self.lun += [msg] + [s]
        self.text = " ".join(self.lun)
        self.text = self.text.replace('\n', '')
        # print('问题和答案:', self.text, len(self.lun))
        if len(self.lun) >= 10:
            del self.lun[:6]
        return s

    # 普通模式
    def chat_gpt(self, msg):
        # 机器人模型
        model = "text-davinci-003"
        print("等待ai回答...")
        try:
            completions = openai.Completion.create(engine=model, prompt=msg, max_tokens=1024, n=1, stop=None, temperature=0.9)
            message = completions.choices[0].text
            return message
        except Exception as e:
            return e

    def __del__(self):
        print("我被销毁了")


if __name__ == '__main__':
    chat = ChatGPT()
    # s = chat.session_chat("消息")   # 会话模式
    # s = chat.chat_gpt("消息")      # 普通模式
    while True:
        i = input("你说：")
        s = chat.session_chat(i)
        print("ChatGPT:", s)


