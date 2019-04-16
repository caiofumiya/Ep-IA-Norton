from numpy.random import choice
from random import sample


def mutation_chance(mutation_probability):
    mutation_possibilities = [True, False]

    mutation_occur = mutation_probability
    mutation_doesnt_occur = 1 - mutation_probability

    m = choice(mutation_possibilities, p=[mutation_occur, mutation_doesnt_occur])

    return m


def mutation(child, n):
    mutation_positions = sample(range(len(child) - 1), n)

    for i in range(0, n):
        position = mutation_positions[i]

        if child[position] == 0:
            child[position] = 1
        else:
            child[position] = 0

    return child
