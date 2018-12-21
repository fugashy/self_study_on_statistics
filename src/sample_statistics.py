# -*- coding: utf-8 -*-
import numpy as np


def mean(data):
    return np.average(data)

def stddev(data):
    ave = sample_mean(data)
    return ave / np.sqrt(data.size)

def two_sigma_interval(u=0, d=0, n=0, data=None):
    if data is not None:
        u = mean(data)
        d = stddev(data)
        n = data.size

    return u - 1.96 * d / np.sqrt(n), u + 1.96 * d / np.sqrt(n)
