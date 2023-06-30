def calc_coin(total, a, b, c, d):
    # 組み合わせの初期値を設定
    min_coins = float('inf')  # 最小のコイン枚数を無限大に設定
    result = None  # 結果の変数を初期化

    # 10円玉のループ
    for i in range(a + 1):
        # 50円玉のループ
        for j in range(b + 1):
            # 100円玉のループ
            for k in range(c + 1):
                # 500円玉のループ
                for l in range(d + 1):
                    # 合計金額の計算
                    total_amount = i * 10 + j * 50 + k * 100 + l * 500
                    # コインの枚数が最小かつ合計金額がtotalと一致する場合
                    if total_amount == total and i + j + k + l < min_coins:
                        min_coins = i + j + k + l
                        result = (i, j, k, l)  # 現在の組み合わせを記録する

    return result  # 最適な組み合わせを返す
