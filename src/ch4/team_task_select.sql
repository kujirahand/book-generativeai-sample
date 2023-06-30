SELECT tasks.title, tasks.description, users.name
FROM tasks
JOIN users ON tasks.user_id = users.id
WHERE users.name = '指定したユーザーの名前';
