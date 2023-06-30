from calc_coin import calc_coin
import pytest

def test_calc_coin():
    # 各コイン枚数をランダムに設定
    a, b, c, d = 10, 10, 10, 10
    # テストケースのリスト
    test_cases = [
        (10, a, b, c, d, (1, 0, 0, 0)),
        (50, a, b, c, d, (0, 1, 0, 0)),
        (100, a, b, c, d, (0, 0, 1, 0)),
        (500, a, b, c, d, (0, 0, 0, 1)),
        (110, a, b, c, d, (1, 0, 1, 0)),
        (550, a, b, c, d, (0, 1, 0, 1)),
        (1000, a, b, c, d, (0, 0, 0, 2)),
        (570, a, b, c, d, (2, 1, 0, 1)),
    ]
    for total, a, b, c, d, expected in test_cases:
        assert calc_coin(total, a, b, c, d) == expected

if __name__ == "__main__":
    pytest.main()


