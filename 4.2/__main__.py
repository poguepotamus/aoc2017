# Day 4 part 2 of Advent of Code
# Author: Matthew Pogue
# Date: December 9th, 2017

import fileinput

### GLOBAL VARIBALES ###
DEBUG = True
DBUG = "# = Starting Debugging:\n#   -\n"
ANSWER = 0

### FUNCTIONS ###
def addDBUG(levels, trailingLines, info):
    output = "# = " + str(levels) + "\t"

    while levels > 1:
        output += ">\t"
        levels -= 1

    output +=  str(info) + "\n"

    while trailingLines > 0:
        output += "#   -\n"
        trailingLines -= 1

    global DBUG
    DBUG += output

def containsDouble(passphrase):
    # addDBUG( 1, passphrase.lstrip() )
    addDBUG( 1, 0, passphrase[:-1] if passphrase[-1:] == "\n" else passphrase )
    for word in passphrase.split():
        if passphrase.split().count(word) > 1:
            addDBUG( 2, 0, word + " found " + str(passphrase.split().count(word)) + " times" )
            return True

    return False

def containsAnagram(passphrase):
    for x in passphrase.split():
        for y in passphrase.split():
            if isAnagram( x, y ) and (x != y):
                addDBUG( 2, 0, x + " is an anagram of " + y )
                return True

    return False

def isAnagram( x, y ):
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def checkPassphrase(passphrase):
    if containsDouble(passphrase) or containsAnagram(passphrase):
        return False
    else: 
        return True

### MAIN LINE ###
for passes in list( map( checkPassphrase, fileinput.input() ) ):
    ANSWER += 1 if passes else 0

fileinput.close()

### STANDARD OUT ###
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================\n" )
