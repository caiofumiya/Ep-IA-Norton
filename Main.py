from GA import rastrigins_minimization
from Performance import performance_plot
import Printing


# Main Program
Printing.introduction()

previous_fitness = []

while True:
    p_size = int(input('Population Size [1; ~]: '))

    while True:
        m_generations = int(input('Maximum Generations [1; ~]: '))
        k_tournament = int(input(f'Number of Tournament Participants [1; {p_size}]: '))
        crossover_p = float(input('Crossover Probability [0; 1]: '))
        mutation_p = float(input('Mutation Probability [0; 1]: '))
        n_genes = int(input('Number of Genes which will Suffer Mutation(s) [1; 20]: '))

        Printing.starting()

        individual, generation, avg, best = rastrigins_minimization(population_size=p_size,
                                                                    max_generations=m_generations,
                                                                    k_tournament_participants=k_tournament,
                                                                    crossover_probability=crossover_p,
                                                                    mutation_probability=mutation_p,
                                                                    n_genes_mutated=n_genes)

        previous_fitness.append(individual[20])

        Printing.best_individual(individual, previous_fitness, generation)

        Printing.show_values(p_size, m_generations,
                             k_tournament, crossover_p,
                             mutation_p, n_genes)

        performance_plot(avg, best)

        Printing.finishing()

        question = input('\nChange Secondary Params [y/n]? ')
        if question == 'n':
            break
        else:
            Printing.restarting()

    question = input('Change Population Size [y/n]? ')
    if question == 'n':
        break
    else:
        Printing.restarting()

Printing.finishing_program()
