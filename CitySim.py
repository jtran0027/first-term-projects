#Jason Tran

import time
import os
import random
import numpy as np

#Colors of use
#Green - 32
#Red - 31
#Yellow - 33
#Blue - 34
#White - 0 



#Creating the initial array
os.system("clear")
size = int(input("Enter a city size: "))
arr = np.full((size,size),'.')



#Creates a list of numbers used for random building generation
number_list1 = [] #House
for i in range(1,11):
	number_list1.append(i)

number_list2 = [] #Road
for k in range(11,21):
	number_list2.append(k)

number_list3 = [] #River
for j in range(21,31):
	number_list3.append(j)




#Starting Statistics
population = 0
revenue = 0



###########
#FUNCTIONS#
###########


#Function that will print the city
def print_array(mat):
	for x in range(0,len(mat)):
		for y in range(0,len(mat[0])):
			if arr[x][y] == '.':
				print('\033[32m.',end='')
			if arr[x][y] == '~':
				print('\033[34m~',end='')
			if arr[x][y] == '#':
				print('\033[0m#',end='')
			if arr[x][y] == '=':
				print('\033[33m=',end='')
			if arr[x][y] == 'X':
				print('\033[31mX',end='')
			if arr[x][y] == '-':
				print('\033[36m-',end='')
			if arr[x][y] == 'o':
				print('\033[31mo',end='')
		print('\033[0m')


#Function that builds a house
def house(mat,coord_y,coord_x,population,revenue):
	for x in range(coord_x,coord_x+2):
		for y in range(coord_y,coord_y+2):
			if (y >= 0) and (y < size):
				if (x >= 0) and (x < size):
					if mat[y][x] == '.':
						mat[y][x] = '#'
					elif mat[y][x] == '-':
						mat[y][x] = '#'
					elif mat[y][x] == 'o':
						mat[y][x] = '#'
					elif mat[y][x] != '.':
						mat[y][x] = 'X'
	population += 15
	revenue += 150		
	return population,revenue


#Function that builds a road
def road(mat, coord_y, coord_x,population,revenue):
	for x in range(coord_x, coord_x+3):
		if (coord_y >= 0) and (coord_y < size):
			if (x >= 0) and (x < size):
				if mat[coord_y][x] == '.':
					mat[coord_y][x] = '='
				elif mat[coord_y][x] == '-':
					mat[coord_y][x] = '='
				elif mat[coord_y][x] == 'o':
					mat[coord_y][x] = '='
				elif mat[coord_y][x] != '.':
					mat[coord_y][x] = 'X'
	population += 10
	revenue += 200
	return population,revenue


#Function that builds a river
def river(mat,coord_y, coord_x,population,revenue):
	for x in range(coord_x,coord_x+5):
		if (coord_y >= 0) and (coord_y < size):
			if (x >= 0) and (x < size):
				if mat[coord_y][x] == '.':
					mat[coord_y][x] = '~'
				elif mat[coord_y][x] == '-':
					mat[coord_y][x] = '~'
				elif mat[coord_y][x] == 'o':
					mat[coord_y][x] = '~'
				elif mat[coord_y][x] != '.':
					mat[coord_y][x] = 'X'
	population += 5
	revenue += 100
	return population,revenue


#Function that starts a flood
def flood(mat,population,revenue):
	for x in range(size):
		for y in range(size):
			mat[x][y] = '-'
		os.system("clear")
		print_array(mat)
		time.sleep(.25)
	print("You have been flooded!")
	time.sleep(1)
	for c in range(size):
		for d in range(size):
			mat[c][d] = '.'
		os.system("clear")
		print_array(mat)
		time.sleep(.25)
	
	population -= 50
	revenue -= 300
	return population, revenue


#Function that creates scattered meteor impacts
def meteor_shower(mat,population,revenue):
	for r in range(size):
		x_impacts = random.randint(0,size-1)
		y_impacts = random.randint(0,size-1)
		mat[x_impacts][y_impacts] = 'o'
		mat[x_impacts][y_impacts] = 'o'
		os.system("clear")
		print_array(mat)
		time.sleep(.25)

	population -= 30
	revenue -= 300
	return population, revenue


#Main bulk of the code, tells the player what they will build next or if an event is happening. Shows them their statistics as well.
def intro(population,revenue,randnum):
	print(f'Population : {population}')
	print(f'Revenue : ${revenue}')
	if randnum in number_list1:
		print("You are building a house next")
	if randnum in number_list2:
		print("You are building a road next")
	if randnum in number_list3:
		print("You are building a river next")
	if randnum == 31:
		print("It is starting to pour heavily...")
	if randnum == 32:
		print("The skies are filled with beautiful streaking stars....")
	while 1==1:
		try:
			coord_y,coord_x = [int(i) for i in input("Pick coordinates: ").split()]
			return coord_y, coord_x, population, revenue
		except:
			print("Not correct input.")
			continue


#Function to compile all buildings/events into one function for easy access. Also updates statistics
def building_selection(mat,population,revenue,randnum):
	if randnum in number_list1:
		population,revenue = house(mat,coord_y,coord_x,population,revenue)
	elif randnum in number_list2: 
		population,revenue = road(mat,coord_y,coord_x,population,revenue)
	elif randnum in number_list3: 
		population,revenue = river(mat,coord_y,coord_x,population,revenue)
	elif randnum == 31:
		population,revenue = flood(mat,population,revenue)
	elif randnum == 32:
		population,revenue = meteor_shower(mat,population,revenue)
		print("You have been hit by meteors!")
		time.sleep(1)
	return population,revenue


#Main body of the game, where everything loops
while 1==1:
	os.system("clear")
	print_array(arr)
	randnum = random.randint(1,32)
	coord_y, coord_x, population, revenue = intro(population,revenue,randnum)
	population, revenue = building_selection(arr,population,revenue,randnum)




