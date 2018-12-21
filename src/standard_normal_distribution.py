# -*- coding: utf-8 -*-
import numpy as np
import math
import plot


if __name__ == '__main__':
    # 標準正規分布
    f = lambda x: np.exp(-0.5 * np.power(x, 2)) / np.sqrt(2 * np.pi)

    # min, max, num
    x = np.linspace(-5.0, 5.0, 10000)
    print('sum(f(x))', np.sum(f(x)))

    x_SD1 = x[np.where(-1 <= x)]
    x_SD1 = x_SD1[np.where(x_SD1 <= 1)]
    print('x_SD1', x_SD1)
    print('SD1 sum(f(x))', np.sum(f(x_SD1)))

    x_SD2 = x[np.where(-2 <= x)]
    x_SD2 = x_SD2[np.where(x_SD2 <= 2)]
    print('x_SD2', x_SD2)
    print('SD2 sum(f(x))', np.sum(f(x_SD2)))

    plot.plot(x, f(x))
