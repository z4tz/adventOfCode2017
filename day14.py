from InputReader import read
from day10 import knotHashB as knotHash
import numpy as np


def usedSpace(data):
    used = 0
    for i in xrange(128):
        key = data + '-{0}'.format(i)
        binaryHash = [bin(int(char, 16))[2:].zfill(4) for char in knotHash(key)]
        used += ''.join(binaryHash).count('1')
    return used


def findRegions(data):
    binaryLists = []
    for i in xrange(128):
        key = data + '-{0}'.format(i)
        binaryHash = ''.join([bin(int(char, 16))[2:].zfill(4) for char in knotHash(key)])
        binaryLists.append([int(numstring) for numstring in binaryHash])
    disk = np.array(binaryLists)
    regions = 0
    for x in range(128):
        for y in range(128):
            if disk[y, x] == 1:
                removeRegion(disk, [y, x])
                regions += 1
    return regions


def removeRegion(disk, startCoord):
    """Identifies all parts of a disk region from a given start coordinate and sets them to zeroes"""
    coordinates = [startCoord]
    while coordinates:
        coord = coordinates.pop()
        coordinates.extend(getNeighbors(disk, coord))
        disk[coord[0], coord[1]] = 0


def getNeighbors(array, coord):
    """Returns the coordinates of the occupied adjacent (not diagonal) disk squares"""
    neighbors = []
    for adj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        try:
            if coord[0] + adj[0] >= 0 and coord[1] + adj[1] >= 0 and array[coord[0] + adj[0], coord[1] + adj[1]] == 1:
                neighbors.append([coord[0] + adj[0], coord[1] + adj[1]])
        except IndexError:
            pass
    return neighbors


def run(data):
    print 'Squares of disk space used: {0}'.format(usedSpace(data[0]))
    print 'Number of regions on the disk: {0}'.format(findRegions(data[0]))


if __name__ == "__main__":
    run(read('inputs/day14.txt'))
