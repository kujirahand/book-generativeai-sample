# ToDOアプリのFunction Callingで使う関数の定義 --- (*1)
functions = [
    # タスクを追加する「add_task」の定義 --- (*2)
    {
        'name': 'add_task',
        'description': 'ToDOタスクの追加、または覚える。',
        'parameters': {
            'type': 'object',
            'properties': {
                'task': {
                    'type': 'string',
                    'description': 'ToDOタスクの内容'
                }
            }
        }
    },
    # タスクを削除する「delete_task」の定義 --- (*3)
    {
        'name': 'delete_task',
        'description': '指定番号のタスクを削除,完了する。(例:5番を削除,7を完了)',
        'parameters': {
            'type': 'object',
            'properties': {
                'index': {
                    'type': 'number',
                    'description': '番号。例えば「3番のタスク」「5を」'
                }
            }
        }
    },
    # ToDOの一覧を表示する「list_tasks」の定義 --- (*4)
    {
        'name': 'list_tasks',
        'description': 'ToDOタスクの一覧を表示する',
        'parameters': {
            'type': 'object',
            'properties': {
                'mode': { # 表示モードの指定 --- (*5)
                    'type': 'string',
                    'description': 'どのように表示するのかを指定',
                    'enum': ['全部', '最新'] # 選択肢を指定
                },
                'num': { # 表示件数を指定
                    'type': 'number',
                    'desctiption': '何件表示するのかを指定'
                }
            }
        }
    }
]
