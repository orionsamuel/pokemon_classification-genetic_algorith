from pandas import read_csv
import numpy as np
from random import randint

db = read_csv("../database/base-pokemon.csv")

# Lista dos pokemon counter
team_selection = []

# Lista de pokemon de entrada
team_target_name = ["Bulbasaur", "Charmander", "Squirtle"]
team_target = []

# Criação aleatória do primeiro time counter
def creat_team():
    for i in range(3):
        team_counter = randint(db.pokedex_number[0],db.pokedex_number.size)
        team_selection.append(team_counter)

# Pega os ID dos pokemon
def getId():
    cont = 0
    while (cont < 3):
        for i in range(db.name.size):
            if(db.name[i] == team_target_name[cont]):
                team_target.append(db.pokedex_number[i])
        cont += 1

def fitness():
    


# main
if __name__ == '__main__':
    creat_team()
    getId()

    print(team_selection)
    print(team_target_name)
    print(team_target)
