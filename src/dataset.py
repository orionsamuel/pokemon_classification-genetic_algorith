from utils import get_db


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class PokemonsData(metaclass=Singleton):
    df = get_db()
    range = df.pokedex_number.size

    def get_df(self):
        return self.df

    def get_range(self):
        return self.range
