from InputReader import read
import numpy as np
import re
from collections import defaultdict


class Particle:
    def __init__(self, id, position, velocity, acceleration):
        self.id = id
        self.p = position
        self.v = velocity
        self.a = acceleration

    @property
    def distance(self):
        return sum(np.absolute(self.p))

    @property
    def speed(self):
        return sum(np.absolute(self.v))

    @property
    def acceleration(self):
        return sum(np.absolute(self.a))

    def tick(self):
        self.v += self.a
        self.p += self.v


def particleDistance(data):
    particles = []
    regex = re.compile('p=<([-0-9,]+)>, v=<([-0-9,]+)>, a=<([-0-9,]+)>')
    for i, line in enumerate(data):
        groups = regex.match(line).groups()
        particles.append(Particle(i, *[np.array([int(num) for num in group.split(',')]) for group in groups]))

    # Particles with the least acceleration will be closest to origo as t -> inf
    # For equal acceleration, move on to check speed then distance (not true in all edge cases unfortunately)
    particles.sort(key=lambda p: (p.acceleration, p.speed, p.distance))
    origoParticle = particles[0].id

    for _ in xrange(100):  # arbitrary length where all collisions should have occurred
        positions = defaultdict(list)
        for particle in particles:
            positions[tuple(particle.p)].append(particle)  # particles with same position end up on same key in dict
        for position in positions.values():
            if len(position) > 1:
                for particle in position:
                    particles.remove(particle)
        for particle in particles:
            particle.tick()
    return origoParticle, len(particles)


def run(data):
    result = particleDistance(data)
    print 'Particle closest to origo as t->inf: {0}\n' \
          'Particles left after all collisions: {1}'.format(*result)


if __name__ == "__main__":
    run(read('inputs/day20.txt'))
