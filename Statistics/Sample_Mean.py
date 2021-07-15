from Statistics.Mean import mean
from Statistics.GetSample import getSample

import random
import statistics


def sample_mean(num):
    sample_size = random.randint(1, len(num))
    new_values = getSample(num, sample_size)
    n = round(mean(new_values), 2)
    actual_mean = round(statistics.mean(new_values), 2)
    return n, actual_mean
