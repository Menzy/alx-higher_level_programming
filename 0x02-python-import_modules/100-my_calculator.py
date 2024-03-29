#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv

    # Check if the correct number of command-line arguments is provided
    if len(argv) - 1 != 3:
        print("Usage: {} <a> <operator> <b>".format(argv[0]))
        exit(1)

    # Perform the calculation based on the provided operator
    if argv[2] == '+':
        print("{} + {} = {:d}"
              .format(argv[1], argv[3], add(int(argv[1]), int(argv[3]))))

    elif argv[2] == '-':
        print("{} - {} = {:d}"
              .format(argv[1], argv[3], sub(int(argv[1]), int(argv[3]))))

    elif argv[2] == '*':
        print("{} * {} = {:d}"
              .format(argv[1], argv[3], mul(int(argv[1]), int(argv[3]))))

    elif argv[2] == '/':
        print("{} / {} = {:d}"
              .format(argv[1], argv[3], div(int(argv[1]), int(argv[3]))))

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
