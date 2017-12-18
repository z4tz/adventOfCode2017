from InputReader import read
from collections import defaultdict
import operator
from Queue import Queue

ops = {'set': (lambda x, y: y),
       'add': operator.add,
       'mul': operator.mul,
       'mod': operator.mod,
       }


def rcvFrequency(data):

    def get(item):
        try:
            return int(item)
        except ValueError:
            return registry[item]

    currentOperation = 0
    operations = [line.split() for line in data]
    registry = defaultdict(int)
    lastSound = 0
    while True:
        operation = operations[currentOperation]

        if 'jgz' in operation[0]:
            if get(operation[1]) > 0:
                currentOperation += get(operation[2]) - 1
        elif 'snd' in operation[0]:
            lastSound = get(operation[1])
        elif 'rcv' in operation[0]:
            if get(operation[1]):
                return lastSound
        else:  # handle set, add, mul and mod operations
            registry[operation[1]] = ops[operation[0]](get(operation[1]), get(operation[2]))

        currentOperation += 1


# Part 2
def duet(data):

    def get(item):
        try:
            return int(item)
        except ValueError:
            return registry[item]

    currentOperation = [0, 0]
    operations = [line.split() for line in data]
    registries = [defaultdict(int), defaultdict(int)]
    registries[0]['p'] = 0
    registries[1]['p'] = 1
    queues = [Queue(), Queue()]
    itemsSent = [0, 0]
    deadlock = [0, 0]

    while True:
        for i in range(2):
            operation = operations[currentOperation[i]]
            registry = registries[i]

            if 'jgz' in operation[0]:
                if get(operation[1]) > 0:
                    currentOperation[i] += get(operation[2]) - 1
            elif 'snd' in operation[0]:
                itemsSent[i] += 1
                queues[1-i].put(get(operation[1]))
            elif 'rcv' in operation[0]:
                if not queues[i].empty():
                    registry[operation[1]] = queues[i].get()
                else:
                    if deadlock[1-i] == 1:
                        return itemsSent[1]
                    else:
                        deadlock[i] = 1
                        continue
            else:  # handle set, add, mul and mod operations
                registry[operation[1]] = ops[operation[0]](get(operation[1]), get(operation[2]))

            currentOperation[i] += 1
            deadlock[i] = 0


def run(data):
    result = rcvFrequency(data)
    resultB = duet(data)
    print result, resultB


if __name__ == "__main__":
    run(read('inputs/day18.txt'))
