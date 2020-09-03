#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[1:]
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py "
              "<a> <operator> <b>")
        sys.exit(1)

    a = int(argv[0])
    b = int(argv[2])
    oper = argv[1]

    if oper not in ['+', '-', '*', '/']:
        print("Unknown operator. "
              "Available operators: +, -, * and /")
        sys.exit(1)
    elif oper == '+':
        print("{} {} {} = {}"
              .format(a, oper, b, add(a, b)))
    elif oper == '-':
        print("{} {} {} = {}"
              .format(a, oper, b, sub(a, b)))
    elif oper == '*':
        print("{} {} {} = {}"
              .format(a, oper, b, mul(a, b)))
    elif oper == '/':
        print("{} {} {} = {}"
              .format(a, oper, b, div(a, b)))
