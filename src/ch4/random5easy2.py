import random
import json

numbers = []
for _ in range(100):
    number = random.randint(1, 99)
    if number % 5 == 0:
        numbers.append(number)

data = {'numbers': numbers}

json_data = json.dumps(data)
print(json_data)
