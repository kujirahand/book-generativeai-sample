def qsort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return qsort(left) + middle + qsort(right)

def test_qsort():
    # テストケース1: 空のリスト
    assert qsort([]) == []
    # テストケース2: 重複なしの整数リスト
    assert qsort([4, 2, 7, 1, 9]) == [1, 2, 4, 7, 9]
    # テストケース3: 重複ありの整数リスト
    assert qsort([4, 2, 7, 1, 9, 2, 4, 7]) == [1, 2, 2, 4, 4, 7, 7, 9]
    # テストケース4: 負の数を含む整数リスト
    assert qsort([4, -2, 7, 1, -9, 2, 4, -7]) == [-9, -7, -2, 1, 2, 4, 4, 7]
    # テストケース5: 重複なしの浮動小数点数リスト
    assert qsort([4.5, 2.1, 7.8, 1.3, 9.0]) == [1.3, 2.1, 4.5, 7.8, 9.0]
    # テストケース6: 文字列リスト
    assert qsort(["apple", "banana", "cat", "dog"]) == ["apple", "banana", "cat", "dog"]
    # テストケース7: リストの要素が1つのみ
    assert qsort([42]) == [42]
    # テストケース8: リストの要素が2つ
    assert qsort([8, 3]) == [3, 8]
    # テストケース9: 大きなリスト (1から100までの整数)
    assert qsort(list(range(1, 101))) == list(range(1, 101))
    # テストケース10: 逆順のリスト (100から1までの整数)
    assert qsort(list(range(100, 0, -1))) == list(range(1, 101))
