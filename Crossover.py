from random import randint


def single_point_crossover(parents):
    parent1 = parents[0]
    parent2 = parents[1]

    parents_size = len(parent1)
    crossover_point = randint(1, parents_size - 1)

    parent1_genes = parent1[0:crossover_point]
    parent2_genes = parent2[crossover_point:parents_size - 1]

    child = parent1_genes[:] + parent2_genes[:]

    return child
