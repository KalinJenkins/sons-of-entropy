#!/usr/bin/python

# kalin jenkins (kalin.jenkins@gmail.com)
# Intended to keep track of munchkin chracters and maintain game playstats
# munchkin_keeper - 11/09/2013 
mkVersion = "v.5"

import sys
import random
import re


#--------------------------------------------------------------------------------------------

def wiper():
    sys.stderr.write("\x1b[2J\x1b[H")	# clears the screen, only works on ANSI (*nix)
    
def drawLog():
    print playLog
    
def drawActions():
    print "\n          Level a player [u]p"
    print "          Level a player [d]own"
    print "          Roll to [e]scape"
    print "\n\n"
    actionInput = str(raw_input("Enter a command to continue:\n\n          "))
    if re.match("[ude]", actionInput):
        wiper()
        drawBoard()
        if re.match("[u]", actionInput):
            print "level up"
        if re.match("[d]", actionInput):
            print "level up"
        if re.match("[e]", actionInput):
            print "level up"
    
def drawBoard():
    playerBoard = '\n\n--------------------------------------------------------------------------------\n\n'
    #playerBoard += 'Round '   --------Not in use yet
    #playerBoard += str(gameRound)   --------Not in use yet
    #playerBoard += '\n\n'   --------Not in use yet
    
    # shows all the player data
    if (playerNum > 0):
        playerBoard += player1['Name']
        playerBoard += ' - Level '
        playerBoard += str(player1['Level'])
        playerBoard += "\n"
    if (playerNum > 1):
        playerBoard += player2['Name']
        playerBoard += ' - Level '
        playerBoard += str(player2['Level'])
        playerBoard += "\n"
    if (playerNum > 2):
        playerBoard += player3['Name']
        playerBoard += ' - Level '
        playerBoard += str(player3['Level'])
        playerBoard += "\n"
    if (playerNum > 3):
        playerBoard += player4['Name']
        playerBoard += ' - Level '
        playerBoard += str(player4['Level'])
        playerBoard += "\n"
    if (playerNum > 4):
        playerBoard += player5['Name']
        playerBoard += ' - Level '
        playerBoard += str(player5['Level'])
        playerBoard += "\n"
    if (playerNum > 5):
        playerBoard += player6['Name']
        playerBoard += ' - Level '
        playerBoard += str(player6['Level'])
        playerBoard += "\n"

    # Display the lowest level player(s) to recieve Charity
    playerBoard += '\n--------------------------------------------------------------------------------'
    print playerBoard

#--------------------------------------------------------------------------------------------

wiper()

print "\n\n\n                           Welcome to the Munchkin Dungeon Exploration Permit Office!"
	
	#Get number of players
playerNum = int(raw_input("\n\nHow many of you munchkins will be going down into the dungeons today? Groups have to have between three and six adventurers.\n\n"))
while (playerNum < 3 or playerNum > 6):
    playerNum = int(raw_input("\nDungeon permits really can only be issued for groups of between three and six adventurers.\nAgain, how many are there in your group?\n\n"))

	#Get each player's info
for num in range(0,playerNum):
    if (num == 0):
        print "\nExcellent! I just need some information about each adventurer. Who wants to be first?\n"
        name = raw_input()
        player1 = {'Name':name, 'Level':1}
    elif (num == 1):
        print "\nNext name for the permit would be?\n"
        name = raw_input()
        player2 = {'Name':name, 'Level':1}
    elif (num == 2):
        print "\nWho wants to be the third?\n"
        name = raw_input()
        player3 = {'Name':name, 'Level':1}
    elif (num == 3):
        print "\nAnd the fourth aspiring adventurer?\n"
        name = raw_input()
        player4 = {'Name':name, 'Level':1}
    elif (num == 4):
        print "\nLucky number five, what name do you go by?\n"
        name = raw_input()
        player5 = {'Name':name, 'Level':1}
    elif (num == 5):
        print "\nYou, the quiet one in the back, what's your name?\n"
        name = raw_input()
        player6 = {'Name':name, 'Level':1}

wiper()
print "\n\n\nOk, this is what I've got for the permit... and it looks like your permit number has been issued.\n\n"

# generates permit and shows info
print "               Munchin Dungeon Exploration Permit - #",random.randrange(873245234)
print "               ------------------------------------------------"
for num in range(0,playerNum):
    if (num == 0):
        print "               ",player1['Name'],"- Level",player1['Level']
    elif (num == 1):
        print "               ",player2['Name'],"- Level",player2['Level']
    elif (num == 2):
        print "               ",player3['Name'],"- Level",player3['Level']
    elif (num == 3):
        print "               ",player4['Name'],"- Level",player4['Level']
    elif (num == 4):
        print "               ",player5['Name'],"- Level",player5['Level']
    elif (num == 5):
        print "               ",player6['Name'],"- Level",player6['Level']
print "               ------------------------------------------------"

# chooses winLevel
winLevel = int(raw_input("\n\n\nWhat level would you like to play to? [min 5/max 15]\n\n"))
while (winLevel > 15 or winLevel < 5):
    winLevel = int(raw_input("\nYou don't listen too well do you? Try picking a winning level between 5 and 15.\n\n"))

print "\n\nOk, I'll declare the winner as soon as one of you munchkins hits level",str(winLevel),"\n\n"

boop = raw_input("Once everyone has gotten their drinks, used the restroom, had a smoke break and found their seats, go ahead and deal out four treasure cards and four door cards to each player.then hit 'Enter'.")

# Determine which player goes first
firstIn = int(random.randrange(playerNum))
nextTurn = firstIn+1

# sets up variables before play
#gameRound = 1   --------Not in use yet
playLog = ''


# A while loop for each player to take their turn
while (player1['Level'] < 10 or player2['Level'] < 10 or player3['Level'] < 10 or player4['Level'] < 10 or player5['Level'] < 10 or player6['Level'] < 10):

    #draw the repeate screen elements
    wiper()
    
    drawBoard()
    
    drawActions()
    
    #drawLog()
    
    #gameRound+1   --------Not in use yet
   
    break       #TAKE THIS OUT OR IT WONT LOOP
else:
    print "Game won!"
