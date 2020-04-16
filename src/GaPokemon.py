from pyeasyga.pyeasyga import GeneticAlgorithm


class GaPokemon(GeneticAlgorithm):
    def run(self):
        self.create_first_generation()

        for _ in range(1, self.generations):
            actual_generation = list(self.last_generation())

            if actual_generation[0][0] == actual_generation[-1][0]:
                break
            self.create_next_generation()
