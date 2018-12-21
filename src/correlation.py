# -*- coding: utf-8 -*-
import numpy as np
import math


def deviation(data_list):
    u"""偏差のベクトルを返す
    Args:
        data_list: 入力データ(list of value)

    Returns:
        偏差(list of value)
    """
    ave = sum(data_list) / len(data_list)
    return [data - ave for data in data_list]


def variance(data_list):
    u"""分散を返す
    Args:
        data_list: 入力データ(list of value)

    Returns:
        分散(float)
    """
    devs = deviation(data_list)
    # 偏差の自乗の総和 / 要素数
    return sum([dev**2 for dev in devs]) / len(devs)


def stddev(data_list):
    u"""標準偏差を返す
    Args:
        data_list: 入力データ(list of value)

    Returns:
        標準偏差(float)
    """
    # 分散の平方根
    return(math.sqrt(variance(data_list)))


def covariance(list_x, list_y, verbose=False):
    u"""2変数の共分散を返す
    Args:
        list_x: 入力データ1(list of value)
        list_y: 入力データ2(list of value)
        verbose: 中間結果を表示する(bool)

    Returns:
        共分散(float)
    """
    if len(list_x) != len(list_y):
        raise Exception('Invalid length')

    dev_x = deviation(list_x)
    dev_y = deviation(list_y)

    cov = sum([dev_x[i] * dev_y[i]
               for i in range(len(list_x))]) / len(list_x)
    if verbose:
        print('dev x', dev_x)
        print('dev x', dev_y)
        print('covariance', cov)

    return cov


def covariance_from_txt(file_path):
    data_np = np.transpose(np.loadtxt(file_path))

    return covariance(data_np[0], data_np[1], verbose=True)


def correlation_from_txt(file_path):
    data_np = np.transpose(np.loadtxt(file_path))

    cov = covariance(data_np[0], data_np[1])
    s_x = stddev(data_np[0])
    s_y = stddev(data_np[1])

    return cov / (s_x * s_y)
