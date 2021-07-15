from Calculator.calculator import Calculator
from Statistics.Mean import mean
from Statistics.Median import median
from Statistics.Mode import mode
from Statistics.Sample_Mean import sample_mean
from Statistics.Variance import variance
from Statistics.StandardDeviation import standardDeviation

class StatisticsCalculator(Calculator):
    data = []

    def __init__(self):
        super().__init__()

    def mean(self, data):
        self.result = mean(data)
        return self.result

    def median(self, data):
        self.result = median(data)
        return self.result

    def mode(self, data):
        self.result = mode(data)
        return self.result

    def standard_deviation(self, a):
        self.result = standardDeviation(a)
        return self.result

    def variance(self, a):
        self.result = variance(a)
        return self.result

    def sample_mean(self, data):
        self.result = sample_mean(data)
        return self.result

