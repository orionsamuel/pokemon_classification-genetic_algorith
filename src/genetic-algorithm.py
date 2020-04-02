import ga
import pandas
import sys

db = pandas.read_csv('database/base-pokemon.csv')

def execInput():
#read the executation input if it exists (aux)
    print("Let's input  Pokomeon GO team or a boss raid to counter!")
    team = input("Input your team by pokedexID spliting by " "(space): ")
    return team.split(" ")

def lstr_to_lint(slist): 
#cast list of strings to a list of integers (aux)
    ilist = []
    for element in slist:
        ilist.append(int(element))
    return ilist

def search_counters(team):
    print(db.head())
    

if __name__ == '__main__':
#main
    team_target = []
    if len(sys.argv)<4:
        team_target = lstr_to_lint(execInput())
        
    elif len(sys.argv)==4:
        del sys.argv[0]
        team_target = lstr_to_lint(sys.argv)
        
    else:
        print("Bad input!")
        exit()
    search_counters(team_target)
