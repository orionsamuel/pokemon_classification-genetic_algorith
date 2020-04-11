from random import randint

from utils import (create_team, exec_input, fitness, get_db, get_pokename)

db = get_db("base-pokemon")

# Lista dos pokemon counter
team_selection = []
best_team_selection = []
best_team_selection_name = []

meltan = "Meltan"
melmetal = "Melmetal"

# Lista de pokemon de entrada
team_target_name = []
team_target = []


# Pega os ID dos pokemon
def get_id():
    cont = 0

    while cont < 3:
        for i in range(db.name.size):
            if db.name[i] == team_target_name[cont]:
                team_target.append(db.pokedex_number[i])
        cont += 1


def pokemon_validation(pokemon=list(range(len(get_db("base-pokemon"))))):
    # validation for meltan and melmetal in our database

    if pokemon == 808:
        return 650
    elif pokemon == 809:
        return 651
    else:
        return pokemon


# Busca local
def local_search():
    global best_team_selection
    global team_selection
    best_avaliation_local = 0

    for i in range(1000):
        change_num = randint(1, 3)

        for j in range(change_num):
            counter = randint(db.pokedex_number[0], db.pokedex_number.size)
            team_selection[j] = counter
        get_fitness = fitness(team_selection, team_target, db)

        if get_fitness > best_avaliation_local:
            best_avaliation_local = get_fitness
            best_team_selection = team_selection.copy()

    return best_avaliation_local, best_team_selection


# Função que executa tudo
def run():
    global best_team_selection
    global team_selection
    pokemons = range(len(db.pokedex_number))
    create_team(pokemons)
    get_id()

    for i in team_selection:
        best_team_selection.append(i)
    print("Team Target:")
    print(team_target_name)
    best_evaluation, best_team_selection = local_search()
    for pokemon in best_team_selection:
        print(get_pokename(pokemon, db))
    print("Best Evaluation : " + str(best_evaluation))
    print("Team Counter:")
    print(best_team_selection_name)
    print(best_team_selection)


# main

if __name__ == '__main__':
    team_target_name = exec_input()
    run()
