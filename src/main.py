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
        save_data("genetico.csv", row)
        start = time()
        search_team, search_fit = run(pokemons)
        stop = time()
        row = DataFrame({
            "time": [round(stop - start, 2)],
            "teams": [str(search_team).replace(', ', '-')],
            "fitness": [search_fit]
        })
        save_data("local.csv", row)
        start = time()
        search_team, search_fit = memetic_search(pokemons, 50)
        stop = time()
        row = DataFrame({
            "time": [round(stop - start, 2)],
            "teams": [str(search_team).replace(', ', '-')],
            "fitness": [search_fit]
        })
        save_data("memetico.csv", row)
print("FINISH!")
