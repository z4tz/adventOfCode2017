from InputReader import read
from collections import defaultdict
import re
import operator

registry = defaultdict(int)
ops = {'==': operator.eq,
       '!=': operator.ne,
       '>': operator.gt,
       '<': operator.lt,
       '>=': operator.ge,
       '<=': operator.le,
       'inc': operator.add,
       'dec': operator.sub}


def computeInstructions(data):
    regex = re.compile('^([a-z]+) (inc|dec) ([-0-9]+) if ([a-z]+) ([=><!]+) ([-0-9]+)')
    maxValue = float('-inf')
    for line in data:
        compute(*regex.match(line).groups())
        maxValue = max(maxValue, max(registry.values()))
    return [max(registry.values()), maxValue]


def compute(var1, op1, val1, var2, op2, val2):
    if ops[op2](registry[var2], int(val2)):
        registry[var1] = ops[op1](registry[var1], int(val1))


def run(data):
    result = computeInstructions(data)
    print 'Final state max registry value: {0}\nMax registry value during runtime: {1}'.format(*result)


if __name__ == "__main__":
    run(read('inputs/day8.txt'))
