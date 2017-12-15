from InputReader import read


def bitGenerator(factor, value, multiple=1):
    while True:
        value = value * factor % 2147483647
        if value % multiple == 0:
            yield value & 0xFFFF


def matchResult(data):
    startValues = [int(line.split()[-1]) for line in data]
    count = countEqual(bitGenerator(16807, startValues[0]), bitGenerator(48271, startValues[1]), 40000000)
    countB = countEqual(bitGenerator(16807, startValues[0], 4), bitGenerator(48271, startValues[1], 8), 5000000)
    return count, countB


def countEqual(genA, genB, iterations):
    count = 0
    for _ in xrange(iterations):
        if genA.next() == genB.next():
            count += 1
    return count


def run(data):
    result = matchResult(data)
    print 'Counts on part A: {0}\n' \
          'Counts on part B: {1}'.format(*result)


if __name__ == "__main__":
    run(read('inputs/day15.txt'))