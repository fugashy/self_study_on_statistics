# -*- coding: utf-8 -*-
import numpy as np

def two_dice_matrix():
    ret_array = np.array([[0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0.],
                          [0., 0., 0., 0., 0., 0.]])

    for i in range(6):
        for j in range(6):
            ret_array[i][j] = float(i + 1 + j + 1) / 2.

    return ret_array
