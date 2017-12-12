# Day 5 of Advent of Code
# Author: Matthew Pogue
# Date: December 9th, 2017

import fileinput

### GLOBAL VARIBALES ###
DEBUG = False
DBUG = "# = Starting Debugging:\n#   -\n"
ANSWER = 0

### DEBUG FUNCTIONS ###
def addDBUG(levels, trailingLines, info):
    levels += 1
    # output = "# = " + str(levels) + "\t"

    # while levels > 1:
    #     output += ">\t"
    #     levels -= 1

    # output +=  str(info) + "\n"

    # while trailingLines > 0:
    #     output += "#   -\n"
    #     trailingLines -= 1

    # global DBUG
    # DBUG += output

### GENERAL FUNCTIONS ###
def run( instructions, startPos ):
    pos = startPos
    steps = 1
    while ( ( instructions[pos] + pos ) < len(instructions) and ( instructions[pos] + pos ) >= 0 ):
        addDBUG( 1, 0, "Position: " + str(pos) + " | Step: " + str(steps) )
        addDBUG( 2, 0, str(instructions[pos]) + " -> " + str( instructions[pos] + 1 ) )
        addDBUG( 2, 0, "Moving to position " + str( pos + instructions[pos] ) )
        instructions[pos] += 1
        pos += instructions[pos] - 1
        addDBUG( 2, 0, "Moving to position " + str(pos) ) 
        addDBUG( 2, 0, "Step from " + str(steps) )
        steps = steps + 1
        addDBUG( 2, 1, "Step to " + str(steps) )

    return steps

### MAIN LINE ###
instructions = []
for instruction in fileinput.input():
    instructions.append(int(instruction))
ANSWER = run( instructions, 0 )

### STANDARD OUT ###
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================" + ( "\n" if DEBUG else '' ) ) 
