#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, subtract, multiply, divide

    a = 10
    b = 5

    result_add = add(a, b)
    result_subtract = subtract(a, b)
    result_multiply = multiply(a, b)
    result_divide = divide(a, b)

    print("Result of {} + {} = {}".format(a, b, result_add))
    print("Result of {} - {} = {}".format(a, b, result_subtract))
    print("Result of {} * {} = {}".format(a, b, result_multiply))
    print("Result of {} / {} = {}".format(a, b, result_divide))