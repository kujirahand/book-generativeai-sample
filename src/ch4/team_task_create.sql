-- tasksテーブル: タスクと担当ユーザーの情報一覧を保存するテーブル
CREATE TABLE tasks (
  id INTEGER PRIMARY KEY, -- タスクの一意の識別子
  title TEXT NOT NULL, -- タスクのタイトル
  description TEXT, -- タスクの詳細な説明
  user_id INTEGER, -- タスクを担当するユーザーのID
  FOREIGN KEY (user_id) REFERENCES users(id) -- usersテーブルのidカラムと関連付け
);

-- usersテーブル: ユーザーの情報一覧を保存するテーブル
CREATE TABLE users (
  id INTEGER PRIMARY KEY, -- ユーザーの一意の識別子
  name TEXT NOT NULL, -- ユーザーの名前
  email TEXT UNIQUE -- ユーザーのメールアドレス
);
