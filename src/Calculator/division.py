def division(a, b):
    try:
        d = float(a) / float(b)
        return round(d, 9)
    except ZeroDivisionError as error:
        error = "ERROR!  YOU CANNOT DIVIDE BY ZERO!"
        return error
