# SIM-TERMINAL, by Simeon Duwel
# Copyright (c) 2019 Simeon Duwel, All Rights Reserved.

# e-mail: walrusgumboot.dev@gmail.com
# phone #: +32 468 47 05 87

# Last edited on: 05/03/2019 (that's DD/MM/YYYY, folks!)

import os

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

# TEXT FUNCTIONS
def asc(*args):
	if len(args) == 0:
		inputChar = input("asc > char? > ")
	elif len(args) == 1:
		inputChar = args[0]
	elif len(args) > 1:
		raise ArgumentError(function="asc()", numOfArgs=len(args))
	else:
		raise UnknownError()
	return bin(ord(inputChar))

# UTILITY FUNCTIONS
def clr():
	os.system('cls')
	return ""

# MATH FUNCTIONS
def hmd(*args):
	if len(args) == 0:
		try:
			inputCheck = eval(input("hmd > what number do you want to check for? > "))
			inputUpTo = eval(input("hmd > what number do you want to test up to? > "))
		except ValueError:
			print("err > input has to be of type int!")
	elif len(args) == 2:
		inputCheck = args[0]
		inputUpTo = args[1]
	elif len(args) > 2 or len(args) < 2:
		raise ArgumentError(function="hmd()", numOfArgs=len(args))
	else:
		print("err > An unknown error occurred.")
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
	elif len(args) == 2:
		inputA = args[0]
		inputB = args[1]
	elif len(args) > 2 or len(args) < 2:
		raise ArgumentError(function="gcd()", numOfArgs=len(args))
	else:
		raise UnknownError()

	result = 0
	aDivs = dvs(inputA)
	bDivs = dvs(inputB)

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
			return None
	elif len(args) == 2:
		inputA = args[0]
		inputB = args[1]
	elif len(args) > 2 or len(args) < 2:
		raise ArgumentError(function="lcm()", numOfArgs=len(args))
	else:
		raise UnknownError()

	result = (abs(inputA) / gcd(inputA, inputB)) * abs(inputB)
	return result

print("SIM-TERMINAL, version alpha-0.0.2")
print("Developed by Simeon Duwel, a. k. a. WalrusGumboot", end='\n\n')

print("Please contact me if you find any bugs:")
print("e-mail: walrusgumboot.dev@gmail.com")
print("phone #: +32 468 47 05 87", end='\n\n')

print("If this is your first time using SIM-TERMINAL, type hlp() for help", end='\n\n')

while True:
	try:
		print("    > " + str(eval(input("sim > "))))
	except (ArgumentError, UnknownError):
		pass
