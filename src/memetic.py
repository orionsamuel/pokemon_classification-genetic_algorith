from pyeasyga.pyeasyga import GeneticAlgorithm

from utils import create_team, fitness, get_relative_pokename
from dataset import PokemonsData

from MyGenetic import team_mutation, team_cossover, team_selection
from ils import local_search

class Memetic(GeneticAlgorithm):
    def run(self):
        """Run (solve) the Genetic Algorithm."""
        self.create_first_generation()
        # Do a local search and rerank this generation!!
        for _ in range(1, self.generations):
            self.create_next_generation()

def memetic_search(team_target, pokemons):
    me = Memetic(list(range(pokemons.get_range())), 50, 15, .8, 0.2, True, True)
    me.create_individual = create_team
    me.mutate_function = team_mutation
    me.crossover_function = team_crossover
    me.selection = team_selection
    me.fitness_function = fitness

    me.run()

    for pokemon in me.best_individual()[1]:
        print(get_relative_pokename(pokemon, pokemons.get_df()))
    print(ga.best_individual()[0])