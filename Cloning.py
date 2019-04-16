from random import uniform


def cloning_best_parent(parents):
    parent1 = parents[0]
    parent2 = parents[1]

    fitness_position = 20

    if parent1[fitness_position] < parent2[fitness_position]:
        clone = parent1[0:fitness_position]
    else:
        clone = parent2[0:fitness_position]

    return clone


def cloning_probability():
    r = uniform(0, 1)

    return r
