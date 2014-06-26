#Python3


# singleton using metaclasses (I like this way)

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#     Final Challenges by Youtube Channel Trevor Payne	#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## 	Create a singleton that has a function which returns a value that
# increase +1 everytime it is called (E.X. Returns 1,2,3,4,5)


class ChallengeOne(metaclass=Singleton):
    def __init__(self):
        print (self.__class__.__name__ + " Instantiated")
        self.count = 0

    def update(self):
        self.count += 1
        return self.count

## Create a singleton that acts like a phonebook. It has a function that you can pass in a Name and a Number to store,
## 	and another function to retrieve a Number and a Given Name
class ChallengeTwo(metaclass=Singleton):

    def __init__(self):
        self.name = ''
        self.number = 0
        print (self.__class__.__name__ + " Instantiated")

    def updatePhoneBook(self, name, number):
        self.name = name
        self.number = number

    def getPhoneBook(self):
        return self.name, self.number