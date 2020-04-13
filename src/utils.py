import sys
from random import choice

from pandas import Index, read_csv
from dataset import PokemonsData


def battle(pokemon1, pokemon2, df):
    """
    This function perform a battle with two pokemons to decide the strongest.
    :param pokemon1: Your pokemon
    :param pokemon2: Enemy pokemon
    :param df: The dataset witch will be used to search for types, againsts
        and combat points.
    :return: The result number suggests the possibly win when higher than 0,
        the possibly loose when lower than 0 and a possible draw when it is 0
        This result is not a deterministic, but we suppose when pokemon2 has a
        better cp and the types of pokemon1 does not affect it, this expression
        try to represent this knowledge.
    """
    pokemon1 = get_relative_pokenumber(pokemon1, df)
    pokemon2 = get_relative_pokenumber(pokemon2, df)
    pokemon1_types = get_types(pokemon1, df)
    pokemon1_cp = get_cp(pokemon1, df)
    pokemon2_types = get_types(pokemon2, df)
    pokemon2_cp = get_cp(pokemon2, df)
    against1 = get_best_against(pokemon2, pokemon1_types, df)
    against2 = get_best_against(pokemon1, pokemon2_types, df)

    return pokemon1_cp * against1 - pokemon2_cp * against2


def create_team(pokemons):
    """
    Generate a random team using the input vector
    :param pokemons: a list with the items that will be selected
    :return: A team with three pokemon's in a list
    """
    new_team = []
    df = PokemonsData()
    for i in range(df.get_team_size()):
        new_team.append(choice(pokemons))
    return new_team



def exec_input():
    """
    Wait an input with pokemon index or pokemon name from terminal
    :return: A list with three pokemon's
    """
    print("Let's input Pokemon GO team or a boss raid to counter!")
    team = input(
        "Input your team by pokedex ID or Pokemon name splitting by ' '"
        "(space): ")

    return team.split(" ")[0:3]


def get_best_against(pokemon, types, df, prefix="against_"):
    """
    Get the against of a specific pokemon compared with types of another
        pokemon
    :param pokemon: A pokemon that will have your against compared with types
        of another pokemon
    :param types: A list with types of a pokemon
    :param df: The dataset with against
    :param prefix: against prefix, if have one (by default the prefix is:
        against_)
    :return: The higher against of a pokemon using the types list
    """
    against = []

    for tp in types:
        against.append(df.loc[pokemon, prefix + tp])

    against.sort(reverse=True)

    return against[0]


def get_cp(pokemon, df):
    """
    Get the combat points of a specific pokemon
    :param pokemon: A pokemon that you want to know the combat points
    :param df: the data base with pokemon's and combat points
    :return: The combat point of the correspondent pokemon
    """

    return df.combat_point[pokemon]


def get_db(file="base-pokemon",########################################
           path="database/",
           extension=".csv",
           header=0,
           sep=","):
    """
    :param file: Name of the dataset
    :param path: Path to the dataset
    :param extension: By default it is .csv, but it can be changed when this
        file support more extensions
    :param header: Use None when the dataset does not have a header or
        identify using a index, by default the first row is the header
    :param sep: The separator of this file, by default is comma
    :return: If success it return a Pandas Data Frame with the data
    """
    file_name = path + file + extension
    try:
        return read_csv(file_name, header=header, sep=sep)
    except IOError:
        print("Cannot open this file: ", file_name)
        sys.exit(1)


def get_types(pokemon, df):
    """
    Get the type of the pokemon and remove the type 2 if not exists
    :param pokemon: The pokemon that you want to know the types
    :param df: A dataset with pokemons and types
    :return: A list with the pokemon type(s)
    """
    pokemon_types = [df.type1[pokemon], str(df.type2[pokemon])]

    if 'nan' in pokemon_types:
        pokemon_types.remove('nan')

    return pokemon_types


def get_relative_pokenumber(pokenumber, df):
    """
    receive a pokemon name, returns his pokedex number
    :param pokenumber: the pokedex number of the pokemon
    :param df: the dataset that will be user to search the pokemon
    :return: the position of this pokemon in the dataset
    """

    return Index(df.pokedex_number).get_loc(pokenumber)


def get_relative_pokename(pokenumber, df):####################################
    """
    receive a pokedex_number, and returns the pokemon name
    :param pokenumber: The number of the pokemon
    :param df: The dataset that will be user to search the pokemon
    :return: The name of this pokemon in the dataset
    """

    return df.name[range(len(df.pokedex_number))[pokenumber]]


def get_true_pokenumber(pokename, df):
    """
    receive a pokemon name, returns his pokedex number
    :param pokename: the name of the pokemon
    :param df: the dataset that will be user to search the pokemon
    :return: the pokedex ID of this pokemon
    """

    return df.pokedex_number[Index(df.name).get_loc(pokename)]


def get_true_pokename(pokenumber, df):
    """
    receive a pokedex_number, and returns the pokemon name
    :param pokenumber: The number of the pokemon
    :param df: The dataset that will be user to search the pokemon
    :return: The name of this pokemon in the dataset
    """

    return df.name[Index(df.pokedex_number).get_loc(pokenumber)]


def lstr_to_lint(slist, df):
    """
    Cast list of strings to a list of integers (aux)
    :param slist: A string list read from terminal or other way
    :param df: The dataset to index this list
    :return: A integer list that contains the ids of the correspondents pokemons
    """
    ilist = []

    for element in slist:
        if element.isnumeric():
            ilist.append(int(element))
        else:
            ilist.append(get_true_pokenumber(element, df))
    return ilist


def fitness(my_team, df):
    """
    This function evaluate the population
    :param my_team: A possible team
    :param df: The database the library requisite this param
    :return: the sum of differences of multiplications the combat points with
        the best against of a type that a pokemon has
     """
    fit = 0
    pokemons = PokemonsData()
    for possible_counter in my_team:
        for countered in pokemons.get_team_target():
            fit += battle(possible_counter, countered, pokemons.get_df())

    return fit

def is_sorted_by_CP_reverse(team):#####################################
#verify if a team is sorted by CP in a reverse way (higher to lower)
    for index in range(len(team)-1):
        if(db.loc[team[index], "combat_point"] < db.loc[team[index+1], "combat_point"]):
            return False
    return True

def sort_by_cp_reverse(team): ####################################
#sort a team by the CP, higher to lower (reverse)
    for x in range(len(team)):
        team[x] = pokemon_validation(team[x])
    tmp = None
    while not is_sorted_by_CP_reverse(team):
        for index in range(len(team)-1):
            if db.loc[team[index], "combat_point"] < db.loc[team[index+1], "combat_point"]:
                tmp = team[index]
                team[index] = team[index+1]
                team[index+1] = tmp
    for x in range(len(team)):
        team[x] = pokemon_validation_reverse(team[x])
    return team

def best_against(team, target, df):
#select the best pokemon of a team against one pokemon target
    result = []
    if len(team)>1:
        for pokemon in team:
            result.append(battle(pokemon, target, df))
        return team[result.index(max(result))]
    else:
        return team[0]

def sort_best_team(counter, df):
#sort the counter team to the best way against team target
    pokemons = PokemonsData()
    target = pokemons.get_team_target()
    team_target = target = pokemons.get_team_target()
    counter_copy = counter.copy()
    for index in range(len(target)):
        counter[index] = best_against(counter_copy, target[index], df)
        counter_copy.remove(counter[index])
    tmp = None
    for k in team_target:
        tmp = counter[team_target.index(k)]
        counter[team_target.index(k)] = counter[target.index(k)]
        counter[target.index(k)] = tmp
    return counter

def best_typeset_against(pokemon1, pokemon2, df):
#return the best type for moves set of pokemon1 against pokemon2
    pokemon1 = get_relative_pokenumber(pokemon1, df)
    pokemon2 = get_relative_pokenumber(pokemon2, df)
    pokemon1_types = get_types(pokemon1, df)
    pokemon1_against = []
    for tp in pokemon1_types:
        pokemon1_against.append(df.loc[pokemon2, "against_"+tp])

    return pokemon1_types[pokemon1_against.index(max(pokemon1_against))]
