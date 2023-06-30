# 自然言語で操作するToDOアプリ
import openai, json, time
import todo_functions
import actions

# ChatGPTを呼び出すためのメッセージを構築 --- (*1)
messages = [{
    'role': 'system',  # システムの役割を指定
    'content': 'あなたはタスク管理の優秀なエージェントです。'
}]
# ToDOアイテムを保持する --- (*2)
todo_items = actions.load_items()

# ToDOボットを実行する --- (*3)
def call_todo_bot(messages, functions=None, debug=False):
    # 希にAPI呼び出しが失敗するので自動的にリトライ --- (*4)
    while True:
        try:
            # APIの呼び出し --- (*5)
            model = 'gpt-3.5-turbo-0613'
            if functions is not None:  # 関数の指定があるとき
                response = openai.ChatCompletion.create(
                    model=model, messages=messages,
                    functions=functions,
                    function_call='auto')
            else:  # 関数の指定がなかったとき
                response = openai.ChatCompletion.create(
                    model=model, messages=messages)
            if debug: print(response)
            break
        except:
            print('アクセスエラー。3秒後に再試行します。')
            time.sleep(3) # 失敗したら3秒待機
    # APIの応答がFunction callingではなかった場合の処理 --- (*6)
    msg = response.choices[0]['message']
    if not msg.get('function_call'):
        content = msg['content']  # 応答を取り出す
        print('- AIの応答:\n', content.strip())
        # 次回の呼び出しのためにmessagesに追加
        messages.append({'role': 'assistant', 'content': content})
        return
    # Function Callingのパラメータを読み出す --- (*7)
    name = msg['function_call']['name']
    args = msg['function_call']['arguments']  # JSON文字列
    if type(args) is str:  # JSONデータをデコード
        args = json.loads(msg['function_call']['arguments'])
    print('+', name, args)
    # 実行すべき関数を確認 --- (*8)
    if name == 'add_task':
        task = args.get('task')
        func_result = actions.add_task(todo_items, task)
    elif name == 'delete_task':
        index = args.get('index', -1)
        func_result = actions.delete_task(todo_items, index)
    elif name == 'list_tasks':
        func_result = actions.list_tasks( # ToDOの一覧を表示
            todo_items,
            args.get('mode'),
            args.get('num', 0))
        return # 一覧の表示に対してAIのコメントは不要のため
    else:
        func_result = '関数の実行に失敗しました。'
    # 関数の実行結果を含め、AIによるフォローアップメッセージを取得 --- (*9)
    messages.append({
        'role': 'function',
        'name': name,
        'content': str(func_result)  # 関数呼び出しの結果を指定
    })
    call_todo_bot(messages, None)

if __name__ == '__main__':
    while True:
        # ユーザーから文章を入力 --- (*10)
        print('\n■ --- ボットへの指示を入力してください ([q]で終了)')
        user = input('>>> ')
        if user == '': continue
        if user == 'q': quit()
        # ToDOボットを実行
        messages.append({'role': 'user', 'content': user})
        call_todo_bot(messages, todo_functions.functions)
