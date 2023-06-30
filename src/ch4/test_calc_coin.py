from calc_coin import calc_coin
def test_calc_coin():
    assert calc_coin(2070, 2, 1, 0, 4) == (2, 1, 0, 4)
    assert calc_coin(4170, 7, 0, 1, 8) == (7, 0, 1, 8)
    assert calc_coin(4660, 6, 0, 1, 9) == (6, 0, 1, 9)
    assert calc_coin(3140, 4, 0, 1, 6) == (4, 0, 1, 6)
    assert calc_coin(2740, 9, 1, 1, 5) == (9, 1, 1, 5)
    assert calc_coin(4660, 6, 0, 1, 9) == (6, 0, 1, 9)
    assert calc_coin(1560, 6, 0, 0, 3) == (6, 0, 0, 3)
    assert calc_coin(4650, 0, 1, 1, 9) == (0, 1, 1, 9)
    assert calc_coin(140, 9, 1, 0, 0) == (9, 1, 0, 0)
    assert calc_coin(1050, 5, 0, 0, 2) == (5, 0, 0, 2)
