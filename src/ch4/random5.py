import random
import json

# (1) 0から99の範囲の乱数を100個生成して変数rに代入
r = [random.randint(0, 99) for _ in range(100)]

# (2) 変数rのうち5の倍数のものを変数r5に代入
r5 = [num for num in r if num % 5 == 0]

# (3) 変数r5の内容をJSON形式に変換して、変数jに代入
j = json.dumps(r5)

# (4) 変数jの内容を標準出力に出力
print(j)

# (5) ファイル「random5.json」に保存
with open('random5.json', 'w') as file:
    json.dump(r5, file)
