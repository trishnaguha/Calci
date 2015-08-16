#!/usr/bin/env python3

import argparse

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

"The Main function"
def Main():
	parser = argparse.ArgumentParser(description="A basic Calculator")
	
	group = parser.add_mutually_exclusive_group()
	group.add_argument("-fa","--fadd",help="Performs addition",action="store_true")
	group.add_argument("-fs","--fsub",help="Performs subtraction",action="store_true")
	group.add_argument("-fd","--fdiv",help="Performs division",action="store_true")
	group.add_argument("-fm","--fmulti",help="Performs multiplication",action="store_true")

	parser.add_argument("num1",help="Number1 to calculate",type=int)
	parser.add_argument("num2",help="Number2 to calculate",type=int)

	args = parser.parse_args()

	if args.fadd:
		print("The addition result of {} and {} is {}".format(args.num1,args.num2,(add(args.num1,args.num2))))
	elif args.fsub:
		print("The subtraction result of {} and {} is {}".format(args.num1,args.num2,(sub(args.num1,args.num2))))
	elif args.fdiv:
		print("The division result of {} and {} is {}".format(args.num1,args.num2,(div(args.num1,args.num2))))
	elif args.fmulti:
		print("The multiplication result of {} and {} is {}".format(args.num1,args.num2,(multi(args.num1,args.num2))))
	else:
		print("Error: requires an argument to perform an action\nType python3 calci.py -h or python3 calci.py --help for help")
	
if __name__ == '__main__':
	Main()
