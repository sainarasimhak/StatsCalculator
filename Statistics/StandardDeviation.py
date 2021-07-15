import math
from Statistics.Variance import variance
from Calculator.square_root import square_root


def standardDeviation(data):
    numValues = len(data)
    if numValues == 0:
        raise Exception('empty list passed to list')
    return square_root(variance(data))
