# -*- coding: utf-8 -*-
import numpy as np

N = 25
p_stddev = 10
x_bar = 80

x_stddev = p_stddev / np.sqrt(N)

min_95per = - (2 * 1.96 - x_bar)
max_95per = - (2 * (-1.96) - x_bar)

print('95 per range is {0} to {1}'.format(min_95per, max_95per))
