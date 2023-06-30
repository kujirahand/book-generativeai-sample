CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY,    /* タスクの一意のID */
    title TEXT NOT NULL,            /* タスクのタイトル（必須）*/
    description TEXT,               /* タスクの説明（任意）*/
    priority INTEGER,               /* タスクの優先度（任意）*/
    completed INTEGER DEFAULT 0     /* タスクの完了状態（デフォルトは未完了）*/
);
