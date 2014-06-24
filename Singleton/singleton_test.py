# # # # # # # # # # # # # # # # # # # # # # # # #
#		Singleton python unittest				#
# # # # # # # # # # # # # # # # # # # # # # # # #	
from __future__ import print_function

from singleton import *

class TestSingleton():
	def test_example1(self):
		print ("Singleton Example1")
		x = MySingleton()
		print (x.y)
		assert x.y == 10

		x.y = 20
		assert x.y != 10
		z = MySingleton()
		print (z.y)
		assert x.y == z.y


	def test_example2(self):
		print ("Singleton Example2")
		x = TestClass()
		assert x.value == 10
		print (x.value)
		x.value *= 10

		assert x.value != 10
		assert x.value == 100
		y = TestClass()
		print (y.value)
		assert x.value == y.value

	def test_challengeOne(self):
		instanceList = [ChallengeOne() for i in range(5)]
		count = 1
		for i in instanceList:
			print ("%s: %s" % (i.__class__.__name__, i.update()))
			assert i.count == count
			assert i == instanceList[0]
			count += 1
		print ("end of challengeOne")

	def test_challengeTwo(self):
		instance = ChallengeTwo()
		assert instance is not None

		nameTest = "Jacob"
		phoneTest = "999-999-9999"
		instance.updatePhoneBook(nameTest, phoneTest)
		assert instance.name is not None and instance.number is not None
		name, phone = instance.getPhoneBook()
		assert name == nameTest and phone == phoneTest

		print ("end of challengeTwo")
