from pandas import read_csv

db = read_csv("../database/base-pokemon.csv")


# Realiza a batalha entre dois pokemon para saber quem é o mais forte
def pokemon_battle(pokemon1, pokemon2):
    pokemon1_types = [
        db.loc[pokemon1 - 1, "type1"],
        str(db.loc[pokemon1 - 1, "type2"])
    ]

    if 'nan' in pokemon1_types:
        pokemon1_types.remove('nan')
    pokemon2_types = [
        db.loc[pokemon2 - 1, "type1"],
        str(db.loc[pokemon2 - 1, "type2"])
    ]

    if 'nan' in pokemon2_types:
        pokemon2_types.remove('nan')
    pokemon1_cp = db.loc[pokemon1 - 1, "combat_point"]
    pokemon2_cp = db.loc[pokemon2 - 1, "combat_point"]
    pokemon1_against = []
    pokemon2_against = []

    for tp in pokemon1_types:
        pokemon1_against.append(db.loc[pokemon2 - 1, "against_" + tp])

    for tp in pokemon2_types:
        pokemon2_against.append(db.loc[pokemon1 - 1, "against_" + tp])

    against1 = pokemon1_against.sort(reverse=True)[0]
    against2 = pokemon2_against.sort(reverse=True)[0]

    return pokemon1_cp * against1 - pokemon2_cp * against2


# Calcula qual é o melhor time
def fitness(team_selection, team_target):
    fitness = 0

    for pokemon_counter in team_selection:
        for pokemon_target in team_target:
            fitness += pokemon_battle(pokemon_counter, pokemon_target)

    return fitness


team_target = [474, 567, 639]
team_selection = [445, 481, 454]

avaliacao = fitness(team_selection, team_target)
print(avaliacao)
