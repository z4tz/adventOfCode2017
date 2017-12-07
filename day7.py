from InputReader import read
from collections import Counter


#Part 1
def findBottom(info):
    names = []
    namesAbove = []
    for line in info:
        split = line.replace(',', '').split()
        names.append(split[0])
        namesAbove.extend(split[3:])
    for name in names:
        if name not in namesAbove:
            return name


#Part 2
class Program:
    def __init__(self, weight, programsAbove):
        self.weight = weight
        self.programsAbove = programsAbove
        self.totalWeight = 0  # not calculated yet if zero


programs = {}


def getCorrectWeight(info, bottom):
    for line in info:
        split = line.replace(',', '').split()
        programs[split[0]] = Program(int(split[1][1:-1]), split[3:])
    return wrongWeight(bottom) + getCorrection(bottom)


def wrongWeight(name):
    weights = [getWeight(program) for program in programs[name].programsAbove]
    occurances = Counter(weights).most_common()
    if len(occurances) <= 1:  # either no programs above or weights above are balanced
        return programs[name].weight
    nameOfWrongWeight = programs[name].programsAbove[weights.index(occurances[-1][0])]
    return wrongWeight(nameOfWrongWeight)


def getWeight(name):
    if programs[name].totalWeight > 0:
        return programs[name].totalWeight
    programs[name].totalWeight = programs[name].weight + sum([getWeight(programName) for programName in programs[name].programsAbove])
    return programs[name].totalWeight


def getCorrection(name):
    weights = [getWeight(program) for program in programs[name].programsAbove]
    occurances = Counter(weights).most_common()
    return occurances[0][0]-occurances[1][0]


def run(data):
    bottom = findBottom(data)  #Part 1
    correctWeight = getCorrectWeight(data, bottom)  #Part 2
    print('The bottom program is {0}\nThe correct weight is {1}'.format(bottom, correctWeight))


if __name__ == "__main__":
    run(read('inputs/day7.txt'))
