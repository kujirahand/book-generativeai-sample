import sqlite3

def execute_sql(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        if sql.strip().lower().startswith('select'):
            # SELECT文の場合、結果を表示する
            rows = cursor.fetchall()
            if rows:
                # ヘッダ行を表示する
                headers = [description[0] for description in cursor.description]
                head_s = ' | '.join(headers)
                print('\n' + head_s + '\n' + ('-' * len(head_s)))
                # 抽出結果を表示する
                for row in rows:
                    print(' | '.join(str(cell) for cell in row))
            else:
                # 結果がない場合はメッセージを表示する
                print('No results.')
        else:
            # SELECT文以外の場合、実行結果を表示する
            print('SQL executed successfully.')
        print()
    except sqlite3.Error as e:
        # エラーが発生した場合、エラーメッセージを表示する
        print(f'\nSQL error: {e}\n')
    except sqlite3.Warning as e:
        print(f'\nSQL warning: {e}\n')

def main(database):
    # データベースに接続する
    connection = sqlite3.connect(database)
    while True:
        # SQL文の入力を繰り返し受け付ける
        lines = []
        while True:
            # ユーザーから1行ずつSQLを入力する
            line = input('> ')
            if line == 'exit' or line == 'q':
                # ユーザーが "exit" と入力した場合、データベースをコミットして終了
                connection.commit()
                connection.close()
                return
            lines.append(line)
            if line.strip().endswith(';'):
                # 入力がセミコロンで終わる場合、SQLを実行する
                sql = '\n'.join(lines)
                execute_sql(connection, sql)
                break

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        # コマンドライン引数の数が正しくない場合はエラーメッセージを表示する
        print('Usage: python sqlite_tool.py <database>')
    else:
        database = sys.argv[1]
        # メインの処理を実行する
        main(database)
