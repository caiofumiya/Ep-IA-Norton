from termcolor import colored
from Fitness import binary_conversion


def introduction():
    print(colored('\n[!] Starting Rastrigins Minimization Process...\n', 'red', attrs=['bold']))
    print('Type below the params of the algorithm: \n')
    print(colored('(*) It\'s important to, for each population size defined,', 'green', attrs=['bold']))
    print(colored('variate the other (secondary) params to reach better results.\n', 'green', attrs=['bold']))


def starting():
    print(colored('\nStarting...', 'red', attrs=['bold']))


def finishing():
    print(colored('Minimization Completed!', 'red', attrs=['bold']))


def restarting():
    print(colored('\nRestarting...\n', 'red', attrs=['bold']))


def finishing_program():
    print(colored('\nThe Process is Over!', 'red', attrs=['bold']))


def best_individual(individual, previous_fitness, generation):
    print(colored('\nBest Individual Achieved:\n', 'green', attrs=['bold']))

    print(f'Binary Chromosome: {individual[0:20]}')
    print(f'Binary Coordinates: {individual[0:10]}, {individual[10:20]}')

    coordinates = binary_conversion(individual)
    print(f'Real Coordinates: ({coordinates[0]}, {coordinates[1]})')

    print(colored('\nFitness:\n', 'green', attrs=['bold']))

    print(colored(f'Current = {individual[20]} - Generation {generation}', attrs=['bold']))
    for i in range(0, len(previous_fitness) - 1):
        print(f'{i+1}º Fitness = {previous_fitness[i]}')


def n_generations(generations):
    return generations


def show_values(p_size, m_generations, k_tournament, crossover_p, mutation_p, n_genes):
    print(colored('\nValues Used: \n', 'green', attrs=['bold']))
    print(colored(f'Population Size = {p_size}', attrs=['bold']))
    print(colored(f'Maximum Generations = {m_generations}', attrs=['bold']))
    print(colored(f'Number of Tournament Participants = {k_tournament}', attrs=['bold']))
    print(colored(f'Crossover Probability = {crossover_p}', attrs=['bold']))
    print(colored(f'Mutation Probability = {mutation_p}', attrs=['bold']))
    print(colored(f'Number of Genes which will Suffer Mutation(s) = {n_genes}\n', attrs=['bold']))
