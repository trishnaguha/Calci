#!/usr/bin/env python3

import argparse
import math

"Performs addition"
def add(a,b):
	val = a+b
	return val

"Performs subtraction"
def sub(a,b):
	val = a-b
	return val

"Performs division"
def div(a,b):
	val = a/b
	return val

"Performs multiplication"
def multi(a,b):
	val = a*b
	return val

"Performs percentage"
def perc(a):
	val = a/100
	return val

"Performs factorial"
def fact(a):
	return math.factorial(a)

"Performs sqaure root"
def squarert(a):
	return math.sqrt(a)

"Performs power operation"
def power(a,b):
	return math.pow(a,b)

"Performs base-10 logarithm"
def log(a):
	return math.log10(a)

"Performs sine operation"
def sin(a):
	return math.sin(a)

"Performs cosine operation"
def cos(a):
	return math.cos(a)

"Performs tangent operation"
def tan(a):
	return math.tan(a)

"Converts angle a from radians to degrees"
def deg(a):
	return math.degrees(a)

"Converts angle a from degrees to radians"
def rad(a):
	return math.radians(a)

"The Main function"
def main():
	parser = argparse.ArgumentParser(description = "A Command Line Calculator", \
				epilog = "Enter two numbers for addition,subtraction \
				and so on....\n Enter only one number for percentage \
				calculation,factorial and so on....")
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-fa", "--fadd", help = "Performs addition", \
			action = "store_true")
	group.add_argument("-fs", "--fsub", help = "Performs subtraction", \
			action = "store_true")
	group.add_argument("-fd", "--fdiv", help = "Performs division", \
			action = "store_true")
	group.add_argument("-fm", "--fmulti", help = "Performs multiplication", \
			action = "store_true")
	group.add_argument("-fp", "--fperc", help = "Performs percentage calculation", \
			action = "store_true")
	group.add_argument("-ff", "--ffact", help = "Performs factorial calculation", \
			action = "store_true")
	group.add_argument("-fsq", "--fsqrt", help = "Performs square root", \
			action = "store_true")
	group.add_argument("-fpw", "--fpow", help = "Performs power operation", \
			action = "store_true")	
	group.add_argument("-fl", "--flog", help = "Performs base-10 logarithm", \
			action = "store_true")
	group.add_argument("-fsi", "--fsin", help = "Performs sine operation", \
			action = "store_true")
	group.add_argument("-fco", "--fcos", help = "Performs cosine operation", \
			action = "store_true")
	group.add_argument("-fta", "--ftan", help = "Performs tangent operation", \
			action = "store_true")
	group.add_argument("-fdg", "--fdeg", help = "Converts angle from radians \
			to degrees", action = "store_true")
	group.add_argument("-frd", "--frad", help = "Converts angle from degrees \
			to radians", action = "store_true")


	parser.add_argument("num1", help = "Number1 to calculate",\
			type = int)
	parser.add_argument("num2", nargs = '?', help = "Number2 to calculate,\
			this is optional", type = int)

	args = parser.parse_args()

	if args.fadd:
		print("The addition result of {} and {} is {}".format \
			(args.num1,args.num2,(add(args.num1,args.num2))))
	elif args.fsub:
		print("The subtraction result of {} and {} is {}".format \
			(args.num1,args.num2,(sub(args.num1,args.num2))))
	elif args.fdiv:
		print("The division result of {} and {} is {}".format \
			(args.num1,args.num2,(div(args.num1,args.num2))))
	elif args.fmulti:
		print("The multiplication result of {} and {} is {}".format \
			(args.num1,args.num2,(multi(args.num1,args.num2))))
	elif args.fperc:
		print("The percentage of {} is {}".format(args.num1, \
			(perc(args.num1))))
	elif args.ffact:
		print("The factorial of {} is {}".format(args.num1, \
			(fact(args.num1))))
	elif args.fsqrt:
		print("The square root of {} is {}".format(args.num1, \
			(squarert(args.num1))))
	elif args.fpow:
		print("{} raised to the power {} results {}".format \
			(args.num1,args.num2,(power(args.num1,args.num2))))
	elif args.flog:
		print("The base-10 logarithmic value of {} is {}".format \
			(args.num1, (log(args.num1))))
	elif args.fsin:
		print("Sine of {} radians is {}".format(args.num1, \
			(sin(args.num1))))
	elif args.fcos:
		print("Cosine of {} radians is {}".format(args.num1, \
			(cos(args.num1))))
	elif args.ftan:
		print("Tangent of {} radians is {}".format(args.num1, \
			(tan(args.num1))))
	elif args.fdeg:
		print("{} radians to degrees is {}".format(args.num1, \
			(deg(args.num1))))
	elif args.frad:
		print("{} degrees to radians is {}".format(args.num1, \
			(rad(args.num1))))
	else:
		print("Error: requires an argument to perform an action\n \
			Type python3 calci.py -h or \
			python3 calci.py --help for help")
	
if __name__ == '__main__':
	main()
