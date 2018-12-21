# -*- coding: utf-8 -*-
import numpy as np

if __name__ == '__main__':
    data = np.loadtxt('../data/stddev_base.txt')

    print('data', data)
    print('data_ave', np.average(data))
    print('data_var', np.var(data))
    print('data_stddev', np.std(data))

    data_puls_4 = [data[i] + 4 for i in range(len(data))]
    print('data_puls_4', data_puls_4)
    print('data_puls_4_ave', np.average(data_puls_4))
    print('data_puls_4_var', np.var(data_puls_4))
    print('data_puls_4_stddev', np.std(data_puls_4))

    data_mul_2 = [data[i] * 2 for i in range(len(data))]
    print('data_mul_2', data_mul_2)
    print('data_mul_2_ave', np.average(data_mul_2))
    print('data_mul_2_var', np.var(data_mul_2))
    print('data_mul_2_stddev', np.std(data_mul_2))

    data_base_SD = [(data[i] - np.average(data)) / np.std(data) for i in range(len(data))]
    print('data_base_SD', data_base_SD)
