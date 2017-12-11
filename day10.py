from InputReader import read


def knotHash(input):
    data = range(0, 256)
    skipSize = 0
    currentPos = 0
    for length in [int(numstring) for numstring in input.split(',')]:
        data = knot(data, currentPos, length)
        currentPos = (currentPos + length + skipSize) % len(data)
        skipSize += 1
    return data[0] * data[1]


def knotHashB(input):
    data = range(0, 256)
    skipSize = 0
    currentPos = 0
    for i in xrange(64):
        for length in [ord(char) for char in input] + [17, 31, 73, 47, 23]:
            data = knot(data, currentPos, length)
            currentPos = (currentPos + length + skipSize) % len(data)
            skipSize += 1
    dense = []
    for i in xrange(16):
        red = reduce(lambda x, y: x ^ y, data[i*16:i*16+16])
        dense.append(hex(red)[2:].zfill(2))
    return ''.join(dense)


def knot(data, currentPos, length):
    if currentPos + length > len(data)-1:
        tempList = data[:] + data[:(currentPos+length) % len(data)]
    else:
        tempList = data[:]
    tempList[currentPos:currentPos+length] = tempList[currentPos:currentPos+length][::-1]
    if currentPos + length > len(data)-1:
        tempList[:(currentPos + length) % len(data)] = tempList[len(data):]
    return tempList[0:len(data)]


def run(data):
    result = knotHash(data[0])
    resultB = knotHashB(data[0])
    print 'Product of first two numbers: {0}\nKnot hash: {1}'.format(result, resultB)


if __name__ == "__main__":
    run(read('inputs/day10.txt'))
