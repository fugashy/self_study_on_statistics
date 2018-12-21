# -*- coding: utf-8 -*-
import numpy as np
import math
import plot


if __name__ == '__main__':
    # 正規分布
    f = lambda x, u, d: \
        np.exp(- np.power(x - u, 2) / (2. * np.power(d, 2))) / \
                np.sqrt(2. * np.pi * np.power(d, 2))

    data = np.loadtxt('../data/tall.txt')
    shape = data.shape
    data = np.resize(data, (1, data.size))
    data = np.sort(data)
    data = np.resize(data, (data.size, 1))
    u = np.average(data)
    print('average', u)
    d = np.std(data)
    print('stddev', d)

    # 6階級 141 から 170でヒストグラムを作成
    data_hist = np.histogram(data, 6, (141, 170))
    print('frequency', data_hist[0])

    # 相対度数
    relative_frequency = \
        [data_hist[0][i] / float(data.size)
        for i in range(len(data_hist[0]))]
    print('relative frequency', relative_frequency)

    # 階級値
    class_values = \
        [(data_hist[1][i + 1] + data_hist[1][i]) / 2.0
        for i in range(len(data_hist[1]) - 1)]
    print('class value', class_values)

    # 階級値*相対度数=平均値
    average_from_class_value = \
        sum([class_values[i] * relative_frequency[i]
        for i in range(len(class_values))])
    print('average_from_class_value',
          '{0:.3f}'.format(average_from_class_value))

    # 標準正規分布に直したヒストグラムを作成
    z = (data - u) / d
    std_data_hist = np.histogram(z, 6, (np.min(z), np.max(z)))
    print('std_frequency', std_data_hist[0])

    # 標準正規分布に直した階級値
    std_class_values = \
        [(std_data_hist[1][i + 1] + std_data_hist[1][i]) / 2.0
        for i in range(len(std_data_hist[1]) - 1)]
    print('std class value', std_class_values)

    # 標準正規分布に座標変換した相対度数
    std_relative_frequency = \
        [std_data_hist[0][i] / float(z.size)
        for i in range(len(std_data_hist[0]))]
    print('std_relative frequency', std_relative_frequency)

    plot.plot([(class_values - u) / d, std_class_values],
              [relative_frequency, std_relative_frequency])
