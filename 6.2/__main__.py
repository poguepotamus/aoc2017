# Day 6 part 1 of Advent of Code
# Author: Matthew Pogue
# Date: December 17th, 2017

import fileinput

### DEBUG VARIBALES ###########################################################
DEBUG = False
DBUG = "# = Starting Debugging:\n#   -\n"

### DEBUG FUNCTIONS ###########################################################
def DBUGOUT(levels, trailingLines, info):
    output = "# = " + str(levels) + "\t"
    for i in range(0, levels):
        output += ">\t"
    return output + str(info) + "" + DBUGLINE(trailingLines)

def DBUGLINE(lines):
    output = ""
    for i in range(0, lines):
        output += "#   -\n"
    return output

### GENERAL FUNCTIONS #########################################################
def maxInPos(array):
    output = i = 0
    for i in range(0, len(array)):
        # if array[int(i)] > array[output]:
        #     output = i
        output = i if array[i] > array[output] else output

    return output

### GLOBAL VARIABLES ##########################################################
ANSWER = 0
mem = []
seen = []

### MAIN LINE #################################################################
# adds each number to mem(list)
for line in fileinput.input():
    for word in line.split():
        mem.append(int(word))

while mem not in seen:
    maxPos = maxInPos(mem)
    maxNum = mem[maxInPos(mem)]
    seen.append(list(mem))
    mem[maxPos] = 0
    # range (2, 9)
    for i in range(maxPos + 1, maxPos + maxNum + 1):
        # print(DBUGOUT( 0, 0, str(mem[i % (len(mem) - 1)]) + str(type(mem[i % len(mem)]))))
        mem[i % (len(mem))] += 1
        # print(mem[i % (len(mem) - 1)])

    ANSWER += 1
    # print(str(mem) + " =? " + str(seen))
#     for i in range( maxPos, mem[maxPos] ):
#         mem[ i % len(mem) ] += 1

#     ANSWER += 1

### STANDARD OUT ##############################################################
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================" + ( "\n" if DEBUG else '' ) )
