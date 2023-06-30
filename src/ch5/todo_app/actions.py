import json, os
DATA_FILE = 'todo_items.json'

# タスクを追加する関数 --- (*1)
def add_task(todo_items, task):
    todo_items.append(task)
    save_items(todo_items)
    return 'ToDOリストにタスクを追加しました。' + \
        'なお、どのようにタスクを完了できるか、1文でヒントを教えてください。'

# タスクを削除する関数 --- (*2)
def delete_task(todo_items, index):
    if 0 <= index < len(todo_items):
        del todo_items[index]
        save_items(todo_items)
        return '指定のToDOを完了にしました。' + \
            '簡潔にお祝いメッセージを述べてください。'
    return '完了にできません。タスク番号を指定してください。'

# アイテムを画面に表示する関数 --- (*3)
def list_tasks(todo_items, mode, num):
    if mode == '全部':
        print(f'+ 全タスク(全{len(todo_items)}件):')
        for no, task in enumerate(todo_items):
            print(f'📌 {no}: {task}')
    elif mode == '最新':
        print(f'+ 最新タスク({num}/{len(todo_items)}件):')
        offset = len(todo_items) - num
        for no, task in enumerate(todo_items):
            if no >= offset:
                print(f'📌 {no}: {task}')

# タスクをファイルから読み込む ---  (*4)
def load_items():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r', encoding='utf-8') as fp:
        data = json.load(fp)
        list_tasks(data, '全部', 0) # 既にタスクがあればそれを画面に表示
        return data
# タスク一覧をファイルに保存 --- (*5)
def save_items(todo_items):
    with open(DATA_FILE, 'w', encoding='utf-8') as fp:
        json.dump(todo_items, fp)
