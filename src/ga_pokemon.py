from random import choice, randrange

from pyeasyga.pyeasyga import GeneticAlgorithm

from utils import *
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
    db = PokemonsData()
    mutate_index = randrange(len(team))
    team[mutate_index] = choice(db.get_list())


def team_crossover(team1, team2):
    # making two new teams to compose the new generation
    for k in range(randrange(len(team1))):
        tmp = team1[k]
        team1[k] = team2[k]
        team2[k] = tmp

    return [team1, team2]


def team_selection(gen):
    bests = []
    for i in range(len(gen)/5):
        bests.append(gen[i])
    return choice(bests)

def set_team_size(team_length, pokemons):
    """
    :param team_length: size of team target
    :param pokemons: dataset that contains our data
    """
    if team_length > 1:
        pokemons.set_team_size(team_length)
    else:
        pokemons.set_team_size(6)

def run(ga, return_names):
#application of ga
    ga.run()
    best_team = sort_best_team(ga.best_individual()[1], ga.seed_data.get_df())
    best_move_sets = []
    teste = PokemonsData()
    team_target = teste.get_team_target()
    for i in range(len(best_team)):
        if len(team_target) > 1:
            best_move_sets.append(best_typeset_against(best_team[i], team_target[i], ga.seed_data.get_df()))
        else:
            best_move_sets.append(best_typeset_against(best_team[i], team_target[0], ga.seed_data.get_df()))
        if return_names:
            best_team[i] = get_true_pokename(best_team[i], ga.seed_data.get_df())
    return best_team, best_move_sets, ga.best_individual()[0]

def search_counters(team_target, return_names=True):
    """
    Client function
    :param team_target: team that user wants to counter
    :param return_names: if true return the counter team by the names, else return counter team by pokedex number
    application of ga to counter a "team"  and return a tuple:
    tuple[0] -> counter team of "team"
    tuple[1] -> best type for move sets of counter[k] against "team"[k]
    tuple[2] -> fitness, how good is the counter team against "team"
    """
    pokemons = PokemonsData()
    ga = GeneticAlgorithm(pokemons, 50, 20, 0.8, 0.2, True, True)
    ga.create_individual = create_team
    ga.mutate_function = team_mutation
    ga.crossover_function = team_crossover
    ga.selection = team_selection
    ga.fitness_function = fitness
    pokemons.set_team_target(lstr_to_lint(team_target, pokemons.get_df()))
    set_team_size(len(team_target), pokemons)
    return run(ga, return_names)
