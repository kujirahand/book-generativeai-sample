from flask import Flask, render_template, request, jsonify

# Flaskアプリケーションのインスタンスを作成 --- (*1)
app = Flask(__name__, template_folder='./')

# タスクをファイルから読み込む関数 --- (*2)
def read_tasks():
    with open('todo_tasks.txt', 'r') as file:
        tasks = file.read().splitlines()
    return tasks

# タスクをファイルに書き込む関数 --- (*3)
def write_tasks(tasks):
    with open('todo_tasks.txt', 'w') as file:
        for task in tasks:
            file.write(task + '\n')

# ルートURLにアクセスした時の処理 --- (*4)
@app.route('/')
def index():
    return render_template('todo_client.html')

# /tasks URLにアクセスした時の処理 --- (*5)
@app.route('/tasks', methods=['GET', 'POST'])
def tasks():
    if request.method == 'GET':
        # GETメソッドの場合、タスクを取得してJSON形式で返す --- (*6)
        tasks = read_tasks()
        return jsonify(tasks)
    elif request.method == 'POST':
        # POSTメソッドの場合
        # 送信されたデータからタスクを取得しファイルに追加する --- (*7)
        data = request.get_json()
        task = data.get('task')
        if task:
            tasks = read_tasks()
            tasks.append(task)
            write_tasks(tasks)
            return jsonify({'message': 'Task added successfully'})
        else:
            return jsonify({'error': 'Invalid task'})

# プログラムが直接実行された場合のみFlaskアプリケーションを起動 --- (*8)
if __name__ == '__main__':
    app.run()
