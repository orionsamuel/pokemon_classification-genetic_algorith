from genetic_algorithm import search_counters
from pandas import write_csv

from ils import run
from utils import get_db, lstr_to_lint

counters = get_db("teams")

start = []
stop = []

genetic_results = []
search_results = []


# lista = []
def get_fitness(tuple):
    return tuple[2]


# lista.sort(key=get_fitness, reverse=True)

for index, steam in counters.iterrows():
    team_target = lstr_to_lint(steam)
    for i in range(5):
        start.append(time.time())
        genetic_results.append(search_counters(team_target))
        stop.append(time.time())
        ## Salvando em lista
        genetic_results.sort(key=get_fitness, reverse=True)
        write_csv("team_fit_genetic.csv", genetic_results)  ## Fazendo um append
        start.append(time.time())
        search_results.append(run(team_target))
        stop.append(time.time())
        ## Salvando em lista
        write_csv("team_fit_local_search.csv",
                  search_results)  ## Fazendo um append
