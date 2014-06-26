# # # # # # # # # # # # # # # # # # # # # # # # #
#		Singleton python unittest				#
# # # # # # # # # # # # # # # # # # # # # # # # #	
from __future__ import print_function

from Singleton.singleton_py3 import *

import sys

class TestSingletonPy3():
	def test_challengeOne(self):
		instance = None
		instanceList = [ChallengeOne() for i in range(5)]
		count = 1
		for i in instanceList:
			print ("%s: %s" % (i.__class__.__name__, i.update()))
			assert i.count == count
			assert i == instanceList[0]
			count += 1
		print ("end of challengeOne")

	def test_challengeTwo(self):
		instance = None
		instance = ChallengeTwo()
		assert instance is not None

		nameTest = "Jacob"
		phoneTest = "999-999-9999"
		instance.updatePhoneBook(nameTest, phoneTest)
		assert instance.name is not None and instance.number is not None
		name, phone = instance.getPhoneBook()
		assert name == nameTest and phone == phoneTest

		print ("end of challengeTwo")
