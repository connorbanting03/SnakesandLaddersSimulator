import pygame
import random
#Connor Banting 101225905 Assignment 6 Comp1405

# Initial Window 
mainWindow = pygame.display.set_mode((720, 720))
mainWindow.fill((240, 240, 250))
pygame.init()
myFont = pygame.font.SysFont("monospace", 35)
diceRoll = pygame.font.SysFont("monospace", 50)
#This function draws red and green lines which are basically snakes and ladder concepts
def drawlines():
    pygame.draw.line(mainWindow, (240, 0, 0), (180, 324), (324, 612), 5)
    pygame.draw.line(mainWindow, (240, 0, 0), (180, 468), (36, 612), 5)
    pygame.draw.line(mainWindow, (240, 0, 0), (180, 36), (324, 324), 5)

    pygame.draw.line(mainWindow, (0, 240, 0), (324, 468), (36, 324), 5)
    pygame.draw.line(mainWindow, (0, 240, 0), (468, 324), (36, 36), 5)
    pygame.draw.line(mainWindow, (0, 240, 0), (180, 612), (468, 468), 5)
    pygame.draw.line(mainWindow, (0, 240, 0), (36, 180), (324, 36), 5)
    pygame.draw.line(mainWindow, (0, 0, 0), (560, 0), (560, 720), 5)
#this function draws the spots where the game piecing will move
def drawsquares():
    for x in range(0, 4):
        for y in range(0, 5):
            pygame.draw.rect(mainWindow, (0, 0, 240), ((x * 144) + 36, (y * 144) + 36, 30, 30))

#This pulls the cordinates off the squares
def getcords():
    xvalues = []
    yvalues = []
    isTrue = True
    y = 612
    for x in range(0, 5):

#So this is sortive complex because I needed the cordinates of the spaces to be read in from left right on the bottom row but then right left on the row above it and so on
#One for loop will read the cordinates of the row in right to left and the other will do it left to right
        if isTrue:

            x = 468
            for w in range(0, 4):
                xvalues.append(x)
                yvalues.append(y)
                x = x-144
            isTrue = False
        else:
            x=36
            for o in range(0, 4):
                xvalues.append(x)
                yvalues.append(y)
                x = x+144
            isTrue = True
        y = y-144
    return xvalues, yvalues


#Calling all functions to setup game
xcords, ycords = getcords()
drawlines()
drawsquares()
#Setting up side menu
p1 = myFont.render("Player1", True, (0, 0, 0))
p2 = myFont.render("Player2", True, (0, 0, 0))
rollSign = myFont.render("Roll:", True, (0, 0, 0))
mainWindow.blit(p1, (590, 100))
mainWindow.blit(p2, (590, 140))
mainWindow.blit(rollSign, (600, 470))
clock = pygame.time.Clock()



#Game roll function
def Roll():
    word = int((((random.random()*4)+1)//1))
    Roll = diceRoll.render(str(word), True, (0, 0, 0))
    mainWindow.blit(Roll, (620, 500))
    return word

#Removes Previous Roll
def removeRoll():
    pygame.draw.rect(mainWindow, (240, 240, 250), (620, 500, 35, 35))


def changePostion(isTurn, Roll, Positon):
    #Orange Turn player 1
    #This determines which player's turn it is to move
    if isTurn:
        Color = (255, 69, 0)
        pygame.draw.rect(mainWindow, (240, 240, 250), ((xcords[Positon - 1] - 30, ycords[Positon - 1] + 3, 10, 10)))

    #These two statments above and below also delete the current spot the user is
    else:
        Color = (255, 105, 193)
        pygame.draw.rect(mainWindow, (240, 240, 250), (xcords[Positon - 1] + 30, ycords[Positon - 1] + 3, 10, 10))

    nP = Roll+Positon
    #This determines if the users new position is on a square with a snake or ladder
    gameWon = False
    if(nP>=20):
        gameWon=True
    elif(nP==6):
        nP=4
    elif(nP==7):
        nP=12
    elif(nP==13):
        nP=18
    elif(nP==3):
        nP=8
    elif(nP==9):
        nP=20
        gameWon=True
    elif(nP==19):
        nP=10
    elif(nP==11):
        nP=2
#then if nobody wins the users next cordinates for the spot the landed are loaded up and placed
    if(not gameWon):
        nextX = xcords[nP-1]
        nextY = ycords[nP-1]
    else:
        nextX = xcords[19]
        nextY = ycords[19]
    if(isTurn):
        pygame.draw.rect(mainWindow, Color, (nextX-30, nextY+3, 10, 10))

    else:
        pygame.draw.rect(mainWindow, Color, (nextX+30, nextY+3, 10, 10))

    return nP, not(gameWon)
#Basic startup settings
word = True
pygame.draw.rect(mainWindow, (255, 69, 0), (438, 615, 10, 10))
pygame.draw.rect(mainWindow, (255, 105, 193), (498, 615, 10, 10))

P1p = 1
P2p = 1
turnTracker = True
pygame.draw.rect(mainWindow, (255, 69, 0), (570, 105, 10, 10))
#Game loop
while word:
    #Calling off roll function, this will pick a random number between 1-4
    roll1 = Roll()
    word = False
    pygame.display.update()
    #This will check who's turn it is apply to roll to there turn and flip the turn shower that appears in the top right
    if(turnTracker):
        P1p, word = changePostion(turnTracker, roll1, P1p)
        turnTracker = False
        pygame.draw.rect(mainWindow, (240, 240, 250), (570, 105, 10, 10))
        pygame.draw.rect(mainWindow, (255, 105, 193), (570, 145, 10, 10))
    else:
        P2p, word = changePostion(turnTracker, roll1, P2p)
        turnTracker = True
        pygame.draw.rect(mainWindow, (240, 240, 250), (570, 145, 10, 10))
        pygame.draw.rect(mainWindow, (240, 69, 0), (570, 105, 10, 10))
    #This line sets the pace of the game
    clock.tick((1/5))
    #This just removes the previous roll to prepare for next turn
    removeRoll()
    pygame.display.update()
#This is staying so the program wont instantly terminate when the game is won
pygame.time.delay(5000)




