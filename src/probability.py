# -*- coding: utf-8 -*-
import numpy as np


class DiceModel():
    def __init__(self):
        self.__values = np.array([1, 2, 3, 4, 5, 6])

    def sample(self):
        return np.random.choice(self.__values)


class CoinModel():
    def __init__(self):
        self.__values = np.array([0, 1])

    def sample(self):
        return np.random.choice(self.__values)


class SimpleValueChecker():
    def __init__(self, threshold, mode='equal'):
        self.__threshold = threshold
        if mode == 'equal':
            self.__check = \
                lambda value: value == threshold
        elif mode == 'lower':
            self.__check = \
                lambda value: value < threshold
        elif mode == 'higher':
            self.__check = \
                lambda value: value > threshold
        else:
            raise Exception('Invalid mode')

    def check(self, value):
        return self.__check(value)


def repetition(num, model, checker):
    u"""繰り返し施行
    Args:
        num: 施行回数(int)
        model: 母集団モデル(class)
        check_func: 判定式(func)

    Returns:
        判定式を満たす事象が起こる確率(float)
        値(list of value)
        確率の推移(list of value)
    """
    ok_count = 0
    values = []
    progress = []
    for i in range(num):
        value = model.sample()
        values.append(value)
        if checker.check(value):
            ok_count += 1
        progress.append(float(ok_count) / float(i + 1))

    return float(ok_count) / float(num), values, progress
