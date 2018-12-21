# -*- coding: utf-8 -*-
import numpy as np
import hypothesis_testing

if __name__ == '__main__':
    # あるデータx = 10の場合にありうる母数Nの集まり
    x = 10
    N_array = []
    for i in range(100):
        # 各枚数にて、平均分散を計算
        u, d = hypothesis_testing.coin_u_d(i)
        if hypothesis_testing.hypothesis_testing(x, u, d):
            N_array.append(i)

    print(N_array)

    # 血圧検査の例
    u = 0    # 平均（求めたい)
    d = 6    # 標準偏差
    x = 130  # 観測値
    u_max, u_min = hypothesis_testing.u_range(x, d)
    print('{0} <= u <= {1}'.format(u_min, u_max))
