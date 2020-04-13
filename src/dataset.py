from pandas import read_csv


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PokemonsData(metaclass=Singleton):

    def __init__(self):
        self._df = read_csv("../database/base-pokemon.csv")
        self._list = self._df["pokedex_number"]
        self._team_target = []
        self._team_size = 3

    def get_df(self):
        return self._df

    def get_list(self):
        return self._list

    def get_team_size(self):
        return self._team_size

    def set_team_size(self, num):
        self._team_size = num

    def get_team_target(self):
        return self._team_target

    def set_team_target(self, team):
        self._team_target = team
