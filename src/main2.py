import sys
from ga_pokemon import search_counters

def print_result(result):
    for i in range(len(result[0])):
        print(result[0][i]+" ("+result[1][i]+" move set)")
    print(result[2])

if __name__ == '__main__':
#main
    result = None
    del sys.argv[0]
    result = search_counters(sys.argv)
    print_result(result)
