# フィボナッチ数列を動的計画法を使って求めるプログラム
def fib(n):
    if n <= 1: return n
    # リスト型のテーブルに初期値を入れる
    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1
    # テーブルにあるキャッシュを使いつつ計算を行う
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

print(fib(10)) # 結果 → 55

