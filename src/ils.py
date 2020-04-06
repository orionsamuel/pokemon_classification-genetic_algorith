from pandas import read_csv
from random import randint
import sys

db = read_csv("../database/base-pokemon.csv")

# Lista dos pokemon counter
team_selection = []
best_team_selection = []
best_team_selection_name = []

# Inicialização da avaliação
#avaliation_global = 0
avaliation_full = []
avaliation = []

# Lista de pokemon de entrada
team_target_name = []
team_target = []

# Recebe como entrada os pokemon
def execInput():
    print("Let's input  Pokomeon GO team or a boss raid to counter!")
    team = input("Input your team by pokedexID spliting by " "(space): ")
    return team.split(" ")

# Criação aleatória do primeiro time counter
def creat_team():
    for i in range(3):
        team_counter = randint(db.pokedex_number[0],db.pokedex_number.size-1)
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
def return_best_team():
    for i in range(len(avaliation_full)):
        avaliation.append(avaliation_full[i][0])
    best_avaliation = max(avaliation)
    for i in range(len(avaliation_full)):
        if(avaliation_full[i][0] == best_avaliation):
            for j in range(3):
                best_team_selection[j] = avaliation_full[i][1][j]
    print("Melhor avaliação: " + str(best_avaliation))

# Busca local
def local_search(team_selection):
    for  i in range(220):
        change_num = randint(1,3)
        for i in range(change_num):
            counter = randint(db.pokedex_number[0],db.pokedex_number.size-1)
            team_selection[i] = counter
        avaliation_full.append(((fitness(team_selection, team_target)),team_selection))
        

# Função que executa tudo
def run():
    creat_team()
    getId()
    for i in team_selection:
        best_team_selection.append(i)
    print("Time Entrada:")
    print(team_target_name)
    local_search(team_selection)
    return_best_team()
    name_team_counter()
    print("Time Counter:")
    print(best_team_selection_name)

# main
if __name__ == '__main__':

    
    team_target_name = execInput()
    
    run()

    
