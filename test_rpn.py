import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 +')
		self.assertEqual(2,result)
	def test_adds(self):
		result = rpn.calculate(' 1 1 + 2 +')
		self.assertEqual(4, result)
	def test_subtract(self):
		result = rpn.calculate('5 2 -')
		self.assertEqual(3,result)
	def test_tomany(self):
		with self.assertRaises(TypeError):
			Eresult = rpn.calculate('1 2 3 +')
	def test_mult(self):
		result = rpn.calculate('3 2 *')
		self.assertEqual(6, result)
	def test_div(self):
		result = rpn.calculate('10 2 /')
		self.assertEqual(5, result)
	def test_all(self):
		result = rpn.calculate('1 1 + 2 *')
		self.assertEqual(4, result)
	def test_div_zero(self):
		result = rpn.calculate('3 4 0 /')
		self.assertEqual('Error div by zero', result)
	def test_factorial(self):
		result = rpn.calculate('4 ! 3 +')
		self.assertEqual(27,result)
	def test_factor(self):
		result = rpn.calculate('.25 F')
		self.assertEqual('1/4', str(result))
	def test_repeat(self):
		result = rpn.calculate('2 3 2 + R')
		self.assertEqual(7,result)
	def test_carret(self):
		result = rpn.calculate(' 3 2 ^')
		self.assertEqual(9,result)
