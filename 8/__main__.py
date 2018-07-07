# Day 8 part 1 of Advent of Code
# Author: Matthew Pogue
# Date: December 22nd, 2017

import fileinput

### DEBUG VARIABLES ###########################################################
DEBUG = False
DBUG = "# = Starting Debugging:\n#   -\n"

### GENERAL FUNCTIONS #########################################################
def getFileInfo():
    file = []
    for line in fileinput.input(): file.append(line)
    fileinput.close()
    return file

def check(reg, op, num):
    if op == '==':
        return True if MEM[reg] == num else False
    elif op == '!=':
        return True if MEM[reg] != num else False
    elif op == '>':
        return True if MEM[reg] > num else False
    elif op == '>=':
        return True if MEM[reg] >= num else False
    elif op == '<':
        return True if MEM[reg] < num else False
    elif op == '<=':
        return True if MEM[reg] <= num else False

### GLOBAL VARIABLES ##########################################################
FILE = getFileInfo()
ANSWER = ""
MEM = {}

### MAIN LINE #################################################################
for line in FILE:
    linx = line.split()
    MEM[linx[0]] = 0 if linx[0] not in MEM else MEM[linx[0]] # Adds new register if it doesn't exist and sets register to 0
    MEM[linx[0]] += linx[2] * (1 if linx[1] == 'inc' else -1) * (1 if check(linx[4], linx[5], int(linx[6])) else 0)

maxValue = int(None)
for key, value in MEM:
    if value > maxValue

### STANDARD OUT ##############################################################
print( ( ( DBUG + "#   -\n# = End of Debugging:\n\n" ) if DEBUG else '' ) + "========================\n  ANSWER = " + str(ANSWER) + "\n========================" + ( "\n" if DEBUG else '' ) )
