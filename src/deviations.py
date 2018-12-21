# -*- coding: utf-8 -*-
import numpy as np
import math

if __name__ == '__main__':
    data = np.loadtxt('../data/bus.txt')
    print('data', data)

    average = np.average(data)
    print('average', average)

    # データ - 平均 = 偏差
    deviation = [data[i] - average for i in range(len(data))]
    print('deviation', deviation)

    # 偏差^2の和 / 個数 = 分散
    valiance = \
        sum([deviation[i] * deviation[i] for i in range(len(data))]) / len(data)
    print('valiance', valiance)

    stddev = math.sqrt(valiance)
    print('stddev', stddev)

    z = (data - average) / stddev
    print('z', z)
    print('z_ave', np.average(z))
    z_dev = [z[i] - np.average(z) for i in range(len(z))]
    print('z_dev', z_dev)
    z_val = sum([z_dev[i] * z_dev[i] for i in range(len(z))]) / len(z)
    print('z_val', z_val)
    print('z_stddev', np.sqrt(z_val))
