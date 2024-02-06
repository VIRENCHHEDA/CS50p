import sys
import csv
from tabulate import tabulate

list=[]

if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
else:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                list.append(row)   #you can use this instead of 'list.append([row[f"{header[0]}"], row[f"{header[1]}"], row[f"{header[2]}"]])'.
                                     #it is use to append(add or merge) the csv files into above list
    except FileNotFoundError:
        sys.exit("File does not exist")

    print(tabulate(list,headers="keys", tablefmt = "grid"))   #check tabulate function documentaion for this line
                                                               #printing the list and using tabulate functionalites for making a table

