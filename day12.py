from InputReader import read
from Queue import Queue


def getPrograms(data):
    """Returns a dict with programs as keys and connected programs as values
    Example data line:
    '5 <-> 109, 628, 1133, 1605'
    """
    programs = {}
    for line in data:
        split = line.split(' <-> ')
        programs[int(split[0])] = [int(numstring) for numstring in split[1].split(', ')]
    return programs


def findConnected(programs, startKey = 0):
    """Returns a set with all connected programs (direct and indirect).
    startKey defines what program to start looking for connections from.
    """
    connectedPrograms = {startKey}
    lookupQueue = Queue()
    lookupQueue.put(startKey)
    while not lookupQueue.empty():
        newConnected = programs[lookupQueue.get()]
        for program in newConnected:
            if program not in connectedPrograms:
                connectedPrograms.add(program)
                lookupQueue.put(program)
    return connectedPrograms


def findGroups(programs):
    """Returns how many groups of programs can be found in the programs dictionary given.
    A group consists of all programs connected to each other."""
    groups = 0
    while len(programs) > 0:
        group = findConnected(programs, programs.keys()[0])
        for program in group:
            del programs[program]
        groups += 1
    return groups


def run(data):
    programs = getPrograms(data)
    result = len(findConnected(programs))
    resultB = findGroups(programs)
    print 'Program 0 is connected to {0} programs (including itself).\n' \
          'There are {1} communication groups.'.format(result, resultB)


if __name__ == "__main__":
    run(read('inputs/day12.txt'))
