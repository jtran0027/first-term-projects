#Jason Tran

import tkinter as tk
import time
import random
import math

# Creates the grid that the marbles bounce around
root = tk.Tk()
Frame_Width = 800
Frame_Height = 600
g = print("%dx%d",(Frame_Width,Frame_Height))
root.geometry(g)
root["bg"] = "blue"


# Creates the popout window
canvas = tk.Canvas(root)
canvas.pack()
canvas.config(width=Frame_Width,height=Frame_Height)
root.title("Marbles")


# Function that creates color
def dec2hex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'



class Marble:
    def __init__(self,x1,y1,r,g,b):
        self.velx = random.randint(20,25)
        self.vely = random.randint(2,3)

        self.size = 15

        self.position_x1 = x1
        self.position_y1 = y1
        self.position_x2 = x1 + self.size
        self.position_y2 = y1 + self.size

        self.stuck = False

        self.r = r
        self.g = g
        self.b = b
    

    #Allows for the movement of the circles
    def move(self):
        #Checks for the borders to keep the ball within the screen
        if (self.position_x1 < 0):
            self.velx = -self.velx
        if (self.position_y1 < 0):
            self.vely = -self.vely
        if (self.position_x1 + self.size > 800):
            self.velx = -self.velx
        if (self.position_y1 + self.size > 600):
            self.vely = -self.vely

        #If it is stuck, it will set the velocity to 0, otherwise it moves the circles around
        if self.stuck == False:
            self.position_x1 += self.velx
            self.position_y1 += self.vely
        elif self.stuck == True:
            self.velx = 0
            self.vely = 0


    #Collision calculations with Pythagoreans Theorm
    def collision(self,other_cir):
        if other_cir.stuck == True:
            if math.sqrt((self.position_x1 - other_cir.position_x1)**2 + (self.position_y1 - other_cir.position_y1)**2) <= 16:
                self.stuck = True
                self.r = 173
                self.g = 216
                self.b = 230



    #Making the stuck marbles change color to be more intense by using the distance formula for the center dot
    def treecolor(self,center_marble):
        if self.stuck == True:
            if math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 50 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 20:
                self.r = 160
                self.g = 200
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 100 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 50:
                self.r = 150
                self.g = 190
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 150 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 100:
                self.r = 140
                self.g = 180
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 200 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 150:
                self.r = 130
                self.g = 170
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 250 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 200:
                self.r = 120
                self.g = 160
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 300 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 250:
                self.r = 110
                self.g = 150
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 350 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 300:
                self.r = 100
                self.g = 140
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 400 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 350:
                self.r = 90
                self.g = 130
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 450 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 400:
                self.r = 80
                self.g = 120
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 500 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 450:
                self.r = 70
                self.g = 110
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 550 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 500:
                self.r = 60
                self.g = 100
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 600 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 550:
                self.r = 50
                self.g = 90
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 650 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 600:
                self.r = 40
                self.g = 80
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 700 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 650:
                self.r = 30
                self.g = 70
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 750 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 700:
                self.r = 20
                self.g = 60
                self.b = 230
            elif math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) <= 800 and math.sqrt((self.position_x1 - center_marble.position_x1)**2 + (self.position_y1 - center_marble.position_y1)**2) > 750:
                self.r = 10
                self.g = 50
                self.b = 230


    #Creates the circle on the window and gives it color
    def draw(self):
        x1 = self.position_x1
        y1 = self.position_y1
        x2 = self.position_x1 + self.size
        y2 = self.position_y1 + self.size

        r = self.r
        g = self.g
        b = self.b

        canvas.create_oval([x1,y1,x2,y2],fill=dec2hex(r,g,b), width=0)
    

    #Returns the stuck variable for use in the main loop
    def get_status(self):
        return self.stuck



# Initializes the very first marble for the tree
First = Marble((Frame_Width/2)-10,(Frame_Height/2)-10,173,216,230)
First.stuck = True
list_of_marbles = [First]



# Creates the 10 randomly places marbles
for j in range(1,11):
    list_of_marbles.append(Marble(random.randint(0,Frame_Width-30),random.randint(0,Frame_Height-30),255,255,255))



# Main body of the code
while True:

    canvas.delete("all")
    canvas['bg'] = "black"

    #Resets the value so that the stuck marble checker functions correctly
    stuck_marbles = 0
    
    #Main loop for class operations
    for i in range(0,len(list_of_marbles)):
        
        #Checks for stuck marbles and adds it to a variable
        if list_of_marbles[i].get_status() == True:
            stuck_marbles += 1

        #If all the marbles are stuck, creates a new batch of 10
        if stuck_marbles == len(list_of_marbles):
            for k in range(1,11):
                list_of_marbles.append(Marble(random.randint(0,Frame_Width-30),random.randint(0,Frame_Height-30),255,255,255))
        
        #Checks for collision
        for p in range(0,len(list_of_marbles)):
            if i != p:
                list_of_marbles[i].collision(list_of_marbles[p])

        #Movement and drawing of the objects
        list_of_marbles[i].move()
        list_of_marbles[i].treecolor(list_of_marbles[0])
        list_of_marbles[i].draw()



    canvas.update() 
    time.sleep(.01) #100 FPS

root.destroy()


