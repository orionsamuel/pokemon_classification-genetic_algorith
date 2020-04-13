from pandas import read_csv


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PokemonsData(metaclass=Singleton):
    _df = read_csv("database/base-pokemon.csv")
    _range = _df.pokedex_number.size
    _team_target = []
    _team_size = 0

    def get_df(self):
        return self._df


    def get_range(self):
        return self._range


    def get_team_size(self):
        return self._team_size


    def get_team_target(self):
        return self._team_target


    def set_team_size(self, num):
        self._team_size = num


    def set_team_target(self, team):
        self._team_target = team
