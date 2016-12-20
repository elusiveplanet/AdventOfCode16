with open('Day6Input.txt', 'r') as f:
    rows = f.read().strip().split("\n")
    
    f.close()

rows = list(map(list, zip(*rows)))

for i in rows:
    mostCommon = min(set(i), key=i.count)
    print(mostCommon, end="")