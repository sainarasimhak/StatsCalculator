from Statistics.Mean import mean
from Calculator.addition import addition
from Calculator.division import division
from Calculator.subtraction import subtraction
from Calculator.square import square


def variance(data):
    numValues = len(data)
    if numValues == 0:
        raise Exception('empty list passed to list')

    meanValue = mean(data)

    total = 0
    for i in data:
        total = addition(total, square(subtraction(i, meanValue)))

    return division(total, len(data) - 1)
