from InputReader import read
import math
import numpy as np


def getDistance(location):
    location = int(location)
    if location == 1:
        return 0
    sideLength = math.ceil(math.sqrt(location))
    if sideLength % 2 == 0:
        sideLength += 1
    diff = sideLength**2-location
    distanceToMiddleOfSide = abs((diff % (sideLength-1)) - (sideLength-1)/2)
    return int(distanceToMiddleOfSide + (sideLength-1)/2)





def getValue(targetValue):
    targetValue = int(targetValue)
    sideLength = int(math.ceil(math.sqrt(targetValue))) + 2
    if sideLength % 2 == 0:
        sideLength += 1

    array = np.zeros((sideLength,sideLength))
    array[sideLength//2, sideLength//2] = 1
    getCoordinates(1, sideLength)
    i = 2
    currentSum = 0
    while currentSum <= targetValue:
        coords = getCoordinates(i, sideLength)
        currentSum = sumNearby(array, coords)
        array[coords[0], coords[1]] = currentSum
        i += 1
    return currentSum

def sumNearby(array, coords):
    return int(sum(sum(array[coords[0] - 1:coords[0] + 2, coords[1] - 1:coords[1] + 2])))


def getCoordinates(number, squareLength):
    if number == 1:
        return [squareLength//2, squareLength//2]
    sideLength = math.ceil(math.sqrt(number))
    if sideLength % 2 == 0:
        sideLength += 1
    diff = sideLength ** 2 - number
    whichSide = diff // (sideLength-1)
    coord = [0, 0]
    if whichSide == 0:
        coord[0] = sideLength-1
        coord[1] = (sideLength-1) - diff % (sideLength - 1)

    elif whichSide == 1:
        coord[1] = 0
        coord[0] = (sideLength - 1) - diff % (sideLength - 1)

    elif whichSide == 2:
            coord[0] = 0
            coord[1] = diff % (sideLength-1)
    else:
        coord[1] = sideLength-1
        coord[0] = diff % (sideLength - 1)
    return [int(x + (squareLength - sideLength)/2) for x in coord]



def run(data):
    print getDistance(data[0])
    print getValue(data[0])

if __name__ == "__main__":
    run(read('inputs/day3.txt'))
