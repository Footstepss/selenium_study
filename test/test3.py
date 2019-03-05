import unittest
import pandas as pd

class A(object):

	def testmethod(self):
		print("test_________________")

class test(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		cls.a = A()


	def test1(self):
		self.a.testmethod()

#	def setUp(self):
		
	

if __name__ == '__main__':
	data = pd.read_excel(r'C:\Users\Z8647\Desktop\测试用例0817.xlsx')
	print(data)