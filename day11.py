from InputReader import read
import numpy as np

directions = {'n' : np.array([1, 0, -1]),
              'ne': np.array([1, -1, 0]),
              'se': np.array([0, -1, 1]),
              's' : np.array([-1, 0, 1]),
              'sw': np.array([-1, 1, 0]),
              'nw': np.array([0, 1, -1])}


def getDistance(input):
    position = np.array([0, 0, 0])
    maxDistance = 0
    for move in input.split(','):
        position += directions[move]
        maxDistance = max(maxDistance, max(np.abs(position)))
    return max(np.abs(position)), maxDistance


def run(data):
    result = getDistance(data[0])
    print result


if __name__ == "__main__":
    run(read('inputs/day11.txt'))
