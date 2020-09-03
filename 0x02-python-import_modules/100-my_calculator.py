#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv = sys.argv[1:]
    if len(argv) != 3:
        print('Usage: ./100-my_calculator.py '
                         '<a> <operator> <b>\n')
        sys.exit(1)

    a = int(argv[0])
    b = int(argv[2])
    oper = argv[1]

    if oper not in ['+', '-', '*', '/']:
        print('Unknown operator. '
              'Available operators: +, -, * and /\n')
        sys.exit(1)
    elif argv[1] == '+':
        print("{} {} {} = {}"
              .format(a, oper, b, add(a, b)))
    elif argv[1] == '-':
        print("{} {} {} = {}"
              .format(a, oper, b, sub(a, b)))
    elif argv[1] == '*':
        print("{} {} {} = {}"
              .format(a, oper, b, mul(a, b)))
    elif argv[1] == '/':
        print("{} {} {} = {}"
              .format(a, oper, b, div(a, b)))
