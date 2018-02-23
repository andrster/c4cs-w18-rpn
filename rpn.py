#!/usr/bin/env python 3

import operator

operator = {
	'+':operator.add,
	'-':operator.sub,
	'*':operator.mul,
	'/':operator.trudiv,
}
def calculate(arg):
	stack = list()
	for token in arg.split():
		try:
			value = int(token)
			stack.append(value)
		except ValueError:
			function = operator[token]
			arg2 = stack.pop()
			arg1 = stack.pop()
			result = function(arg1,arg2)
			stack.append(result)
			
	if len(stack) != 1:
		raise TypeError	
			
	return stack.pop();
		
	

def main():
	while True:
		print(calculate(input('rpn calc>')))

if __name__ == '__main__':
	main()
