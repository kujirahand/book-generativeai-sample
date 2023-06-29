# フィボナッチ数列を再帰的に求めるプログラム
def fib(n):
    if n <= 1: return n
    return fib(n-2) + fib(n-1)

print(fib(10)) # 結果 → 55

