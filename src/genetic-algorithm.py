import ga
import pandas
import random
import sys

db = pandas.read_csv("database/base-pokemon.csv")

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

def base_gen_generator(length):
#set a new base generation with a "lentgh" of this first population (first gen)
    base_gen = []
    pokemons = list(db["pokedex_number"])
    for i in range(length):
        new_team = [random.choice(pokemons), random.choice(pokemons), random.choice(pokemons)]
        base_gen.append(new_team)
    return base_gen

def team_crossover(teamA, teamB):
#making two new teams to compose the new generation
    for k in range(0):
        tmp = teamA[k]
        teamA[k] = teamB[k]
        teamB[k] = tmp
    return [teamA, teamB]

def new_gen_generator(base_gen):
#set a new generation based on previous generation "base_gen" (crossover)
    new_gen = base_gen
    crossover_tax = 80
    crossovers_times = (len(base_gen)*crossover_tax)/200
    for k in range(int(crossovers_times)):
        random_team_A = random.choice(base_gen)
        base_gen.remove(random_team_A)
        random_team_B = random.choice(base_gen)
        base_gen.remove(random_team_B)
        new_teams = team_crossover(random_team_A, random_team_B)
        new_gen.append(new_teams[0])
        new_gen.append(new_teams[1])
    return new_gen


def fitness(gen):
#em produção
    return

def search_counters(team):
#application of ga
    base_gen = base_gen_generator(5)
    new_gen = new_gen_generator(base_gen)
    pokemons = list(db["pokedex_number"])
    while fitness(new_gen):
        base_gen = new_gen
        new_gen = new_gen_generator(base_gen)

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
    search_counters(team_target)
