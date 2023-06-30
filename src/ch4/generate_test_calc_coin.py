import random

def generate_test_cases():
    test_cases = []
    
    for _ in range(10):
        a = random.randint(0, 9)  # aに0から9のランダムな値を代入
        d = random.randint(0, 9)  # dに0から9のランダムな値を代入
        b = random.randint(0, 1)  # bに0または1のランダムな値を代入
        c = random.randint(0, 1)  # cに0または1のランダムな値を代入
        total = a * 10 + b * 50 + c * 100 + d * 500  # totalに計算結果を代入
        
        test_case = f"assert calc_coin({total}, {a}, {b}, {c}, {d}) == ({a}, {b}, {c}, {d})"  # test_caseにテストケースのアサーションを代入
        test_cases.append(test_case)  # test_casesにtest_caseを追加
    
    return test_cases

test_cases = generate_test_cases()

# テストケースを出力する
print("from calc_coin import calc_coin")  # calc_coinをインポートする文を出力
print("def test_calc_coin():")  # test_calc_coin関数の宣言を出力
for test_case in test_cases:
    print(f"    {test_case}")  # 各テストケースを出力
