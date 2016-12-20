file = open('Day3Input.txt', 'r')

possible = 0

for line in file:
    split = line.split()
    x = split[0]
    y = split[1]
    z = split[2]

    if int(x) + int(y) > int(z):
        if int(x) + int(z) > int(y):
            if int(y) + int(z) > int(x):
                possible += 1

print (possible)