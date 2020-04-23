from dataset import PokemonsData
from utils import get_db, lstr_to_lint

pokemons = PokemonsData()
counters = get_db("teams", header=None, sep=" ")

team_target = []

for index, steam in counters.iterrows():
    if index == 0:
        my_team = []
        team_target = lstr_to_lint(steam, pokemons.get_df())

    for enemy in team_target:
        partial_id = []
        against = pokemons.get_df().loc[enemy][9:]
        pkm_types = against.where(
            against.astype('float').max() == against).dropna().keys()

        for pkm_type in pkm_types:
            pkm_type = pkm_type.replace("against_", "")
            partial_id.append(
                pokemons.get_df().loc[(pokemons.get_df()['type1'] == pkm_type)
                                      |
                                      (pokemons.get_df()['type2'] == pkm_type)]
                .combat_point.astype("int64").idxmax())
        my_team.append(pokemons.get_df().combat_point[partial_id].idxmax())
