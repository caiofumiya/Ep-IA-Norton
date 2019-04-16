from random import randint


def selection(pop_fitness, k):
    parent1 = tournament_selection(pop_fitness, k)
    parent2 = tournament_selection(pop_fitness, k)

    parents = [parent1[:], parent2[:]]

    return parents


def tournament_selection(pop_fitness, k):
    participants = []

    for i in range(0, k):
        random_individual = randint(0, len(pop_fitness) - 1)
        participants.append(pop_fitness[random_individual])

    winner = tournament_winner(participants)

    return winner


def tournament_winner(participants):
    fitness_position = 20
    min_fitness = participants[0][fitness_position]
    min_index = 0

    for i in range(0, len(participants)):
        if participants[i][fitness_position] < min_fitness:
            min_fitness = participants[i][fitness_position]
            min_index = i

    winner = participants[min_index]

    return winner
