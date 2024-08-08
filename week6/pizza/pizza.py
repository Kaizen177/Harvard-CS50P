
import csv
import sys
from tabulate import tabulate


def main():

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if not sys.argv[1].endswith(".csv") :
            sys.exit("Not a CSV file")
        else:
            print(menu(sys.argv[1]))




def menu(x):

    with open(x) as file:
        rows = csv.reader(file)
        return tabulate(rows,headers="firstrow",tablefmt='grid')

main()
