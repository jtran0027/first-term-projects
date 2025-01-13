# Jason Tran

# Libraries
import random
import math
import time
import sys
import os
import numpy as np


# Creates the size of the array with command-line arguments
os.system("cls||clear")
n = 5 #(sys.argv[1])
SEED = int(sys.argv[1])
MAGNITUDE = int(sys.argv[2])

random.seed(SEED)


# Initializes the array using numpy
size = (2**int(n)) + 1
land = np.full((size,size),0)




# Function that prints the array neatly
def print_array(mat):
	for y in range(0,len(mat)):
		for x in range(0,len(mat[0])):
			#If statements here to check the value at a given coordinate and see if its higher or lower and set it to a certain color & symbol
			if int(mat[y][x]) <= 15:
				print("\033[34;7m~~",end='')
			if (int(mat[y][x]) > 15) and (int(mat[y][x]) <= 25):
				print("\033[33;7m.'",end='')
			if (int(mat[y][x]) > 25) and (int(mat[y][x]) <= 40):
				print("\033[32;7m;'",end='')
			if (int(mat[y][x]) > 40) and (int(mat[y][x]) <= 60):
				print("\033[37;7m^^",end='')
			if (int(mat[y][x]) > 60):
				print("\033[37;7m^^",end='')


		print('\033[0m')


# Creates random integers used for elevation in the corners of the array
A = random.randint(0,60)
B = random.randint(0,60)
C = random.randint(0,60)
D = random.randint(0,60) 

land[0][0] = A
land[0][size-1] = B 
land[size-1][0] = C
land[size-1][size-1] = D


# Main body of the recursion
def land_generation(map, topleft_x, topleft_y, topright_x, topright_y, bottomleft_x, bottomleft_y, bottomright_x, bottomright_y, depth, MAGNITUDE):
	#time.sleep(.1)
	print("\033[33A",end="\r")
	print_array(map)

	#	Base case
	# if statement for the depth
	if depth >= 5:
		return


	# Magnitude changes based on the depths
	if depth == 1:
		MAGNITUDE = int(MAGNITUDE - 2**-depth)
	
	if depth == 2:
		MAGNITUDE = int(MAGNITUDE - 2**-depth)

	if depth == 3:
		MAGNITUDE = int(MAGNITUDE - 2**-depth)

	if depth == 4:
		MAGNITUDE = int(MAGNITUDE - 2**-depth)
	
	if depth == 5:
		MAGNITUDE = int(MAGNITUDE - 2**-depth)


	# The x-step
	middle_x = (topleft_x + bottomright_x)//2
	middle_y = (topleft_y + bottomright_y)//2
	middle_value = (int(map[topleft_y][topleft_x]) + int(map[topright_y][topright_x]) + int(map[bottomleft_y][bottomleft_x]) + int(map[bottomright_y][bottomright_x]))//4
	map[middle_y][middle_x] = middle_value + random.randint(-MAGNITUDE, MAGNITUDE)


	# The plus-step
	#Left-middle side
	middleleft_x = (topleft_x + bottomleft_x)//2
	middleleft_y = (topleft_y + bottomleft_y)//2
	middleleft_value = (int(map[topleft_y][topleft_x]) + int(map[bottomleft_y][bottomleft_x]) + middle_value)//3
	map[middleleft_y][middleleft_x] = middleleft_value + random.randint(-MAGNITUDE, MAGNITUDE)

	#Right-middle side
	middleright_x = (topright_x + bottomright_x)//2
	middleright_y = (topright_y + bottomright_y)//2
	middleright_value = (int(map[topright_y][topright_x]) + int(map[bottomright_y][bottomright_x]) + middle_value)//3
	map[middleright_y][middleright_x] = middleright_value + random.randint(-MAGNITUDE, MAGNITUDE)
	
	#Top-middle side
	middletop_x = (topleft_x + topright_x)//2
	middletop_y = (topleft_y + topright_y)//2
	middletop_value = (int(map[topleft_y][topleft_x]) + int(map[topright_y][topright_x]) + middle_value)//3
	map[middletop_y][middletop_x] = middletop_value + random.randint(-MAGNITUDE, MAGNITUDE)

	#Bottom-middle side
	middlebottom_x = (bottomleft_x + bottomright_x)//2
	middlebottom_y = (bottomleft_y + bottomright_y)//2
	middlebottom_value = (int(map[bottomleft_y][bottomleft_x]) + int(map[bottomright_y][bottomright_x]) + middle_value)//3
	map[middlebottom_y][middlebottom_x] = middlebottom_value + random.randint(-MAGNITUDE, MAGNITUDE)


	# Apply 4 recursions to each respective subsquare
	#Top left subsquare
	land_generation(map, topleft_x, topleft_y, middletop_x, middletop_y, middleleft_x, middleleft_y, middle_x, middle_y, depth+1, MAGNITUDE)

	#Top right subsquare
	land_generation(map, middletop_x, middletop_y, topright_x, topright_y, middle_x, middle_y, middleright_x, middleright_y, depth+1, MAGNITUDE)

	#Bottom left subsquare
	land_generation(map, middleleft_x, middleleft_y, middle_x, middle_y, bottomleft_x, bottomleft_y, middlebottom_x, middlebottom_y, depth+1, MAGNITUDE)

	#Bottom right subsquare
	land_generation(map, middle_x, middle_y, middleright_x, middleright_y, middlebottom_x, middlebottom_y, bottomright_x, bottomright_y, depth+1, MAGNITUDE)


# Gives the recursion function the needed starting statistics
land_generation(land, 0, 0, 0, size-1, size-1, 0, size-1, size-1, 0, MAGNITUDE)
