from random import randint


def population(size):
    inhabitants = []

    for i in range(0, size):
        inhabitants.append(individual()[:])

    return inhabitants


def individual():
    x = coordinates()
    y = coordinates()

    person = x[:] + y[:]

    return person


def coordinates():
    coord = []

    for i in range(0, 10):
        coord.append(randint(0, 1))

    return coord
