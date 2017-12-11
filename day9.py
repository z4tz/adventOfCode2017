from InputReader import read
import re


def calcGroups(input):
    input = re.sub('!.?', '', input)
    stringLength = len(input)
    input, n = re.subn('<.*?>', '', input)
    removedGarbage = stringLength - len(input) - 2 * n
    totalScore = 0
    value = 0
    for char in input:
        if char is '{':
            value += 1
            totalScore += value
        elif char is '}':
            value -= 1
    return totalScore, removedGarbage


def run(data):
    result = calcGroups(data[0])
    print('The value of all groups is: {0}\nCharacters removed as garbage: {1}'.format(*result))


if __name__ == "__main__":
    run(read('inputs/day9.txt'))
