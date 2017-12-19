from InputReader import read
import numpy as np


class Packet:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self):
        if self.direction == 0:
            self.y -= 1
        elif self.direction == 1:
            self.x += 1
        elif self.direction == 2:
            self.y += 1
        elif self.direction == 3:
            self.x -= 1


def pathLetters(data):
    maxWidth = max([len(line) for line in data])
    arr = np.array([list(line.replace('\n', '').ljust(maxWidth, ' ')) for line in data])  # all lines same length
    packet = Packet(data[0].index('|'), 0, 2)  # find x-coord for start position
    letters = []
    moves = 0
    while ' ' not in arr[packet.y, packet.x]:
        packet.move()
        moves += 1  # first move not counted but counts one move extra at end instead
        if str.isalpha(arr[packet.y, packet.x]):
            letters.append(arr[packet.y, packet.x])
        elif '+' in arr[packet.y, packet.x]:
            if packet.direction % 2:
                if '|' in arr[packet.y-1, packet.x]:
                    packet.direction = 0
                else:
                    packet.direction = 2
            else:
                if '-' in arr[packet.y, packet.x+1]:
                    packet.direction = 1
                else:
                    packet.direction = 3

    return ''.join(letters), moves


def run(data):
    result = pathLetters(data)
    print 'Letters found on the path {0}\n' \
          'Total number of steps {1}'.format(*result)


if __name__ == "__main__":
    run(read('inputs/day19.txt'))