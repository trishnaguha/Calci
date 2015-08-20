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

"The Main function"
def main():
	parser = argparse.ArgumentParser(description = "A Command Line Calculator", epilog = "Enter two numbers for addition,subtraction and so on.... \n Enter only one number for percentage calculation,factorial and so on....")
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-fa", "--fadd", help = "Performs addition", action = "store_true")
	group.add_argument("-fs", "--fsub", help = "Performs subtraction", action = "store_true")
	group.add_argument("-fd", "--fdiv", help = "Performs division", action = "store_true")
	group.add_argument("-fm", "--fmulti", help = "Performs multiplication", action = "store_true")
	group.add_argument("-fp", "--fperc", help = "Performs percentage calculation", action = "store_true")
	group.add_argument("-ff", "--ffact", help = "Performs factorial calculation", action = "store_true")
	

	parser.add_argument("num1", help = "Number1 to calculate", type = int)
	parser.add_argument("num2", nargs='?', help = "Number2 to calculate, this is optional", type = int)

	args = parser.parse_args()

	if args.fadd:
		print("The addition result of {} and {} is {}".format(args.num1,args.num2,(add(args.num1,args.num2))))
	elif args.fsub:
		print("The subtraction result of {} and {} is {}".format(args.num1,args.num2,(sub(args.num1,args.num2))))
	elif args.fdiv:
		print("The division result of {} and {} is {}".format(args.num1,args.num2,(div(args.num1,args.num2))))
	elif args.fmulti:
		print("The multiplication result of {} and {} is {}".format(args.num1,args.num2,(multi(args.num1,args.num2))))
	elif args.fperc:
		print("The percentage of {} is {}".format(args.num1,(perc(args.num1))))
	elif args.ffact:
		print("The factorial of {} is {}".format(args.num1,(fact(args.num1))))
	else:
		print("Error: requires an argument to perform an action\nType python3 calci.py -h or python3 calci.py --help for help")
	
if __name__ == '__main__':
	main()
