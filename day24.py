from InputReader import read


class BridgeBuilder:
    def __init__(self, data):
        self.possibleBridges = []
        self.parts = [[int(a) for a in line.split('/')] for line in data]
        # create all possible bridges
        self.connectNext(self.parts, 0, 0)

    def connectNext(self, notConnected, nextConnection, strength):
        nothingConnected = True
        for part in notConnected:
            if nextConnection in part:
                nothingConnected = False
                copy = notConnected[:]
                copy.remove(part)
                self.connectNext(copy, part[part.index(nextConnection) - 1], strength + sum(part))
        if nothingConnected:
            self.possibleBridges.append([strength, len(self.parts) - len(notConnected)])

    def strongestBridge(self):
        self.possibleBridges.sort(key=lambda x: x[0])
        return self.possibleBridges[-1][0]

    def longestBridge(self):
        self.possibleBridges.sort(key=lambda x: (x[1], x[0]))
        return self.possibleBridges[-1][0]


def run(data):
    bridgeBuilder = BridgeBuilder(data)
    print 'The strongest bridge is {0} units strong\n' \
          'The longest bridge is {1} units strong' \
        .format(bridgeBuilder.strongestBridge(), bridgeBuilder.longestBridge())


if __name__ == "__main__":
    run(read('inputs/day24.txt'))
