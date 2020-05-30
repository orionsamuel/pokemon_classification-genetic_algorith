from random import randrange

from utils import create_team, fitness, mutate_team


# Busca local
def local_search(pokemons, team_selection, iterations=1000):
    """

    :param pokemons: The structure of the Singleton
    :param team_selection: The first generated team to try counter
    :param iterations: The max number of iterations of the local search,
        by default 1000
    :return: A tuple with best team and this fit
    """
    best_evaluation_local = fitness(team_selection, pokemons)
    best_team_selection = team_selection.copy()

    for i in range(iterations):
        mutations = randrange(len(team_selection)) + 1

        while mutations > 0:
            mutations -= 1
            team_selection = mutate_team(team_selection)
        get_fitness = fitness(team_selection, pokemons)

        if get_fitness > best_evaluation_local:
            best_evaluation_local = get_fitness
            best_team_selection = team_selection.copy()

    return best_team_selection, best_evaluation_local


# Função que executa tudo
def run(pokemons, iterations=1000):
    base_team = create_team(list(range(pokemons.get_range())))

    return local_search(pokemons, base_team, iterations)
