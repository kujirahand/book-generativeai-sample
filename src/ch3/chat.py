# ChatGPTと会話を続ける
import openai, os
# APIキーを環境変数から設定
openai.api_key = os.getenv('OPENAI_API_KEY')

# 会話履歴を管理する変数 --- (*1)
messages = [
    {'role': 'system', 'content': 'あなたは心優しい癒やし系の恋人です。'}
]
# ChatGPTのAPIを呼び出す --- (*2)
def chat_completion(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    # 応答からChatGPTの返答を取り出して返す
    return response.choices[0]['message']['content']

print('ChatGPTと会話します。終了したいときはCtrl+Cを押してください。')
# 連続で会話を繰り返す --- (*3)
while True:
    print('---')
    # ユーザーからの入力を取得 --- (*4)
    prompt = input(">>> ")
    # ユーザーの入力を会話履歴に追加
    messages.append({'role': 'user', 'content': prompt})
    # ChatGPTによる応答を取得 --- (*5)
    response = chat_completion(messages)
    # ChatGPTの応答を表示 --- (*6)
    print("😉ChatGPT:", response)
    # ChatGPTの応答を会話履歴に追加
    messages.append({'role': 'assistant', 'content': response})


