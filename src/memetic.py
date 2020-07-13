from ils import local_search
from MyGenetic import team_crossover, team_mutation, team_selection
from pyeasyga.pyeasyga import GeneticAlgorithm
from utils import create_team, fitness


class Memetic(GeneticAlgorithm):
    _iterations = 100

    def set_iterations(self, num):
        self._iterations = num

    def run(self):
        """Run (solve) the Genetic Algorithm."""
        self.create_first_generation()
        # Do a local search and rerank this generation!!
        self.do_local_search()
        self.rank_population()

        for _ in range(1, self.generations):
            actual_generation = list(self.last_generation())

            if actual_generation[0][0] != actual_generation[-1][0]:
                self.create_next_generation()
                self.do_local_search()
                self.rank_population()
            else:
                break

    def do_local_search(self):
        for individual in self.current_generation:
            individual.genes, individual.fitness = local_search(
                self.seed_data, individual.genes, 10)


def memetic_search(pokemons, iterations):
    me = Memetic(list(range(pokemons.get_range())), 50, 15, .8, 0.2, True,
                 True)
    me.set_iterations(iterations)
    me.create_individual = create_team
    me.mutate_function = team_mutation
    me.crossover_function = team_crossover
    me.selection = team_selection
    me.fitness_function = fitness

    me.run()

    return me.best_individual()[1], me.best_individual()[0]
