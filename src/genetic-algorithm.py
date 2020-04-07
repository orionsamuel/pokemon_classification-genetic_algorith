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

db = read_csv("database/base-pokemon.csv")
pokemons = list(db["pokedex_number"])
ga = GeneticAlgorithm(pokemons, 50, 20, 0.8, 0.2, True, True)
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
        if element.isnumeric():
            ilist.append(int(element))
        else:
            ilist.append(pokename_to_pokenumber(element))
    return ilist


def create_team(pokemons):
#creating a team of 3 (individual)
    return [random.choice(pokemons), random.choice(pokemons), random.choice(pokemons)]

ga.create_individual = create_team

def team_mutation(team):
#this function will mutate a team acording mutation tax, creating a new team in scope (mutation)
    mutate_index = random.randrange(len(team))
    team[mutate_index] = random.choice(pokemons)

ga.mutate_function = team_mutation

def team_crossover(teamA, teamB):
#making two new teams to compose the new generation
    for k in range(random.randrange(len(teamA))):
        tmp = teamA[k]
        teamA[k] = teamB[k]
        teamB[k] = tmp
    return [teamA, teamB]

ga.crossover_function = team_crossover

def team_selection(gen):
    return random.choice(gen)

ga.selection = team_selection

def pokemon_validation(pokemon):
#validation for meltan and melmetal in our database
    if pokemon == 808:
        return 649
    elif pokemon == 809:
        return 650
    else:
        return pokemon - 1

def pokemon_validation_reverse(pokemon):
#pokemon_validation ^-1
    if pokemon == 649:
        return 808
    elif pokemon == 650:
        return 809
    else:
        return pokemon + 1


def pokemon_battle(pokemon1, pokemon2):
    """
    return the result os a battle between two pokemons:
    if result>0 => pokemon1 wins,
    if result<0 => pokemon2 wins,
    case result = 0, means possibly occurred a draw
    
    """
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
#fitness function will generate a value to rank each team (fitness)
    fitness = 0
    for pokemon_counter in individual:
        for pokemon_target in team_target:
            fitness+=pokemon_battle(pokemon_counter, pokemon_target)

    return fitness

ga.fitness_function = fitness

def pokename_to_pokenumber(pokename):
#receive a pokemon name, returns his pokedex number
    for i in range(len(db["name"])):
        if pokename==db["name"][i]:
            return db.pokedex_number[i]

def pokenumber_to_pokename(pokenumber):
#receive a pokedex_number, returns his pokemon name
    for i in range(len(db["pokedex_number"])):
        if pokenumber==db["pokedex_number"][i]:
            return db.name[i]

def is_sorted_by_CP_reverse(team):
#verify if a team is sorted by CP in a reverse way (higher to lower)
    for index in range(len(team)-1):
        if(db.loc[team[index], "combat_point"] < db.loc[team[index+1], "combat_point"]):
            return False
    return True

def sort_by_cp_reverse(team):
#sort a team by the CP, higher to lower (reverse)
    for x in range(len(team)):
        team[x] = pokemon_validation(team[x])
    tmp = None
    while not is_sorted_by_CP_reverse(team):
        for index in range(len(team)-1):
            if db.loc[team[index], "combat_point"] < db.loc[team[index+1], "combat_point"]:
                tmp = team[index]
                team[index] = team[index+1]
                team[index+1] = tmp
    for x in range(len(team)):
        team[x] = pokemon_validation_reverse(team[x])
    return team

def best_against(team, target):
#select the best pokemon of a team against one pokemon target
    result = []
    if len(team)>1:
        for pokemon in team:
            result.append(pokemon_battle(pokemon, target))
        return team[result.index(max(result))]
    else:
        return team[0]

def sort_best_team(counter):
#sort the counter team to the best way against team target
    target = sort_by_cp_reverse(team_target.copy())
    counter_copy = counter.copy()
    for index in range(len(target)):
        counter[index] = best_against(counter_copy, target[index])
        counter_copy.remove(counter[index])
    tmp = None
    for k in team_target:
        tmp = counter[team_target.index(k)]
        counter[team_target.index(k)] = counter[target.index(k)]
        counter[target.index(k)] = tmp
    return counter

def best_typeset_against(pokemon1, pokemon2):
    pokemon1 = pokemon_validation(pokemon1)
    pokemon2 = pokemon_validation(pokemon2)
    pokemon1_types = [db.loc[pokemon1, "type1"], str(db.loc[pokemon1, "type2"])]
    if 'nan' in pokemon1_types: pokemon1_types.remove('nan')
    pokemon1_against = []
    for tp in pokemon1_types:
        pokemon1_against.append(db.loc[pokemon2, "against_"+tp])

    return pokemon1_types[pokemon1_against.index(max(pokemon1_against))]


def search_counters():
#application of ga
    ga.run()
    best_team = sort_best_team(ga.best_individual()[1])
    for i in range(len(best_team)):
        print(pokenumber_to_pokename(best_team[i])+" ("+best_typeset_against(best_team[i], team_target[i])+" typeset)")
    print(ga.best_individual()[0])

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
