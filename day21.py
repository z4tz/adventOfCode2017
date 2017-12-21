from InputReader import read
import numpy as np


class Rule:
    def __init__(self, pattern, output):
        self.output = output
        self.patterns = []
        self._patternPermutations(pattern)

    def _patternPermutations(self, pattern):
        self._addPatternRotations(pattern)
        pattern = np.fliplr(pattern)
        self._addPatternRotations(pattern)

    def _addPatternRotations(self, pattern):
        for _ in xrange(4):
            pattern = np.rot90(pattern)
            if not self.patternExists(pattern):
                self.patterns.append(pattern.copy())

    def patternExists(self, pattern):
        for p in self.patterns:
            if np.array_equal(p, pattern):
                return True
        return False


rules = []


def fractalArtSize(data):
    for line in data:
        split = line.replace('#', '1').replace('.', '0').split()
        pattern = np.array([[int(char) for char in row] for row in split[0].split('/')])
        output = np.array([[int(char) for char in row] for row in split[2].split('/')])
        rules.append(Rule(pattern, output))

    pattern = np.array([[int(char) for char in row] for row in '010/001/111'.split('/')])
    results = []
    for iteration in xrange(0, 18):
        patternLength = len(pattern)
        sLen = patternLength % 2 + 2  # sidelength of subarray to be identified (2/3)
        outputs = []
        for i in xrange(patternLength/sLen):
            outputs.append([])
            for j in xrange(patternLength/sLen):
                # selects each subarray and identifies output pattern
                outputs[i].append(getOutputPattern(pattern[i*sLen:(i+1)*sLen, j*sLen:(j+1)*sLen]))
        # combines output arrays for each row which are then stacked
        pattern = np.vstack([np.concatenate(row, axis=1) for row in outputs])
        results.append(np.sum(pattern))

    return results[4], results[17]


def getOutputPattern(pattern):
    for rule in rules:
        if rule.patternExists(pattern):
            return rule.output


def run(data):
    result = fractalArtSize(data)
    print 'After 5 iterations {0} pixels are on\n' \
          'After 18 iterations {1} pixels are on'.format(*result)


if __name__ == "__main__":
    run(read('inputs/day21.txt'))
