from dataset import PokemonsData
from utils import get_db, lstr_to_lint

pokemons = PokemonsData()
counters = get_db("teams2", header=None, sep=" ")

team_target = []

for index, steam in counters.iterrows():
    if(index == 0):
        my_team = []
        team_target = lstr_to_lint(steam, pokemons.get_df())
        for enemy in team_target:
            against = pokemons.get_df().loc[enemy][9:]
            pkm_type = against.astype("float").idxmax().split("_")[1]
            my_team.append(pokemons.get_df().loc[
        
