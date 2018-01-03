from InputReader import read
from collections import namedtuple, defaultdict

State = namedtuple('State', 'name write move nextState')


def turingChecksum(data):
    states = {}
    for i in xrange(3, len(data), 10):
        state = createState([line.strip().replace('right', '1').replace('left', '-1') for line in data[i:i + 10]])
        states[state.name] = state
    currentState = states[data[0][-3]]  # startState
    steps = int(data[1].split()[-2])
    currentPos = 0
    tape = defaultdict(int)

    for _ in xrange(steps):
        tapeValue = tape[currentPos]
        tape[currentPos] = currentState.write[tapeValue]
        currentPos += currentState.move[tapeValue]
        currentState = states[currentState.nextState[tapeValue]]

    return sum(tape.values())


def createState(lines):
    name = lines[0][-2]
    write = [int(lines[2][-2]), int(lines[6][-2])]
    move = [int(lines[3][-3:-1]), int(lines[7][-3:-1])]
    nextState = [lines[4][-2], lines[8][-2]]
    return State(name, write, move, nextState)


def run(data):
    result = turingChecksum(data)
    print result


if __name__ == "__main__":
    run(read('inputs/day24.txt'))
