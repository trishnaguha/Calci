#! /usr/bin/env python3


import argparse
import math
import sys

def add(a, b):
    """Perform Addition of two numbers passed as arguments."""
    val = a + b
    return val


def sub(a, b):
    """Perform Subtraction of two numbers passed as arguments."""
    val = a - b
    return val


def div(a, b):
    """Perform Division of two numbers passed as arguments."""
    try:
        val = a / b
        # If the denominator is Zero, division is not defined.
        if b == 0:
            raise
    except:
        print("Cannot divide by Zero !")
        sys.exit(0)
    return val


def multi(a, b):
    """Perform Multiplication of two numbers passed as arguments."""
    val = a * b
    return val

def mod(a,b):
    """Compute the modulus.

    The number passed as argument 1 is modulus
    to the number passed as argument 2.
    """
    val = a % b
    return val



def perc(a):
    """Compute the Percentage of the number passed as argument."""
    val = (a * 1.0) / 100
    return val


def fact(a):
    """Compute the Factorial of the number passed as argument."""
    return math.factorial(a)

def binary(a):
    """Compute the binary equivalent of the decimal number passed as argument."""
    return bin(a)

def hexa(a):
    """Compute the hexadecimal equivalent of the decimal number passed as argument."""
    return hex(a)

def octal(a):
    """Compute the octal equivalent of the decimal number passed as argument."""
    return oct(a)

def squarert(a):
    """Compute the Square Root of the number passed as argument."""
    return math.sqrt(a)


def power(a, b):
    """Compute the Power.

    The number passed as argument 1 is raised
    to the power of the number passed as argument 2.
    """
    return math.pow(a, b)


def log(a):
    """Compute the Common Logarithm of the number passed as argument."""
    return math.log10(a)


def log2(a):
    """Compute the Natural Logarithm of the number passed as argument."""
    return math.log2(a)


def sin(a):
    """Compute the Sine of the number passed as argument."""
    return math.sin(math.radians(a))


def cos(a):
    """Compute the Cosine of the number passed as argument."""
    return math.cos(math.radians(a))


def tan(a):
    """Compute the Tangent of the number passed as argument."""
    return math.tan(math.radians(a))


def deg(a):
    """Convert angle passed as argument from radian to degrees."""
    return math.degrees(int(a))


def rad(a):
    """Convert angle passed as argument from degrees to radian."""
    return math.radians(a)
	


def main():
    """The Driver function."""
    parser = argparse.ArgumentParser(
        description="A Command Line Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Enter two numbers for addition, subtraction and so on...
Enter only one number for percentage calculation, factorial and so on...""")

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-fa", "--fadd",
        help="Performs addition",
        action="store_true")
    group.add_argument(
        "-fs", "--fsub",
        help="Performs subtraction",
        action="store_true")
    group.add_argument(
        "-fd", "--fdiv",
        help="Performs division",
        action="store_true")
    group.add_argument("-fm", "--fmulti",
                       help="Performs multiplication",
                       action="store_true")
    group.add_argument(
        "-fp", "--fperc",
        help="Performs percentage calculation",
        action="store_true")
    group.add_argument(
        "-ff", "--ffact",
        help="Performs factorial calculation",
        action="store_true")
    group.add_argument("-fsq", "--fsqrt",
                       help="Performs square root",
                       action="store_true")
    group.add_argument(
        "-fpw", "--fpow",
        help="Performs power operation",
        action="store_true")
    group.add_argument(
        "-fl", "--flog",
        help="Performs base-10 logarithm",
        action="store_true")
    group.add_argument(
        "-fl2", "--flog2",
        help="Performs base-2 logarithm",
        action="store_true")
    group.add_argument(
        "-fsi", "--fsin",
        help="Performs sine operation",
        action="store_true")
    group.add_argument(
        "-fco", "--fcos",
        help="Performs cosine operation",
        action="store_true")
    group.add_argument(
        "-fta", "--ftan",
        help="Performs tangent operation",
        action="store_true")
    group.add_argument(
        "-fb", "--fbin",
        help="Convert to binary",
        action="store_true")
    group.add_argument(
        "-fh", "--fhex",
        help="Convert to hexadecimal",
        action="store_true")
    group.add_argument(
        "-fo", "--foct",
        help="Convert to octal",
        action="store_true")
    group.add_argument(
        "-fdg", "--fdeg",
        help="Converts angle from radians to degrees",
        action="store_true")
    group.add_argument(
        "-frd", "--frad",
        help="Converts angle from degrees to radians",
        action="store_true")
    group.add_argument(
        "-fmo", "--fmod",
        help="Performs modulus",
        action="store_true")

    parser.add_argument(
        "num1",
        help="Number1 to calculate",
        type=int)
    parser.add_argument(
        "num2",
        nargs='?',
        help="Number2 to calculate, this is optional", type=int)


    args = parser.parse_args()

    if args.fadd:
        print("The addition result of {} and {} is {}".format(
            args.num1, args.num2, (add(args.num1, args.num2))))
    elif args.fsub:
        print("The subtraction result of {} and {} is {}".format(
            args.num1, args.num2, (sub(args.num1, args.num2))))
    elif args.fmod:
        print("The modulus result of {} and {} is {}".format(
            args.num1, args.num2, (mod(args.num1, args.num2))))
    elif args.fdiv:
        print("The division result of {} and {} is {}".format(
            args.num1, args.num2, (div(args.num1, args.num2))))
    elif args.fmulti:
        print("The multiplication result of {} and {} is {}".format(
            args.num1, args.num2, (multi(args.num1, args.num2))))
    elif args.fperc:
        print("The percentage of {} is {}".format(
            args.num1, (perc(args.num1))))
    elif args.ffact:
        print("The factorial of {} is {}".format(args.num1, (fact(args.num1))))
    elif args.fsqrt:
        print("The square root of {} is {}".format(
            args.num1, (squarert(args.num1))))
    elif args.fbin:
        print("The binary equivalent of {} is {}".format(
            args.num1, (binary(args.num1))))
    elif args.foct:
        print("The Octal equivalent of {} is {}".format(
            args.num1, (octal(args.num1))))
    elif args.fhex:
        print("The Hexadecimal equivalent of {} is {}".format(
            args.num1, (hexa(args.num1))))
    elif args.fpow:
        print("{} raised to the power {} results {}".format(
            args.num1, args.num2, (power(args.num1, args.num2))))
    elif args.flog:
        print(
            "The base-10 logarithmic value of"
            " {} is {}".format(args.num1, (log(args.num1))))
    elif args.flog2:
        print(
            "The base-2 logarithmic value of"
            " {} is {}".format(args.num1, (log2(args.num1))))
    elif args.fsin:
        print("Sine of {} radians is {}".format(args.num1, (sin(args.num1))))
    elif args.fcos:
        print("Cosine of {} radians is {}".format(args.num1, (cos(args.num1))))
    elif args.ftan:
        print("Tangent of {} radians is {}".format(
            args.num1, (tan(args.num1))))
    elif args.fdeg:
        print("{} radians to degrees is {}".format(
            args.num1, (deg(args.num1))))
    elif args.frad:
        print("{} degrees to radians is {}".format(
            args.num1, (rad(args.num1))))
    else:
        print("Error: requires an argument to perform an action\n"
              "Type python3 calci.py -h or python3 calci.py --help for help")

if __name__ == '__main__':
    main()
