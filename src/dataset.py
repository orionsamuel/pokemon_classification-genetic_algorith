from utils import get_db


class PokemonsData(object):
    __instance = None
    def __new__(cls, val):
        if PokemonsData.__instance is None:
            PokemonsData.__instance = object.__new__(cls)
            PokemonsData.__instance.df = get_db(val)
            PokemonsData.__instance.range = PokemonsData.__instance.df.\
                pokedex_number.size
        return PokemonsData.__instance
