#!/usr/bin/python

# kalin.jenkins@gmail.com - last edited   11/09/2013 
#
# thouShaltPass.py can be used on it's own at the command line or copy the passGenner function (everything between the two line blocks) into your own script to use the generation in your own project. Make sure to put a wordlist.txt file into the same folder as this script for dictionary match error checking.
#
# This tool is intended to be downloaded and run locally on a machine to generate a password so that the password is not sent to the user in the clear over http traffic.

tsp_version = '1.2'

#----------------------------------------------------------------

import re
import random
import string
import sys

#passGenner(length of the password[8-20], if caps are to be used[y/n], if punctuation is to be used[y/n], if numbers are to be used[y/n]
   
def passGenner(length, caps, punct, nums):
    # initialize passOutput
    passOutput = ''
    
    # use a loop to generate a password of passLength
    while (passOutput.__len__() < length):
        # determine to add an lower, caps, punct or num
        charChoice = ''
        
        lowerRoll = random.randrange(1,1000)
        charChoice = 'l'
        charHigh = lowerRoll
        if (caps == 'y'):
            capsRoll = random.randrange(1,1000)
            if (capsRoll > charHigh):
                charChoice = 'c'
                charHigh = capsRoll
        if (punct == 'y'):
            punctRoll = random.randrange(1,1000)
            if (punctRoll-250 > charHigh):
                charChoice = 'p'
                charHigh = punctRoll
        if (nums == 'y'):
            numsRoll = random.randrange(1,1000)
            if (numsRoll > charHigh):
                charChoice = 'n'
                charHigh = numsRoll
        
        # get a random character from the highest rolling character set and append it to passOutput
        if (charChoice == 'l'):
            lowerAdd = random.choice(string.letters).lower()
            passOutput += lowerAdd
        if (charChoice == 'c'):
            lowerAdd = random.choice(string.letters)
            passOutput += lowerAdd
        if (charChoice == 'p'):
            punctAdd = random.choice(string.punctuation)
            passOutput += punctAdd
        if (charChoice == 'n'):
            numberAdd = str(random.randrange(0,9))
            passOutput += numberAdd

    # check the passOutput for any dictionary words
    
    # passOutput = 'bolt'        ----- enter a dictionary word here to test the wordllist matching
    
    datafile = file('wordlist.txt') 
    for line in datafile:
        if passOutput in line:
            passOutput = 'error'

    return [passOutput]
    
#----------------------------------------------------------------

sys.stderr.write("\x1b[2J\x1b[H")	# clears the screen, only works on ANSI (*nix)

print "\n\n            thouShaltPass secure password generator : version",tsp_version
print "            last modified 11/09/2013\n\n"

# sets the password length to be generated
passLength = int(raw_input("How long would you like the password to be? [8-20 characters]"))
while (passLength > 20 or passLength < 8 ):
    passLength = int(raw_input("Try Again. How long would you like the password to be? [8-20 characters]"))

# sets if upper case letters are to be used in the password
useUpper = raw_input("Would you like to use upper-case letters in the password?[y/n]")
if not re.match("[yn]", useUpper):
    useUpper = raw_input("Enter 'y' or 'n'. Would you like to use upper-case letters in the password?")

# sets if punctuation is to be used in the password
usePunct = raw_input("Would you like to use punctuation characters in the password?[y/n]")
if not re.match("[yn]", usePunct):
    usePunct = raw_input("Enter 'y' or 'n'. Would you like to use punctuation characters in the password?")

# sets if number is to be used in the password
useNums = raw_input("Would you like to use numbers in the password?[y/n]")
if not re.match("[yn]", useNums):
    useNums = raw_input("Enter 'y' or 'n'. Would you like to use numbers in the password?")


# gets password from criteria and displays it or an error
passOutput = passGenner(passLength, useUpper, usePunct, useNums)

if 'error' in passOutput:
    print "\n\n                     The password generated did not pass safety/security checks or was malformed.\n\nThe most likely (although still statistically very rare) reason is that the password generated contained a word in thouShaltPass' comparison dictionary. Please run thouShaltPass.py again to generate another password. If you see this error again, most likely a dependency is not active or something is broken.\n\n"
else:
    #print "\n\n"
    #print "Password generated with the following criteria:"
    #print "Password Length:               ",passLength
    #print "Use lower/upper case letters:   ",useUpper.title()
    #print "Use punctuation:                ",usePunct.title()
    #print "Use numbers:                    ",useNums.title()
    print "\n\n"
    print "            Generated password: ",passOutput,"\n\n"
    print "Please copy and paste this password somewhere safe before use or alternatively use a trusted password management system such as http://keepass.info/\n\n"


