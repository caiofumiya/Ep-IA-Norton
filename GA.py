from Population import population
from Fitness import fitness
from Selection import selection
from Crossover import single_point_crossover
from Cloning import cloning_probability, cloning_best_parent
from Mutation import mutation_chance, mutation
from Performance import avg_performance, best_performance
from termcolor import colored


def rastrigins_minimization(population_size,
                            max_generations,
                            k_tournament_participants,
                            crossover_probability,
                            mutation_probability,
                            n_genes_mutated):

    print(colored('\nInitial Population...\n', attrs=['bold']))

    initial_population = population(population_size)
    population_fitness = fitness(initial_population)

    avg = []
    best = []

    avg_fitness = avg_performance(population_fitness)
    best_fitness = best_performance(population_fitness)

    avg.append(avg_fitness)
    best.append(best_fitness)

    generations = 0

    while (generations < max_generations) and (minimum_found(population_fitness) is False):
        print(colored(f'\nGeneration {generations+1}...\n', attrs=['bold']))

        new_population = []

        for i in range(0, population_size):
            parents_selected = selection(population_fitness, k_tournament_participants)

            if crossover_probability >= cloning_probability():
                child = single_point_crossover(parents_selected)
            else:
                child = cloning_best_parent(parents_selected)

            if mutation_chance(mutation_probability):
                mutation(child, n_genes_mutated)

            new_population.append(child[:])

        population_fitness = fitness(new_population)
        generations += 1

        avg_fitness = avg_performance(population_fitness)
        best_fitness = best_performance(population_fitness)

        avg.append(avg_fitness)
        best.append(best_fitness)

    return minimum(population_fitness), generations, avg, best


def minimum(pop):
    fitness_position = 20
    min_fitness = pop[0][fitness_position]
    min_index = 0

    for i in range(0, len(pop)):
        if pop[i][fitness_position] < min_fitness:
            min_fitness = pop[i][fitness_position]
            min_index = i

    individual = pop[min_index]

    return individual


def minimum_found(pop):
    fitness_position = 20

    for individual in pop:
        if individual[fitness_position] == 0:
            return True

    return False
