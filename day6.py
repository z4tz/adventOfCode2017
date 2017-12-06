from InputReader import read


def findLoop(memoryBanks):
    memoryBanks = [int(numString) for numString in memoryBanks.split()]
    history = []
    loops = 0
    while memoryBanks not in history:
        loops += 1
        history.append(memoryBanks[:])
        redistribute(memoryBanks)
    return [loops, len(history) - history.index(memoryBanks)]


def redistribute(memoryBanks):
    blocks = max(memoryBanks)
    index = memoryBanks.index(blocks)
    memoryBanks[index] = 0
    for i in range(index+1,index+1+blocks):
        memoryBanks[i % len(memoryBanks)] += 1
    return memoryBanks


def run(data):
    print 'Loop detected after {0} cycles\nLoop length: {1}'.format(*findLoop(data[0]))


if __name__ == "__main__":
    run(read('inputs/day6.txt'))
