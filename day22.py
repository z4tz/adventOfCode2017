from InputReader import read
from collections import defaultdict


class Virus:
    def __init__(self, x, y):
        self.position = x + y * 1j
        self.direction = 0 - 1j  # start facing up

    def move(self):
        self.position += self.direction

    def turnLeft(self):
        self.direction *= -1j

    def turnRight(self):
        self.direction *= 1j

    def turn180(self):
        self.direction *= -1


def infectedNodes(data):
    infected = getInfectedNodes(data)
    startCoord = len(data[0].strip())/2
    virus = Virus(startCoord, startCoord)
    infectionsCaused = 0
    for _ in xrange(10000):
        if infected[virus.position]:
            virus.turnRight()
            del infected[virus.position]
        else:
            virus.turnLeft()
            infected[virus.position] = 1
            infectionsCaused += 1
        virus.move()
    return infectionsCaused


def infectedNodesB(data):
    infected = getInfectedNodes(data, 2)
    startCoord = len(data[0].strip())/2
    virus = Virus(startCoord, startCoord)

    infectionsCaused = 0
    for _ in xrange(10000000):
        if infected[virus.position] == 1:  # weakened
            infected[virus.position] += 1
            infectionsCaused += 1
        elif infected[virus.position] == 2:  # infected
            virus.turnRight()
            infected[virus.position] += 1
        elif infected[virus.position] == 3:  # flagged
            virus.turn180()
            del infected[virus.position]
        else:  # clean
            virus.turnLeft()
            infected[virus.position] = 1
        virus.move()
    return infectionsCaused


def getInfectedNodes(data, infectionValue = 1):
    infected = defaultdict(int)
    for y, line in enumerate(data):
        for x, node in enumerate(line.strip()):
            if '#' in node:
                infected[x + y * 1j] = infectionValue
    return infected


def run(data):
    result = infectedNodes(data)
    resultsB = infectedNodesB(data)
    print result, resultsB


if __name__ == "__main__":
    run(read('inputs/day22.txt'))
