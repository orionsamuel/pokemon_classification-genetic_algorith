from MyGenetic import search_counters

from dataset import PokemonsData
from utils import get_db, lstr_to_lint

counters = get_db("teams", header=None, sep=" ")

team_target = []

for index, steam in counters.iterrows():
    team_target = lstr_to_lint(steam, pokemons.df)
    print(search_counters(team_target))
