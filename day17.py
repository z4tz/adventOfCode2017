from InputReader import read


def spinLock(data):
    steps = int(data)
    insertions = [0]
    currentPos = 0
    for i in xrange(1, 2018):
        currentPos = (steps + currentPos + 1) % len(insertions)
        insertions.insert(currentPos+1, i)
    return insertions[insertions.index(2017)+1]


def longSpinLock(data):
    # Since values are always inserted after its current possition nothing will enter "in front" of zero.
    # Using this the last value assigned with currentPos == 0 will be just behind zero.
    steps = int(data)
    currentPos = 0
    afterZero = 0
    for i in xrange(1, 50000000):
        currentPos = (steps + currentPos + 1) % i
        if currentPos == 0:
            afterZero = i
    return afterZero


def run(data):
    result = spinLock(data[0])
    resultB = longSpinLock(data[0])
    print '2017 insertions, next value after 2017: {0}\n' \
          '50000000 insertions, next value after 0: {1}'.format(result, resultB)


if __name__ == "__main__":
    run(read('inputs/day17.txt'))
