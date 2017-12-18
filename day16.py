from InputReader import read


def danceOrder(data, order=None):
    if order is None:
        order = [chr(num) for num in xrange(ord('a'), ord('p') + 1)]
    for move in data.split(','):
        if 's' in move[0]:
            number = int(move[1:])
            order = order[-number:] + order[:-number]
        elif 'x' in move[0]:
            i, j = [int(pos) for pos in move[1:].split('/')]
            order[i], order[j] = order[j], order[i]
        else:
            i, j = [order.index(pos) for pos in move[1:].split('/')]
            order[i], order[j] = order[j], order[i]
    return order


def danceRepater(data):
    order = [chr(num) for num in xrange(ord('a'), ord('p') + 1)]
    permutatations = []
    while ''.join(order) not in permutatations:
        permutatations.append(''.join(order))
        order = danceOrder(data, order)
    return permutatations[10**9 % len(permutatations)]


def run(data):
    result = danceOrder(data[0])
    resultB = danceRepater(data[0])
    print 'Positions after first dance: "{0}"\n' \
          'Positions after 10^9 repetitions: "{1}"'.format(''.join(result), resultB)


if __name__ == "__main__":
    run(read('inputs/day16.txt'))
