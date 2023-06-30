import random
import json

# 手順1: 0以上100未満の乱数を100個生成
random_numbers = [random.randint(0, 99) for _ in range(100)]

# 手順2: 5の倍数のものだけをJSON形式で表示
multiple_of_5 = [num for num in random_numbers if num % 5 == 0]
json_data = json.dumps(multiple_of_5)
print(json_data)

# 手順3: ファイル「random5.json」にも同じものを保存
with open("random5.json", "w") as file:
    file.write(json_data)
