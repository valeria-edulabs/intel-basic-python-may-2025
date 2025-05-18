# file_handler = open("data/alice_in_wonderland.txt", "r", encoding="utf-8")
# print(file_handler)
# content = file_handler.read()
# print(len(content), content[:100])
# file_handler.close()

with open("../data/alice_in_wonderland.txt", "r", encoding="utf-8") as f:
    # f.read().split("\n")
    counter = 0
    total_chars = 0
    alice = 0
    for line in f:
        print(line)
        print("---------")
        total_chars += len(line)
        counter += 1
        alice += line.lower().count("alice")

print("li.nes:", counter)
print("total chars", total_chars)
print("alice", alice)