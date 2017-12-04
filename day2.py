from InputReader import read


def calcChecksum(matrix):
    checksum = 0
    for row in matrix:
        numbers = [int(numString) for numString in row.split('\t')]
        checksum += max(numbers) - min(numbers)
    return checksum


def calcChecksumB(matrix):
    checksum = 0
    for row in matrix:
        checksum += findEvenDivision([int(numString) for numString in row.split('\t')])
    return checksum


def findEvenDivision(numbers):
    for i in xrange(0,len(numbers)):
        for j in xrange(0,len(numbers)):
            if i != j and numbers[i] % numbers[j] == 0:
                return numbers[i]/numbers[j]


def run(data):
    print calcChecksum(data)
    print calcChecksumB(data)


if __name__ == "__main__":
    run(read('inputs/day2.txt'))