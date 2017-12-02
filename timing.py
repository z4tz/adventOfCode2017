import timeit
import os
from InputReader import read

days = xrange(1, len(os.listdir('inputs/'))+1)


def setupstring(day):
    return """
from day{0} import run
from InputReader import read
data = read('inputs/day{0}.txt')""".format(day)

if __name__ == '__main__':
    for day in days:
        data = read('inputs/day{0}.txt'.format(day))
        print("-----## Assignment day {0} ##-----".format(day))
        print("Time used for assignment {0}: {1}s\n\n".format(day, timeit.timeit("run(data)", setup=setupstring(day), number=1)))
