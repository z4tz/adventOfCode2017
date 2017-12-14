from InputReader import read


class Layer:
    def __init__(self, depth):
        self.depth = depth
        self._scannerPositions = range(depth)+range(depth-2, 0, -1)

    def scannerAtTop(self, time):
        return self._scannerPositions[time % len(self._scannerPositions)] == 0


def passFirewall(data):
    firewall = {}
    for line in data:
        split = line.split(':')
        firewall[int(split[0])] = Layer(int(split[1]))
    # Part 1
    severity = 0
    for i in xrange(max(firewall.keys())+1):
        if i in firewall and firewall[i].scannerAtTop(i):
            severity += i*firewall[i].depth
    # Part 2
    delay = 0
    while detected(firewall, delay):
        delay += 1
    return severity, delay


def detected(firewall, delay):
    for i in xrange(max(firewall.keys()) + 1):
        if i in firewall and firewall[i].scannerAtTop(i + delay):
            return True
    return False


def run(data):
    result = passFirewall(data)
    print 'The severity for passing through the firewall at time 0 is: {0}\n' \
          'To avoid detection one must wait {1}ps'.format(*result)


if __name__ == "__main__":
    run(read('inputs/day13.txt'))
