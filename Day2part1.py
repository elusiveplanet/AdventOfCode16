#Day2Part1AoC2016
#Written by: Alexis Renderos	
file = open('Day2Input.txt', 'r')

keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

global cX
global cY

cX = 1
cY = 1

a = []

def kUp():
	global cY
	if (cY == 0):
		cY = 0
	elif (cY > 0):
		cY -= 1

def kDown():
	global cY
	if (cY == 2):
		cY = 2
	elif (cY < 2):
		cY += 1

def kLeft():
	global cX
	if (cX == 0):
		cX = 0
	elif (cX > 0):
		cX -= 1

def kRight():
	global cX
	if (cX == 2):
		cX = 2
	elif (cX < 2):
		cX += 1

def kRat(rat):
	if (rat == "U"):
		kUp()
	elif (rat == "D"):
		kDown()
	elif (rat == "L"):
		kLeft()
	elif (rat == "R"):
		kRight()


#print (keypad[0,2])

for line in file:
	a.append(line.split())

i = 0
k = 0
#print(keypad[cX][cY])
while i < len(a): #This gets the individual key code sequences
	while k < len(a[i][0]): #Loops over the current sequence
		kRat(a[i][0][k:k - len(a[i][0]) + 1]) #This interprets the current sequence and logs it
		print(keypad[cX][cY])
		k += 1
	#print(keypad[cX][cY])
	cX = 1 #reset keypad to center
	cY = 1
	i += 1
	k = 0