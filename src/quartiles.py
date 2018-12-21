# -*- coding: utf-8 -*-
import numpy as np

def median(data_array):
    u"""中央値とそのインデックスを返す
    Args:
        data_array: 入力データ(list of value)

    Returns:
        m: 中央値(float)
        indices: 中央値のインデックス
                 入力データの要素数が奇数なら1個
                 入力データの要素数が偶数なら2個
    """
    if len(data_array) % 2 == 0:
        # 0数えのための-1
        lower_index = len(data_array) / 2 - 1
        higher_index = lower_index + 1
        m = (data_array[higher_index] + data_array[lower_index]) / 2.
        indices = [lower_index, higher_index]
    else:
        index = int((len(data_array) / 2.))
        m = data_array[index]
        indices = [index]

    return m, indices


def quatiles_from_txt(file_path):
    data_np = np.loadtxt(file_path)
    if len(data_np.shape) == 1:
        data_array = [data_np[i]
                      for i in range(data_np.shape[0])]
    else:
        data_array = [data_np[i][j]
                      for i in range(data_np.shape[0])
                      for j in range(data_np.shape[1])]
    data_array = np.sort(data_array)

    m, indices = median(data_array)
    if len(indices) == 2:
        lower_group = data_array[:indices[0] + 1]
        higher_group = data_array[indices[1]:]
    else:
        lower_group = data_array[:indices[0]]
        higher_group = data_array[indices[0] + 1:]

    q1, _ = median(lower_group)
    q3, _ = median(higher_group)

    print('min   : {0}'.format(min(data_array)))
    print('q1    : {0}'.format(q1))
    print('median: {0}'.format(m))
    print('q3    : {0}'.format(q3))
    print('max   : {0}'.format(max(data_array)))
    print('IQR   : {0}'.format(q3 - q1))
