# 注文テキストの中にある「料理名」と「配達時間」を認識させる
import openai, json

# 注文テキストを以下に指定 --- (*1)
order_text = 'お昼にチーズバーガーが食べたい。よろしく。'
# order_text = '19:00にトマトパスタを注文したいのでお願いします。'

# ChatGPTを呼び出すためのメッセージを構築 --- (*2)
messages = [
    {
        'role': 'system', # システムの役割を指定
        'content': 'あなたはデリバリーで料理の注文を受ける優秀なウェイトレスです。'
    },
    {
        'role': 'user', 
        'content': order_text
    }
]
# 関数の定義 - 抽出したい情報を指定 --- (*3)
functions = [ # 複数の関数が指定可能
    {
        # 関数の名前と説明を指定 --- (*4)
        'name': 'order_menu',
        'description': '料理を注文する',
        # どんな情報が必要かパラメータを指定 --- (*5)
        'parameters': {
            'type': 'object',
            'properties': {
                # 料理名と配達時間の詳細を指定 --- (*6)
                'menu': {
                    'type': 'string',
                    'description': '料理名'
                },
                'time': {
                    'type': 'string', 
                    'format': 'time', 
                    'description': '配達時間'
                }
            }
        }
    }
]

# 料理を注文するダミー関数 --- (*7)
def order(menu, time):
    print('# 厨房サーバーに注文を出しました。')
    print(f'- 料理名:{menu}\n- 配達時間:{time}\n')
    return f'注文を正しく承りました。{time}に配達します。'

# 料理の注文ボットを実行する関数 --- (*8)
def call_order_bot(messages, functions=None, debug=False):
    # APIを呼び出す --- (*9)
    model = 'gpt-3.5-turbo-0613'
    if functions is not None: # 関数の指定があるとき
        response = openai.ChatCompletion.create(
            model=model, messages=messages,
            functions=functions,
            function_call='auto')
    else: # 関数の指定がなかったとき
        response = openai.ChatCompletion.create(
            model=model, messages=messages)
    if debug: print(response)
    # APIの応答がFunction callingではなかった場合の処理 --- (*10)
    message = response.choices[0]['message']
    if not message.get('function_call'):
        content = message['content'] # 応答を取り出す
        print(f'# AIの応答\n{content}\n')
        return
    # Function Callingのパラメータを読み出す --- (*11)
    name = message['function_call']['name']
    args = message['function_call']['arguments'] # JSON文字列
    if type(args) is str: # JSONデータをデコード
        args = json.loads(message['function_call']['arguments'])
    # 実行すべき関数を確認 --- (*12)
    if name == 'order_menu':
        # 厨房に対して注文を行う
        func_result = order(args.get('menu'), args.get('time'))
    else:
        func_result = '注文に失敗'
    # 関数の実行結果を含め、AIによるフォローアップメッセージを取得 --- (*13)
    messages.append({
        'role': 'function',
        'name': name, 
        'content': str(func_result) # 関数呼び出しの結果を指定
    })
    call_order_bot(messages, None)

if __name__ == '__main__':  # 料理の注文ボットを実行 ---(*14)
    print(f'# ユーザーからの注文\n{order_text}\n')
    call_order_bot(messages, functions)
