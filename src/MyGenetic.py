from random import choice, randrange

from pyeasyga.pyeasyga import GeneticAlgorithm

from utils import create_team, fitness, get_pokename
from dataset import PokemonsData

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
    mutate_index = randrange(len(team))
    team[mutate_index] = choice(pokemons)


def team_crossover(team1, team2):
    # making two new teams to compose the new generation
    for k in range(randrange(len(team1))):
        tmp = team1[k]
        team1[k] = team2[k]
        team2[k] = tmp

    return [team1, team2]


def team_selection(gen):
    return choice(gen)


def search_counters(team_target, pokemons):
    print(team_target)
    ga = GeneticAlgorithm(pokemons, 50, 15, 0.8, 0.2, True, True)
    ga.create_individual = create_team
    ga.mutate_function = team_mutation
    ga.crossover_function = team_crossover
    ga.selection = team_selection
    ga.fitness_function = fitness
    # application of ga
    ga.run()
    print(team_target)


    for pokemon in ga.best_individual()[1]:
        print(get_pokename(pokemon))
    print(ga.best_individual()[0])
