import sys
from genetic_algorithm import search_counters

if __name__ == '__main__':
#main
    if len(sys.argv)<4:
        search_counters(execInput())

    elif len(sys.argv)==4:
        del sys.argv[0]
        search_counters(sys.argv)

    else:
        print("Bad input!")
        exit()
