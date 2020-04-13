from time import time

from MyGenetic import search_counters
from utils import get_db, lstr_to_lint
from dataset import PokemonsData
import csv


def write_csv(name, values):
    try:
        with open(name, "w", encoding="UTF-8") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(values)
        csvFile.close()
    except IOError:
        print("Invalid name")
        raise


# lista = []
def get_fitness(t):
    return t[1]

pokemons = PokemonsData()
counters = get_db("teams", header=None, sep=" ")

for index, steam in counters.iterrows():
    team_target = lstr_to_lint(steam, pokemons.get_df())
    pokemons.set_team_target(team_target)
    start = []
    stop = []
    genetic_results = []
    search_results = []
    if index == 0:
        for i in range(5):
            start.append(time())
            genetic_results.append(search_counters(pokemons))
            stop.append(time())
            ## Salvando em lista
            genetic_results.sort(key=get_fitness, reverse=True)
            write_csv("team_fit_genetic.csv", genetic_results)  ## Fazendo um append
    else:
        break
print("FINISH!")