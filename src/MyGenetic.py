from random import choice, randrange

from dataset import PokemonsData
from pyeasyga.pyeasyga import GeneticAlgorithm
from utils import create_team, fitness
"""
ga = pyeasyga.GeneticAlgorithm(data,
                               population_size=10,
                               generations=20,
                               crossover_probability=0.8,
                               mutation_probability=0.05,
                               elitism=True,
                               maximise_fitness=True)
"""


def team_mutation(team):
    """ this function will mutate a team according mutation tax, creating a new
    team in scope (mutation)"""
    db = PokemonsData()
    mutate_index = randrange(len(team))
    team[mutate_index] = choice(range(db.get_range()))


def team_crossover(team1, team2):
    # making two new teams to compose the new generation

    for k in range(randrange(len(team1))):
        tmp = team1[k]
        team1[k] = team2[k]
        team2[k] = tmp

    return [team1, team2]


def team_selection(gen):
    bests = []

    for i in range(len(gen) // 5):
        bests.append(gen[i])

    return choice(bests)


def search_counters(pokemons):
    """
    Client function
    :param pokemons: A PokemonData object
    application of ga to counter a "team"  and return a tuple:
    tuple[0] -> counter team of "team"
    tuple[1] -> best type for move sets of counter[k] against "team"[k]
    tuple[2] -> fitness, how good is the counter team against "team"
    """
    ga = GeneticAlgorithm(list(range(pokemons.get_range())), 50, 20, 0.8, 0.2,
                          True, True)
    ga.create_individual = create_team
    ga.mutate_function = team_mutation
    ga.crossover_function = team_crossover
    ga.selection = team_selection
    ga.fitness_function = fitness
    # application of ga
    ga.run()

    return ga.best_individual()[1], ga.best_individual()[0]
