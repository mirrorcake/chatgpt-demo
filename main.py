import openai

openai.api_key = "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"


def send(msg):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=msg,
        temperature=0,
        max_tokens=2048,
        top_p=1,
        stop=["【人类】：", "【chatGPT】："],
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response['choices'][0]['text'].strip()


history = ""

while True:
    msg = input("【人类】：")
    if msg == "exit" or msg == "再见":
        break
    msg = history + msg
    res = "【chatGPT】：" + send(msg)
    print(res)
    history += res
