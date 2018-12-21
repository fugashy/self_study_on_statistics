# -*- coding: utf-8 -*-
import numpy as np
import plot

if __name__ == '__main__':
    data = np.loadtxt('../data/tall.txt')

    print('average', '{0:.3f}'.format(np.average(data)))

    # 6階級 141 から 170でヒストグラムを作成
    data_hist = np.histogram(data, 6, (141, 170))
    print('frequency', data_hist[0])

    # 相対度数
    relative_frequency = \
        [data_hist[0][i] / float(data.size)
        for i in range(len(data_hist[0]))]
    np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

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

    plot.bar(class_values, data_hist[0])
