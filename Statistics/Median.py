from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.division import division


def median(data):
    try:
        total_values = len(data)
        list_of_numbers = [data[i] for i in range(total_values)]
        list_of_numbers.sort()
        if total_values % 2 == 0:
            median1 = list_of_numbers[int(total_values / 2)]
            median2 = list_of_numbers[int(subtraction((total_values // 2), 1))]
            result = division(addition(median1, median2), 2)
        else:
            result = list_of_numbers[int(division(total_values, 2))]
        return result
    except ValueError:
        print("ERROR!  That is an empty array.  Try again.")