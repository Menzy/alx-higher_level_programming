#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *

    argument_count = len(argv)

    if argument_count != 4:
        print("Usage: {} <num1> <operator> <num2>".format(argv[0]))
        exit(1)

    num1 = int(argv[1])
    num2 = int(argv[3])
    operator = argv[2]

    def handle_unknown_operator():
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    def perform_addition():
        total = add(num1, num2)
        print("{:d} + {:d} = {:d}".format(num1, num2, total))
        return total

    def perform_subtraction():
        total = subtract(num1, num2)
        print("{:d} - {:d} = {:d}".format(num1, num2, total))
        return total

    def perform_multiplication():
        total = multiply(num1, num2)
        print("{:d} * {:d} = {:d}".format(num1, num2, total))
        return total

    def perform_division():
        total = divide(num1, num2)
        print("{:d} / {:d} = {:d}".format(num1, num2, total))
        return total

    operations = {
        "+": perform_addition,
        "-": perform_subtraction,
        "*": perform_multiplication,
        "/": perform_division
    }

    operations.get(operator, handle_unknown_operator)()
