import matplotlib.pyplot as plt


def avg_performance(population):
    avg = 0

    for individual in population:
        avg += individual[20] / len(population)

    return avg


def best_performance(population):
    fitness_position = 20
    min_fitness = population[0][fitness_position]
    min_index = 0

    for i in range(0, len(population)):
        if population[i][fitness_position] < min_fitness:
            min_fitness = population[i][fitness_position]
            min_index = i

    individual = population[min_index]

    return individual[fitness_position]


def performance_plot(avg_lst, best_lst):
    plt.plot(range(0, len(avg_lst)), avg_lst, label='Average')
    plt.plot(range(0, len(avg_lst)), best_lst, label='Best')

    plt.xlabel('Generations')
    plt.ylabel('Fitness')

    plt.title('Performance Plot')

    plt.legend()

    plt.show()
