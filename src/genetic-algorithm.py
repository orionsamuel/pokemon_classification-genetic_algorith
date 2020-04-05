from pyeasyga.pyeasyga  import GeneticAlgorithm
from pandas import read_csv
import random
import sys
"""
ga = pyeasyga.GeneticAlgorithm(data,
                               population_size=10,
                               generations=20,
                               crossover_probability=0.8,
                               mutation_probability=0.05,
                               elitism=True,
                               maximise_fitness=True)
"""

db = read_csv("../database/base-pokemon.csv")
pokemons = list(db["pokedex_number"])
ga = GeneticAlgorithm(pokemons, 20, 20, 0.8, 0, False, True)
team_target = None

def execInput():
#read the executation input if it exists (aux)
    print("Let's input  Pokomeon GO team or a boss raid to counter!")
    team = input("Input your team by pokedexID spliting by " "(space): ")
    return team.split(" ")

def lstr_to_lint(slist): 
#cast list of strings to a list of integers (aux)
    ilist = []
    for element in slist:
        ilist.append(int(element))
    return ilist


def create_team(pokemons):
#creating a team of 3 (individual)
    return [random.choice(pokemons), random.choice(pokemons), random.choice(pokemons)]

ga.create_individual = create_team

def team_crossover(teamA, teamB):
#making two new teams to compose the new generation
    for k in range(0):
        tmp = teamA[k]
        teamA[k] = teamB[k]
        teamB[k] = tmp
    return [teamA, teamB]

ga.crossover_function = team_crossover

def team_selection(gen):
    return random.choice(gen)

ga.selection = team_selection

def pokemon_validation(pokemon):
    if pokemon == 808:
        return 649
    elif pokemon == 809:
        return 650
    else:
        return pokemon - 1

def pokemon_validation_reverse(pokemon):
    if pokemon == 649:
        return 808
    elif pokemon == 650:
        return 809
    else:
        return pokemon + 1


def pokemon_battle(pokemon1, pokemon2):
    pokemon1 = pokemon_validation(pokemon1)
    pokemon2 = pokemon_validation(pokemon2)
    pokemon1_types = [db.loc[pokemon1, "type1"], str(db.loc[pokemon1, "type2"])]
    if 'nan' in pokemon1_types: pokemon1_types.remove('nan')
    pokemon2_types = [db.loc[pokemon2, "type1"], str(db.loc[pokemon2, "type2"])]
    if 'nan' in pokemon2_types: pokemon2_types.remove('nan')
    pokemon1_cp = db.loc[pokemon1, "combat_point"]
    pokemon2_cp = db.loc[pokemon2, "combat_point"]
    pokemon1_against = []
    pokemon2_against = []
    for tp in pokemon1_types:
        pokemon1_against.append(db.loc[pokemon2, "against_"+tp])
    for tp in pokemon2_types:
        pokemon2_against.append(db.loc[pokemon1, "against_"+tp])

    pokemon1_against.sort(reverse=True)
    pokemon2_against.sort(reverse=True)

    return pokemon1_cp*pokemon1_against[0] - pokemon2_cp*pokemon2_against[0]

def fitness(individual, pokemons):
    fitness = 0
    for pokemon_counter in individual:
        for pokemon_target in team_target:
            fitness+=pokemon_battle(pokemon_counter, pokemon_target)

    return fitness

ga.fitness_function = fitness

def search_counters():
#application of ga
    ga.run()
    print(list(ga.last_generation()))
    print(ga.best_individual())

if __name__ == '__main__':
#main
    team_target = []
    if len(sys.argv)<4:
        team_target = lstr_to_lint(execInput())
        
    elif len(sys.argv)==4:
        del sys.argv[0]
        team_target = lstr_to_lint(sys.argv)
        
    else:
        print("Bad input!")
        exit()
    search_counters()
