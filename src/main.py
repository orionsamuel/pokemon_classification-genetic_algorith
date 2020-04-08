import sys
from genetic_algorithm import search_counters

def print_result(result):
    for i in range(len(result[0])):
        print(result[0][i]+" ("+result[1][i]+" move set)")
    print(result[2])

if __name__ == '__main__':
#main
    result = None
    if len(sys.argv)<4:
        result = search_counters(execInput())

    elif len(sys.argv)==4:
        del sys.argv[0]
        result = search_counters(sys.argv)

    else:
        print("Bad input!")
        exit()
    print_result(result)
