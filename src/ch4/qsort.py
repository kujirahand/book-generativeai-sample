def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)

# サンプルデータのリスト
data = [4, 2, 7, 1, 3, 9, 5, 8, 6]

# qsort関数を呼び出し、ソート後の結果を表示
sorted_data = qsort(data)
print(sorted_data)
