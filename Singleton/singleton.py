# # # # # # # # # # # # # # # # # # # # # # # # #
#		Design Pattern: Singleton       #
# singleton is a design pattern where only one  #
#	instance may exist at any given time    #
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


# Third way to do a singleton using metaclasses (I like this way)
class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Python2 example
class MyClass(object):
    __metaclass__ = Singleton


#Python3
#class MyClass(BaseClass, metaclass=Singleton):
#    pass

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     Final Challenges by Youtube Channel Trevor Payne	#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## 	Create a singleton that has a function which returns a value that
# increase +1 everytime it is called (E.X. Returns 1,2,3,4,5)
class ChallengeOne():
    __metaclass__ = Singleton

    def __init__(self):
        print (self.__class__.__name__ + " Instantiated")
        self.count = 0

    def update(self):
        self.count += 1
        return self.count


## Create a singleton that acts like a phonebook. It has a function that you can pass in a Name and a Number to store,
## 	and another function to retrieve a Number and a Given Name
class ChallengeTwo():
    __metaclass__ = Singleton

    def __init__(self):
        self.name = ''
        self.number = 0
        print (self.__class__.__name__ + " Instantiated")

    def updatePhoneBook(self, name, number):
        self.name = name
        self.number = number

    def getPhoneBook(self):
        return self.name, self.number
