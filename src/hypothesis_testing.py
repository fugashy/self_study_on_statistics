# -*- coding: utf-8 -*-
import numpy as np

def coin_u_d(N):
    return N / 2, np.sqrt(N) / 2

def compute_z(x, u, d):
    return (x - u) / d

def u_range(x, d):
    # 式変形過程
    # -1.96 = (x - u) / d
    # -1.96 * d + u = x
    # u = x + 1.96 * d
    return x + 1.96 * d, x - 1.96 * d

def hypothesis_testing(x, u, d, verbose=False):
    # 式変形過程
    # -1.96 = (x - u) / d
    # -1.96 * d + u = x
    x_min_thresh = -1.96 * d + u
    x_max_thresh = 1.96 * d + u
    if verbose:
        print('case {0} <= x <= {1} is 95 percent range'.format(
            x_min_thresh, x_max_thresh))

    if x_min_thresh <= x and x <= x_max_thresh:
        if verbose:
            print('{0} is accepted'.format(x))
        return True
    else:
        if verbose:
            print('{0} is rejected'.format(x))
        return False


if __name__ == '__main__':
    # N枚のコインを投げる実験をした
    # 10枚表がでたとする
    # Nを何枚と想定するのが妥当か
    # 以下のA, Bから選べ
    # A : 16枚
    # B : 36枚
    x = 10

    # N = 16とした場合
    u, d = coin_u_d(16)
    hypothesis_testing(x, u, d, True)


    # N = 36とした場合
    u, d = coin_u_d(36)
    hypothesis_testing(x, u, d, True)

    # N = 100とした場合、x = 57は妥当か
    x = 57
    u, d = coin_u_d(100)
    hypothesis_testing(x, u, d, True)
