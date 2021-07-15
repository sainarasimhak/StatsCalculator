from Calculator.calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median


class StatisticsCalculator(Calculator):
    result = 0

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result
