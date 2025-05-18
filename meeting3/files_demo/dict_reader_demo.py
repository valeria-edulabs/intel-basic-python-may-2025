# open("/Users/valeria/Downloads/API - functions - Callable from UI.csv")
# path = "C:\\sdf\\sdf\\f"
import csv
import pprint

with open("../data/AAPL.csv", "r") as f:
    reader = csv.DictReader(f)
    for line in reader:
        pprint.pprint(line)
        # Date: .. Highest price: ...
        print(f"Date: {line['Date']}, Highest price: {line['High']}")