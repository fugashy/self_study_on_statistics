# -*- coding: utf-8 -*-
import numpy as np
import dice
import plot

if __name__ == '__main__':
    # 2回サイコロを降って、その平均をとった値のすべての組み合わせ
    data = dice.two_dice_matrix()

    # 一様分布から別な分布になる
    # 平均値の度数が特に大きくなる
    # 元分布の平均値が標本平均から推定できることが数学的に表されている
    data_hist = np.histogram(data, 11, (1, 6))

    print(data_hist[0])

    plot.bar([1., 1.5, 2., 2.5, 3., 3.5, 4., 4.5, 5., 5.5, 6.], data_hist[0])

