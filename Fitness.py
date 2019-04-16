import math
from Truncate import truncate
from termcolor import colored


def fitness(population):
    for individual in population:
        vector = binary_conversion(individual)

        x = vector[0]
        y = vector[1]

        individual.append(fitness_calculation(x, y))

        print(f'{individual[0:20]} - ', end='')
        f_value = str(individual[20])
        f_value = f_value[:10]
        f_value = f_value.ljust(10, '0')
        print(colored(f'{f_value}', attrs=['bold']))

    return population


def fitness_calculation(x, y):
    part1 = 20 + math.pow(x, 2) + math.pow(y, 2)
    part2 = 10 * (math.cos(2 * math.pi * x) + math.cos(2 * math.pi * y))

    rast = part1 - part2

    return rast


def binary_conversion(individual):
    lst_x = individual[0:10]
    lst_y = individual[10:20]

    str_x = ''.join(str(i) for i in lst_x)
    str_y = ''.join(str(i) for i in lst_y)

    calc_x = int(str_x, 2) * 0.00978 - 5
    calc_y = int(str_y, 2) * 0.00978 - 5

    x = truncate(calc_x, 2)
    y = truncate(calc_y, 2)

    return [x, y]

