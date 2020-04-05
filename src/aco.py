from pandas import read_csv
import numpy as np
from random import randint

db = read_csv("../database/base-pokemon.csv")

team_target_name = ["Bulbasaur", "Charmander", "Squirtle"]

# Lista de pokemon de entrada
team_target = []

# Pega os ID dos pokemon
cont = 0
while (cont < 3):
    for i in range(db.name.size):
        if(db.name[i] == team_target_name[cont]):
            team_target.append(db.pokedex_number[i])
    cont += 1

# Lista dos pokemon counter
team_selection = []

# Criação aleatória do primeiro time counter
for i in range(3):
    team_counter = randint(db.pokedex_number[0],db.pokedex_number.size)
    team_selection.append(team_counter)

print(team_selection)
print(team_target_name)
print(team_target)

#if __name__ == '__main__':
#main

