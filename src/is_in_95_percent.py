# -*- coding: utf-8 -*-
import numpy as np

def is_in_95_percent(x, u, d):
    x_z = (x - u) / d

    if -1.96 <= x_z and x_z <= 1.96:
        print('{0} ({1}) is in 95 percent'.format(x, x_z))
    else:
        print('{0} ({1}) is out of 95 percent'.format(x, x_z))


if __name__ == '__main__':
    data = np.loadtxt('../data/weight.txt')

    u = np.average(data)
    d = np.std(data)

    print('data = {0:.3f} +- {1:.3f}'.format(u, d))

    is_in_95_percent(u + d, u, d)
    is_in_95_percent(63, u, d)
    is_in_95_percent(40, u, d)
