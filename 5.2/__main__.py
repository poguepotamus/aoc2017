# Day 5 part 2 of Advent of Code
# Author: Matthew Pogue
# Date: December 9th, 2017

import fileinput

### DEBUG VARIBALES ###
DEBUG = False
DBUG = "# = Starting Debugging:\n#   -\n"

### DEBUG FUNCTIONS ###
def addDBUG(levels, trailingLines, info):
    output = "# = " + str(levels) + "\t"

    while levels > 1:
        output += ">\t"
        levels -= 1

    output +=  str(info) + "\n"
    DBUGLine(trailingLines)
    global DBUG
    DBUG += output

def DBUGLine(lines):
    while lines > 1:
        output += "#   -\n"
        lines -= 1

### GENERAL FUNCTIONS ###

## GLOBALS ##
ANSWER = 0
nextPos = 0
step = 0
inst = []

### MAIN LINE ###
# Gets lines into list named inst
for line in fileinput.input():
    inst.append(int(line))

# while nextPos exists in array
while nextPos >= 0 and nextPos < len(inst):
    if inst[nextPos] >= 3:
        inst[nextPos] -= 1
        nextPos = nextPos + inst[nextPos] + 1

    else:
        inst[nextPos] += 1
        nextPos = nextPos + inst[nextPos] - 1

    step += 1

ANSWER = step

### STANDARD OUT ###
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================" + ( "\n" if DEBUG else '' ) )
