# Day 3 part 2 of Advent of Code
# Author: Matthew Pogue
# Date: December 7th, 2017

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

def checkPassphrase(passphrase):
    # addDBUG( 1, passphrase.lstrip() )
    addDBUG( 1, 0, passphrase[:-1] if passphrase[-1:] == "\n" else passphrase )
    quit = False
    for word in passphrase.split():
        if passphrase.split().count(word) > 1:
            addDBUG( 2, 0, word + " found " + str(passphrase.split().count(word)) + " times" )
            passes = False
            quit = True

        else:
            passes = True

        if quit:
            break

    return passes

### MAIN LINE ###
for passes in list( map( checkPassphrase, fileinput.input() ) ):
    ANSWER += 1 if passes else 0

fileinput.close()

### STANDARD OUT ###
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================\n" )
