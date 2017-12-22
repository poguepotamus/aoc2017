# Day 7 part 1 of Advent of Code
# Author: Matthew Pogue
# Date: December 18th, 2017

import fileinput

### DEBUG VARIABLES ###########################################################
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
def getFileInfo():
    file = []
    for line in fileinput.input(): file.append(line)
    fileinput.close()
    return file

def findDiff(x, y):
    y = set(y)
    return [i for i in x if i not in y]

### GLOBAL VARIABLES ##########################################################
ANSWER = ""
FILE = getFileInfo()
MAINLIST = []
SLIST = []

### MAIN LINE #################################################################
for line in FILE:
    line = line.replace(',', '')
    linx = line.split()
    MAINLIST.append(linx[0])
    for i in range(3, len(linx)):
        SLIST.append(linx[i]) if linx[i] not in SLIST else None

ANSWER = findDiff(MAINLIST, SLIST)

### STANDARD OUT ##############################################################
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================" + ( "\n" if DEBUG else '' ) )
