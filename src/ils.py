from pandas import read_csv
import numpy as np
from random import randint

db = read_csv("../database/base-pokemon.csv")

# Lista dos pokemon counter
team_selection = []
best_team_selection = []
best_team_selection_name = []

# Inicialização da avaliação
avaliation_global = 0

# Lista de pokemon de entrada
team_target_name = ["Bulbasaur", "Charmander", "Squirtle"]
team_target = []

# Criação aleatória do primeiro time counter
def creat_team():
    for i in range(3):
        team_counter = randint(db.pokedex_number[0],db.pokedex_number.size)
        team_selection.append(team_counter)

# Retorna o nome do time counter
def name_team_counter():
    cont = 0
    while (cont < 3):
        for i in range(db.pokedex_number.size):
            if(db.pokedex_number[i] == best_team_selection[cont]):
                best_team_selection_name.append(db.name[i])
        cont += 1

# Pega os ID dos pokemon
def getId():
    cont = 0
    while (cont < 3):
        for i in range(db.name.size):
            if(db.name[i] == team_target_name[cont]):
                team_target.append(db.pokedex_number[i])
        cont += 1

# Realiza a batalha entre dois pokemon para saber quem é o mais forte
def pokemon_battle(pokemon1, pokemon2):
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

# Calcula qual é o melhor time
def fitness(team_selection, team_target):
    fitness = 0
    for pokemon_counter in team_selection:
        for pokemon_target in team_target:
            fitness+=pokemon_battle(pokemon_counter, pokemon_target)

    return fitness

# Retorna o melhor time
def return_best_team(avaliation):
    if(fitness(team_selection, team_target) > avaliation):
        avaliation = fitness(team_selection, team_target)
        print(avaliation)
        for i in range(len(team_selection)):
            best_team_selection[i] = team_selection[i]
    else:
        local_search(team_selection)
    return avaliation

# Busca local
def local_search(team_selection):
    print()    

# Função que executa tudo
def run(avaliation):
    creat_team()
    getId()
    for i in team_selection:
        best_team_selection.append(i)
    alaviation = return_best_team(avaliation)
    print(avaliation)
    return avaliation

# main
if __name__ == '__main__':
    
    avaliation_global = run(avaliation_global)
    name_team_counter()

    print("Time Entrada:")
    print(team_target_name)
    print("Time Counter:")
    print(best_team_selection_name)
    print("Fitness")
    print(avaliation_global)
