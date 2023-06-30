# (注意) 間違っています
from calc_coin import calc_coin

def test_calc_coin():
    assert calc_coin(100, 0, 0, 1, 0) == (0, 0, 1, 0)
    assert calc_coin(420, 5, 2, 3, 1) == (1, 0, 2, 0)
    assert calc_coin(760, 2, 5, 3, 1) == (0, 2, 1, 1)
    assert calc_coin(670, 0, 10, 3, 1) == (0, 10, 2, 1)
    assert calc_coin(350, 5, 2, 3, 1) == (0, 0, 3, 0)
    assert calc_coin(920, 5, 2, 3, 1) == (2, 0, 1, 1)
    assert calc_coin(80, 1, 1, 0, 1) == (0, 1, 0, 1)
    assert calc_coin(1230, 5, 5, 5, 5) == (0, 1, 0, 2)
