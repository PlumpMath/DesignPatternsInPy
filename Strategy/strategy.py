# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#		Design Pattern: Strategy Pattern                              #
# Strategy Pattern is a pattern that enables an algorithm's           #
# behavior to be selected at runtime. The strategy pattern            #
# defines a family of algorithms, encapsulates each algorithm, and    #
# makes the algorithms interchangeable within that family.            #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
from __future__ import print_function

__author__ = 'Jacob'
# more information about the strategy pattern: https://en.wikipedia.org/wiki/Strategy_pattern
# other resources:
# https://stackoverflow.com/questions/963965/how-is-this-strategy-pattern-written-in-python-the-sample-in-wikipedia

class StrategyDisbatcher:
    def __init__(self, func=None):
        if func:
            self.execute = func

    def execute(self, a=None, b=None):
        print("Default Execution")


def executeAdd(a, b):
    print("%d+%d: %d" % (a, b, a + b))
    return a + b


def executeSub(a, b):
    print("%d-%d: %d" % (a, b, a - b))
    return a - b


def executeMul(a, b):
    print("%d*%d: %d" % (a, b, a * b))
    return a * b


def executeDiv(a, b):
    if b != 0:
        print("%d/%d: %d" % (a, b, a / b))
        return a / b
    return 1


def executeExp(a):
    print("%d^%d: %d" % (a, a, a ** a))
    return a ** a


if __name__ == "__main__":
    value1 = 5
    value2 = 3
    strat = StrategyDisbatcher()
    stratAdd = StrategyDisbatcher(executeAdd)
    stratSub = StrategyDisbatcher(executeSub)
    stratMul = StrategyDisbatcher(executeMul)
    stratDiv = StrategyDisbatcher(executeDiv)
    stratExp = StrategyDisbatcher(executeExp)

    list = []
    strat.execute()
    list.append(stratAdd.execute(value1, value2))
    list.append(stratSub.execute(value1, value2))
    list.append(stratMul.execute(value1, value2))
    list.append(stratDiv.execute(value1, value2))
    list.append(stratExp.execute(value1))

    total = 0
    for l in list:
        total += l
    print("total: ", total)
