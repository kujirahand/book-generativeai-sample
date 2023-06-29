# ChatCompletionを使ったサイコロ
import os, openai
# APIキーを環境変数から設定
openai.api_key = os.getenv('OPENAI_API_KEY')

# ChatGPTのAPIを呼び出す --- (*1)
def chat_completion(messages, temperature=1.0):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=temperature,
    )
    # 応答からChatGPTの返答を取り出す
    content = response.choices[0]['message']['content']
    return content

if __name__ == '__main__':
    # 詳細なパラメータを指定 --- (*2)
    messages = [
        {'role': 'system', 'content': 'あなたは6面体のサイコロです。'},
        {'role': 'user', 'content': 'サイコロを振ってください。'},
    ]
    # APIを呼び出す --- (*3)
    res = chat_completion(messages, temperature=1.5)
    # 結果を出力 --- (*4)
    print(res)

