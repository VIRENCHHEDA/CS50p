import sys
import csv

if  len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
else:
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first","last","house"])
        writer.writerow({"first":"first", "last":"last", "house":"house"})
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    c1,c2=row["name"].split(",")
                    house=row["house"]
                    writer.writerow({"first":c2.lstrip(), "last":c1, "house":house})
        except FileNotFoundError:
            sys.exit(f"Could not read{sys.argv[1]}")