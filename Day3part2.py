file = open('Day3Input.txt', 'r')

possible = 0

a = []

for line in file:
    a.append(line.split())

i = 0

while i < len(a):
    for num in range(0,3):
        x = a[int(i)][int(num)]
        y = a[int(i)+1][int(num)]
        z = a[int(i)+2][int(num)]
        if int(x) + int(y) > int(z):
            if int(x) + int(z) > int(y):
                if int(y) + int(z) > int(x):
                    possible+= 1
    i += 3

print (possible)