import csv
import json

# 入力ファイルと出力ファイルを指定
input_file = "ninja_corpus.csv"
output_file = "ninja_corpus.jsonl"

# ファイルを開く
with open(input_file, "r", encoding="utf-8") as csv_file, \
     open(output_file, "w", encoding="utf-8") as jsonl_file:
    csv_reader = csv.reader(csv_file) # CSVファイルを読む
    next(csv_reader)  # ヘッダー行をスキップする
    # for文で毎行を繰り返し処理
    for row in csv_reader:
        prompt = row[0] # プロンプトの列
        completion = row[1] # 応答の列
        data = {"prompt": prompt, "completion": completion}
        # JSONで書き込む
        jsonl_file.write(json.dumps(data, ensure_ascii=False) + "\n")
