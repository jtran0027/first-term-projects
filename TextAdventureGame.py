#Jason Tran

#Starting statistics of the player. Goal is to gather as much points as possible
score = 0
bag = []
LiquidCheck = False


import time
import os



#Checking statistics
def checkinfo():
        print(f'You have a score of: {score}')
        print('Items acquired:')
        print(bag)



#Rooms written in functions
def DeeperCavern(score, bag):
	print("The huge cavern glistens from an unknown blue light from the ceiling. You hear huge streams splashing as they hit the cave floor. Under you is a huge drop into a huge pool.")
	if score == 0:
		score +=1
	return score


def Outside(score, bag):
	print("The bright sun beams onto your face, as you observe your surroundings. Immediately, two structures stand out to you: The huge wooden mansion on the left path, and a couple of houses resembling a village.")
	score += 5
	return score


def mansion(score, bag):
	print("You head towards the mansion, noticing slight scratches all over you. Needing help, you hope that there is someone there who is amiable.")
	time.sleep(1)
	print("Arriving at the entrance, you notice a butler standing at the front. You decide to sprint toward him and ask him politely for help.")
	time.sleep(1)
	print("He decides to let you into the building and leads you to the doctor's office. You feel reassured that you will get the proper help.")
	time.sleep(1)
	print("As you are walking, you observe the inside of the building, noticing it's very unique, yet eerie, design.Oddly painted paintings are all around and the hallway is absurdly long.")
	time.sleep(1)
	print("The butler abruptly stops within the middle of the hallway...")
	time.sleep(1)
	print("You stop behind him as you notice his head slightly turning.")
	time.sleep(1)
	print("He just smiles at you silently. Breaking the silence he tells you to turn around.")
	time.sleep(3)
	print("Before you have even realized it, you have been shanked in the back to a man in a lab coat. You presume he is the 'doctor' as you fall to the floor in immmense agony.")
	time.sleep(1)
	print("Your vision fades, as your screams do as well. You hear distant laughing as the warm feeling of blood comes out of the wound.")
	time.sleep(2)
	print("You have died.")
	score = -1
	return score

def village(score, bag):
	print("You decide to stray away from the eerie mansion in the distance and head downwards to the village.")
	time.sleep(1)
	print("Rummaging through some shrubs, you find a path that looks like it leads towards the village.")
	time.sleep(1)
	print("You walk along the path, trying to remember what had happened to you before you somehow got into the cave. Maybe the villagers have some answers.")
	time.sleep(2)
	print("You arrive at the village and greet one of the guards. He looks at you and raises his weapon. You tell him to wait and explain your scenario.")
	time.sleep(2)
	print("He allows you to enter, but guides you toward the village head. As you walk towards your meeting, you notice the villagers giving you worrying looks. You wonder why, but realize you look beaten up from the incident.")
	time.sleep(2)
	print("You meet with the very nice Villager Head and explain your scenario. He is very supportive about your scenario and thinks you have been attacked by one of the 3 Great Villains.")
	time.sleep(2)
	print("Hearing this, you hope that your family is okay and is not also held captive by him. You beg the Village Head to assist you in taking revenge. He can only offer few supplies and says that you will have to train with the greatest to defeat him.")
	time.sleep(2)
	print("With new resolve, you set out on your journey of defeating one of the Great Three. Acquipped with just a starting 'Iron Sword' and 'Copper Shield' you set foot out for the next village he recommends.")
	score += 10
	return score

#Interacting with the backpack
def Add_Item(a):
	if (len(a) <= 10):
		a.append(item)
	else:
		print("You have too many items")
	return a
	
def Remove_Item(a):
	a.pop()
	return a



#Start of the game
os.system("clear")
print("You wake up to water splashing onto your forehead, accomidated with a headache. You look around, confused as to how you are here now.")
while 1 == 1:
	command = input("What would you like to do now?: Look, Delve, Exit. ")
	
#Look command
	if command == "Look": 
		print("You look around, holding your head as it throbs. With your blurred vision, you observe that your exit is blocked by a huge boulder. The outside leaks through the rough edges of the huge boulder. The light creates an outline of an object that catches your eye.")
		print("Type in 'Pick up' if you would like to obtain the object.")
		print('')
		continue

#Dive deeper into the cavern
	elif command == "Delve":
		print("You decide to wander deeper into the cave. Wondering if you are doing the right decision, the answer is shown clearly to you as you trip and fall over a small ledge. As you dust yourself off, you see an even bigger cave.")
		score = DeeperCavern(score, bag)
		print(f'You have a score of: {score}')
		command = input("What would you like to do?: Jump, Back. ")
#Loses the game
		if command == "Jump":
			print("As you take the leap, you pray that the water isn't too shallow. You second guessed your choice, as you could not see how shallow the pool was. You decided to take the risk and went for the leap.")
			time.sleep(1)
			print("SPLASH!!!!!!!!!")
			time.sleep(1)
			print("\033[0;31mYou have died.\033[0;0m")
			score = -1
			print(f'You ended up with the score: {score}')
#Go back to the start
		elif command == "Back":
			print('')
			continue

#The route that let's them explore the outside world. Continuation of the story
	elif command == "Exit":
		print("You attempt to move the boulder, but to no avail... Maybe there is something you can use to help you.")		
		for n in range(0,len(bag)): #Checks for item
			if bag[n] == "Strange Liquid":
				LiquidCheck = True
		if LiquidCheck == True: #If true, the story continues
			print("You consume the potion and feel a sudden surge of energy. Something is flowing through your veins.")
			bag = Remove_Item(bag)
			time.sleep(2)
			print("You shove the rock with all your might. To your surprise, the huge boulder glides across the floor as the cave rumbles. You manage to open to create an openning for you to escape. The stalactites begin to fall, making you rush outside before it is too late.")
#Visiting the outside world
			time.sleep(2)
			score = Outside(score,bag)
			command = input("What would you like to do?: Explore Mansion, Explore Village: ")

#Route that loses the game
			if command == 'Explore Mansion':
					score = mansion(score,bag)
					checkinfo()
					break

#Route that wins the game
			elif command == 'Explore Village':
				score = village(score,bag)
				time.sleep(1)
				item = 'Iron Sword'
				bag = Add_Item(bag)
				item = 'Copper Sword'
				bag = Add_Item(bag)
				print("You have finished the first edition of the game. It is to be continued in the sequel.")
				checkinfo()
				break

		else:
			print("It seems as you do not have anything... Maybe search the room again.")
			print('')
			continue

#Obtains the liquid needed to escape the cave
	elif command == "Pick up":
		if LiquidCheck == False:
			print("You obtain a strange liquid. It may come in handy later.")
			print('')
			item = "Strange Liquid"
			bag = Add_Item(bag)
			LiquidCheck = True
			continue
		elif LiquidCheck == True:
			print("You have already obtained this liquid.")
			continue
	else:
		print("Not a valid command, please put in a proper command.")
		print('')
		time.sleep(2)
		continue

	
	#Losing score is -1
	if score == -1:
		break
	
