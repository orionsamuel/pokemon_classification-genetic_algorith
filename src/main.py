from time import time

from dataset import PokemonsData
from ils import run
from memetic import memetic_search
from MyGenetic import search_counters
from pandas import DataFrame
from utils import get_db, lstr_to_lint, save_data

pokemons = PokemonsData()
counters = get_db("teams", header=None, sep=" ")
columns = ["time", "teams", "fitness"]
genetic = DataFrame(columns=columns)
memetic = DataFrame(columns=columns)
local = DataFrame(columns=columns)

for index, steam in counters.iterrows():
    team_target = lstr_to_lint(steam, pokemons.get_df())
    pokemons.set_team_target(team_target)

    for _ in range(5):
        start = time()
        search_team, search_fit = search_counters(pokemons)
        stop = time()
        row = DataFrame({
            "time": [round(stop - start, 2)],
            "teams": [str(search_team).replace(', ', '-')],
            "fitness": [search_fit]
        })
        genetic = genetic.append(row, ignore_index=True)
        start = time()
        search_team, search_fit = run(pokemons)
        stop = time()
        row = DataFrame({
            "time": [round(stop - start, 2)],
            "teams": [str(search_team).replace(', ', '-')],
            "fitness": [search_fit]
        })
        local = local.append(row, ignore_index=True)
        start = time()
        search_team, search_fit = memetic_search(pokemons, 50)
        stop = time()
        row = DataFrame({
            "time": [round(stop - start, 2)],
            "teams": [str(search_team).replace(', ', '-')],
            "fitness": [search_fit]
        })
        memetic = memetic.append(row, ignore_index=True)
save_data("genetico.csv", genetic)
save_data("local.csv", local)
save_data("memetico.csv", memetic)
print("FINISH!")
