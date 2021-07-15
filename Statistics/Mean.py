from Calculator.addition import addition
from Calculator.division import division


def mean(data):
    try:
        total_values = len(data)
        total = 0
        for num in data:
            total = addition(total, num)
        return division(total, total_values)
    except ZeroDivisionError:
        print("Error: Can't Divide by 0")
    except ValueError:
        print("ERROR!  That is an empty array.  Try again")
