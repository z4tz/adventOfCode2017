from InputReader import read


def stepsToOutside(instructionList):
    instructionList = [int(numString) for numString in instructionList]
    nextStep = 0
    steps = 0
    while 0 <= nextStep < len(instructionList):
        instructionList[nextStep] += 1
        nextStep += instructionList[nextStep]-1
        steps += 1
    return steps

def stepsToOutsideB(instructionList):
    instructionList = [int(numString) for numString in instructionList]
    nextStep = 0
    steps = 0
    while 0 <= nextStep < len(instructionList):
        if instructionList[nextStep] >= 3:
            instructionList[nextStep] -= 1
            nextStep += instructionList[nextStep] + 1
        else:
            instructionList[nextStep] += 1
            nextStep += instructionList[nextStep]-1
        steps += 1
    return steps


def run(data):
    print stepsToOutside(data)
    print stepsToOutsideB(data)


if __name__ == "__main__":
    run(read('inputs/day5.txt'))