# Copyright (c) 2019 Simeon Duwel, All Rights Reserved.

# e-mail: walrusgumboot.dev@gmail.com
# phone #: +32 468 47 05 87

# Last edited on: 04/03/2019 (that's DD/MM/YYYY, folks!)

import os

functions = {
	"asc()" : "ascii representation of a char",
	"clr()" : "clear the console",
	"dvs()" : "return divisors of an int",
	"gcd()" : "return the gcd of an int",
	"hlp()" : "print a basic welcome guide",
	"hmd()" : "amount of times an int divides in another",
	"lcm()" : "return the lcm of an int",
	"lst()" : "list all functions",
	"pwd()" : "print the working directory"
}

# EXCEPTIONS
class ArgumentError(Exception):
	"""
	Raised when too little (or too many) arguments get passed to a function.

	Parameters:
	-----------
	numOfArgs : int
		the amount of arguments that were passed to the function
	function : str
		the name of the function that tried to execute
	"""
	def __init__(self, function, numOfArgs):
		self.function = function
		self.numOfArgs = numOfArgs
		print(f"ArgumentError: {self.numOfArgs} arguments were passed while trying to execute {self.function}.")
class UnknownError(Exception):
	"""
	Raised when an unknown error occurs.
	"""
	def __init__(self):
		print("UnknownError: An unknown error occurred. \nPlease contact me with the details provided on startup.")
class DoNotPrint(Exception):
	"""This is not really an exception, more a cheeky way to get around my Pythonic way of handling
	input and output without having to implement an if statement."""
	def __init__(self):
		pass

# TEXT FUNCTIONS
def hlp(*args):
	if len(args) == 0:
		print()
		print("    > SIM-TERMINAL is a terminal-like utility tool based on Python.")
		print("    > It contains some useful commands to quickly calculate all kinds of things,")
		print("    > create new files or perform bulk operations on a large group of files.", end='\n\n')

		print("    > Everything in SIM-TERMINAL is based around the concept of functions.")
		print("    > An example would be \"dvs()\", which, when typed, prompts you with \"dvs > input?> \"")
		print("    > Entering a number and pressing Enter will in this case return the divisors of the")
		print("    > number you entered.", end="\n\n")

		print("    > Most function can also be called with the value between the brackets.")
		print("    > For example, dvs(420) will return the divisors of 420 while skipping the prompt.", end='\n\n')

		print("    > If you want detailed info on a specific function, type hlp(\"name_of_function\").")
		print("    > For a list of all available commands and a short summary of what they do, type lst().", end='\n\n')
	elif len(args) == 1:
		if args[0] in functions:
			print(f"    > {args[0]} : {functions.get(args[0])}")
		else:
			print("    > That function was not found. Remember to end function names with brackets.")
	elif len(args) > 1:
		raise ArgumentError(function="lst()", numOfArgs=len(args))
	else:
		raise UnknownError()
	raise DoNotPrint()
def asc(*args):
	"""asc()
	ascii representation of a given character"""
	if len(args) == 0:
		inputChar = input("asc > char? > ")
	elif len(args) == 1:
		inputChar = args[0]
	elif len(args) > 1:
		raise ArgumentError(function="asc()", numOfArgs=len(args))
	else:
		raise UnknownError()
	return bin(ord(inputChar))
def lst():
	print()
	print("    > function | description")
	print("    > ---------+------------")
	for k, v in functions.items():
		print(f"    > {k}    | {v}")
	print()
	raise DoNotPrint()

# UTILITY FUNCTIONS
def clr():
	if os.name == "nt":
		os.system('cls')
	else:
		os.system(' clear')
	raise DoNotPrint()

# MATH FUNCTIONS
def hmd(*args):
	if len(args) == 0:
		try:
			inputCheck = eval(input("hmd > check? > "))
			inputUpTo = eval(input("hmd > up to? > "))
		except ValueError:
			print("err > input has to be of type int!")
			raise DoNotPrint()
	elif len(args) == 2:
		inputCheck = args[0]
		inputUpTo = args[1]
	elif len(args) > 2 or len(args) < 2:
		raise ArgumentError(function="hmd()", numOfArgs=len(args))
	else:
		raise UnknownError()
	result = 0

	for i in range(inputUpTo):
		if (i % inputCheck == 0):
			result = result + 1
		else:
			continue
	return result
def dvs(*args):
	inputVal = 0
	if len(args) == 0:
		try:
			inputVal = eval(input("dvs > input? > "))
		except ValueError:
			print("err > input has to be of type int!")
			raise DoNotPrint()
	elif len(args) == 1:
		inputVal = args[0]
	elif len(args) > 1:
		raise ArgumentError(function="dvs()", numOfArgs=len(args))
	else:
		raise UnknownError()

	divisors = []
	for i in range(1, inputVal + 1):
		if inputVal % i == 0:
			divisors.append(i)
	return divisors
def gcd(*args):
	if len(args) == 0:
		try:
			inputA = eval(input("gcd > input a? > "))
			inputB = eval(input("gcd > input b? > "))
		except ValueError:
			print("err > input has to be of type int!")
			raise DoNotPrint()
	elif len(args) == 2:
		inputA = args[0]
		inputB = args[1]
	elif len(args) > 2 or len(args) < 2:
		raise ArgumentError(function="gcd()", numOfArgs=len(args))
	else:
		raise UnknownError()


	# Euclid's algorithm
	result = 0
	while inputB != 0:
		temp = inputB
		inputB = inputA % inputB
		inputA = temp
	return inputA
def lcm(*args):
	if len(args) == 0:
		try:
			inputA = eval(input("lcm > input a? > "))
			inputB = eval(input("lcm > input b? > "))
		except ValueError:
			print("err > input has to be of type int!")
			raise DoNotPrint()
	elif len(args) == 2:
		inputA = args[0]
		inputB = args[1]
	elif len(args) > 2 or len(args) < 2:
		raise ArgumentError(function="lcm()", numOfArgs=len(args))
	else:
		raise UnknownError()

	result = (abs(inputA) / gcd(inputA, inputB)) * abs(inputB)
	return result

# FILE OPERATIONS
def pwd():
	print()
	print(f"    > {os.getcwd()}")
	print()
	raise DoNotPrint()

print("SIM-TERMINAL, version alpha-0.0.3")
print("Developed by Simeon Duwel, a. k. a. WalrusGumboot", end='\n\n')

print("Please contact me if you find any bugs:")
print("e-mail: walrusgumboot.dev@gmail.com")
print("phone #: +32 468 47 05 87", end='\n\n')

print("If this is your first time using SIM-TERMINAL, type hlp() for help", end='\n\n')

while True:
	try:
		print("    > " + str(eval(input("sim > "))))
	except SyntaxError:
		print("sim > err > syntax error")
		pass
	except NameError:
		print("sim > err > name error")
		pass
	except (ArgumentError, UnknownError, DoNotPrint):
		pass
