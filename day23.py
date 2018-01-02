from InputReader import read
from collections import defaultdict
import operator
import math


ops = {'set': (lambda x, y: y),
       'add': operator.add,
       'sub': operator.sub,
       'mul': operator.mul,
       }


def mulNr(data):

    def get(item):
        try:
            return int(item)
        except ValueError:
            return registry[item]

    currentOperation = 0
    operations = [line.split() for line in data]
    registry = defaultdict(int)
    mulCount = 0
    try:
        while True:

            operation = operations[currentOperation]

            if 'jnz' in operation[0]:
                if get(operation[1]) is not 0:
                    currentOperation += get(operation[2]) - 1
            else:  # handle set, add, mul and mod operations
                registry[operation[1]] = ops[operation[0]](get(operation[1]), get(operation[2]))
                if 'mul' in operation[0]:
                    mulCount += 1
            currentOperation += 1
    except IndexError:
        pass
    return mulCount


def hValue(data):
    def get(item):
        try:
            return int(item)
        except ValueError:
            return registry[item]

    operations = [line.split() for line in data]
    currentOperation = 0
    registry = defaultdict(int)
    registry['a'] = 1
    counter = 0
    for _ in xrange(11):

        operation = operations[currentOperation]

        if 'jnz' in operation[0]:
            if get(operation[1]) is not 0:
                currentOperation += get(operation[2]) - 1
        else:  # handle set, add, mul and mod operations
            registry[operation[1]] = ops[operation[0]](get(operation[1]), get(operation[2]))
        currentOperation += 1

    stepSize = abs(int(operations[30][2]))
    # converted algorithm from the assembly code (the input), check extras/day23interpreting.txt for details
    for b in range(registry['b'], registry['c'] + 1, stepSize):

        if not prime(b):
            registry['h'] += 1

    return registry['h']


def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True


def run(data):
    result = mulNr(data)
    resultB = hValue(data)
    print result, resultB


if __name__ == "__main__":
    run(read('inputs/day23.txt'))
