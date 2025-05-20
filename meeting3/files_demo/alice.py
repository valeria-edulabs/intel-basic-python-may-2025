# f = open("../data/alice_in_wonderland.txt", "r", encoding="utf-8")
# print(f)
# content = f.read()
# print(content)
# f.close()
from pprint import pprint

# with open("../data/alice_in_wonderland.txt", "r", encoding="utf-8") as f:
#     content = f.read()
#     print(content)


# with open("../data/alice_in_wonderland.txt", "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)
#         break
#     # f.seek(0)
#     print(f.readline())

with open("../data/AAPL.csv", "r", encoding="utf-8") as f:
    header = f.readline().strip().split(",")
    rows = []
    for line in f:
        data = line.strip().split(",")
        row = {}
        for key, value in zip(header, data):
            row[key] = value
        rows.append(row)
    pprint(rows)



# l = [
#     {
#        'Date': '2025-02-03',
#         'Open': 234.4
#     }
# ]