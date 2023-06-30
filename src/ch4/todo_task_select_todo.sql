SELECT *
FROM tasks
WHERE completed = 0
ORDER BY priority DESC
LIMIT 5;
