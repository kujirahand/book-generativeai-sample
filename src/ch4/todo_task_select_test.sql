SELECT *
FROM tasks
WHERE completed = 0
  AND title LIKE '%テスト%';
