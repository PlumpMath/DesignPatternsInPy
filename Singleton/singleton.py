# # # # # # # # # # # # # # # # # # # # # # # # #
#		Design Pattern: Singleton               #
# singleton is a design pattern where only one  #
#	instance may exist at any given time        #
# # # # # # # # # # # # # # # # # # # # # # # # #	

# Refer here to for more information
#	https://stackoverflow.com/questions/6760685/creating-a-singleton-in-python

# first way to do a singleton through hard coding
class MySingleton(object):
	_instance = None
	def __new__(self):
		# check if _instance hasn't been set
		if not self._instance:
			# create a new instance
			self._instance = super(MySingleton, self).__new__(self)
			self.y = 10

		return self._instance
print "Singleton Example1"
x = MySingleton()
print x.y
assert x.y == 10

x.y = 20
assert x.y != 10
z = MySingleton()
print z.y
assert x.y == z.y


# Second way to do a singleton using a decorator
def singleton(MyClass):
	instances = {}
	def getInstance(*args, **kwargs):
		if MyClass not in instances:
			instances[MyClass] = MyClass(*args, **kwargs)
		return instances[MyClass]
	return getInstance

@singleton
class TestClass(object):
	def __init__(self):
		self.value = 10

print "Singleton Example2"
x = TestClass()
assert x.value == 10
print x.value
x.value *= 10

assert x.value != 10
assert x.value == 100
y = TestClass()
print y.value
assert x.value == y.value

# Third way to do a singleton using metaclasses
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#Python2
class MyClass(BaseClass):
    __metaclass__ = Singleton

#Python3
#class MyClass(BaseClass, metaclass=Singleton):
#    pass

