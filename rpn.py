#!/usr/bin/env python 3

import operator
import sys
import logging 
import math
from fractions import Fraction
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
logger.addHandler(sh)

operator = {
	'+':operator.add,
	'-':operator.sub,
	'*':operator.mul,
	'/':operator.truediv,
	'^':operator.pow,
	'!':math.factorial,
	'F':Fraction,
	'R':operator.add,
}
def calculate(arg):
	stack = list()
	oldtoken = ''
	for token in arg.split():
		try:
			value = float(token)
			value = round(value,2)
			stack.append(value)
		except ValueError:
			function = operator[token]
			arg2 = stack.pop()
			

			if token != '!' and token != 'F' and token != 'R':
				arg1 = stack.pop()
			if token == '/' and arg2 == 0:
				return 'Error div by zero'
			elif token == '!' or token == 'F':
				result = function(arg2)
				stack.append(result)
				print(result)
			elif token == 'R':
				function = operator[oldtoken]
				if oldtoken == '!' or oldtoken == 'F':
                                	result = function(arg2)
                                	stack.append(result)
                                	print(result)
				else:
					arg1 = stack.pop()
					result = function(arg1,arg2)
					stack.append(result)

			else:
				result = function(arg1,arg2)
				stack.append(result)
		logger.debug(stack)
		oldtoken = token		
	if len(stack) != 1:
		raise TypeError	
			
	return stack.pop();
		
	

def main():
	while True:
		print(calculate(input('rpn calc>')))

if __name__ == '__main__':
	main()
