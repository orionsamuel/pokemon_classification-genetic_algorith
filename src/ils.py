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
teams = []

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
    pokemon1_types = [db.loc[pokemon1-1, "type1"], str(db.loc[pokemon1-1, "type2"])]
    if 'nan' in pokemon1_types: pokemon1_types.remove('nan')
    pokemon2_types = [db.loc[pokemon2-1, "type1"], str(db.loc[pokemon2-1, "type2"])]
    if 'nan' in pokemon2_types: pokemon2_types.remove('nan')
    pokemon1_cp = db.loc[pokemon1-1, "combat_point"]
    pokemon2_cp = db.loc[pokemon2-1, "combat_point"]
    pokemon1_against = []
    pokemon2_against = []
    for tp in pokemon1_types:
        pokemon1_against.append(db.loc[pokemon2-1, "against_"+tp])
    for tp in pokemon2_types:
        pokemon2_against.append(db.loc[pokemon1-1, "against_"+tp])

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
    print("Começa aqui a separação")
    for i in range(len(avaliation)):
        print(str(teams[i]) + " " + str(avaliation[i]))
    

# Busca local
def local_search():
    global best_team_selection
    global team_selection
    best_avaliation_local = 0
    for  i in range(100):
        change_num = randint(1,3)
        for j in range(change_num):
            counter = randint(db.pokedex_number[0],db.pokedex_number.size-2)
            team_selection[j] = counter
        get_fitness = fitness(team_selection, team_target)
        if(get_fitness > best_avaliation_local):
            best_avaliation_local = get_fitness
            best_team_selection = team_selection
            print(str(get_fitness) + " " + str(team_selection) + " " + str(best_team_selection))
    print(team_selection)
    print(best_team_selection)
    return best_avaliation_local, best_team_selection
        

# Função que executa tudo
def run():
    global best_team_selection
    global team_selection
    creat_team()
    getId()
    for i in team_selection:
        best_team_selection.append(i)
    print("Team Target:")
    print(team_target_name)
    best_avaliation, best_team_selection = local_search()
    #return_best_team()
    name_team_counter()
    print("Best Avaliation : " + str(best_avaliation))
    print("Team Counter:")
    print(best_team_selection_name)
    print(best_team_selection)

# main
if __name__ == '__main__':

    
    team_target_name = execInput()
    
    run()

    


    
