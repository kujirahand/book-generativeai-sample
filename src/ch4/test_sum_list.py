# 引数に指定したリストを合計して返す関数 --- (*1)
def sum_list(a_list):
    return sum(a_list)

# 関数sum_listをpytestでテストするための関数 --- (*2)
def test_sum_list():
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([-1, 0, 1]) == 0
    assert sum_list([10, 20, 30, 40]) == 100
    assert sum_list([]) == 0
    assert sum_list([5]) == 5

