#---------------------------------------------------#
#                   Antonio Pelusi                  #
#---------------------------------------------------#


#-------------------- LIBRARIES --------------------#

import os
import time as t
import random as r


#---------------------- SETUP ----------------------#

#characters used in print
empty_char = "  "
half_char = "▓▓"
full_char = "██"

#screen size
gridwidth = 35
gridheight = 19

#variables initialization
counter = 0
index = 1
recursion = False
first = second = third = fourth = None


#-------------------- FUNCTIONS --------------------#

#print the grid once
def printgrid(grid):
    outstring = ""
    outstring += (full_char*(gridwidth + 2))
    outstring += ("\n")
    for i in range(gridheight):
        outstring += full_char
        for j in range(gridwidth):
            outstring += grid[j][i]
        outstring += full_char
        outstring += "\n"
    outstring += (full_char*(gridwidth + 2))
    outstring += "\n"
    return outstring

#count neighbors
def numneighbors(grid, row, col):

    #neighbors counter
    num = 0

    try:
        #right neighbor
        if grid[row + 1][col] == half_char:
            num += 1

        #left neighbor
        if grid[row - 1][col] == half_char:
            num += 1
    
        #down neighbor
        if grid[row][col + 1] == half_char:
            num += 1
    
        #up neighbor
        if grid[row][col - 1] == half_char:
            num += 1
    
        #right-down neighbor
        if grid[row + 1][col + 1] == half_char:
            num += 1
    
        #right-up neighbor
        if grid[row + 1][col - 1] == half_char:
            num += 1
    
        #left-down neighbor
        if grid[row - 1][col + 1] == half_char:
            num += 1
    
        #left-up neighbor
        if grid[row - 1][col - 1] == half_char:
            num += 1

    #no neighbors
    except:
        pass
    
    return num

#check for end of motion
def check_end():

    #check for collision between two consecutive grid
    if pixelgrid == newiteration:

        #flush terminal
        os.system('clear')

        #print the final grid
        print(printgrid(pixelgrid))
        print("Stopped at iteration ", counter)

        #wait any command to end
        input()

        #quit the app
        quit()
    
#check for recursion
def check_recursion():

    #get global variables
    global recursion, index, first, second, third, fourth

    #save every grid
    if recursion == False:
        if index == 1:
            first = newiteration
            index = 2
        elif index == 2:
            second = newiteration
            index = 3
        elif index == 3:
            third = newiteration
            index = 4
        elif index == 4:
            fourth = newiteration
            index = 1

        #check if there is any 2-state or 3-state recursion
        if first == third or first == fourth:
            recursion = True


#-------------- START GRID GENERATION --------------#

#flush terminal
os.system('clear')

#generate empty grid
pixelgrid = [[empty_char for y in range (gridheight)] for x in range(gridwidth)]

#insert random object
for i in range(gridheight):
    for j in range(gridwidth):
        if r.randint(0,1) == 1: 
            pixelgrid[j][i] = half_char
        else:
            pixelgrid[j][i] = empty_char

#print initial grid
print(printgrid(pixelgrid))

#ask for tick time
try:
    tick_time = float(input("Insert tick speed to start (default: 0.1): "))
except ValueError:
    tick_time = 0.1


#-------------------- MAIN LOOP --------------------#

while True:

    #flush terminal
    os.system('clear')

    #generate empty grid
    newiteration = [[empty_char for y in range (gridheight)] for x in range(gridwidth)] #create a new grid to iterate onto

    for j in range(gridheight):
        for i in range(gridwidth):

            #count neighbors
            livingneighbors = numneighbors(pixelgrid, i, j)
            
            #case >3: reproduction
            if pixelgrid[i][j] == empty_char:
                if livingneighbors == 3:
                    newiteration[i][j] = half_char
            
            elif pixelgrid[i][j] == half_char:
                #case ==2 or ==3: continue to live
                if (livingneighbors == 2) or (livingneighbors == 3):
                    newiteration[i][j] = half_char
                #case <2 or >3: death
                elif (livingneighbors < 2) or (livingneighbors > 3):
                    newiteration[i][j] = empty_char #If a living cell has one or less than two or more than three neighbors, it dies
    
    #check for end of motion
    check_end()

    #check for recursion
    check_recursion()

    #save current state
    pixelgrid = newiteration

    #print current state
    print(printgrid(pixelgrid))

    #check if a recursion has occurred
    if recursion == False:
        counter += 1
        print("Iteration count:", counter)
    else:
        print("Recursion found at iteration", counter)

    #wait the tick time
    t.sleep(tick_time)
