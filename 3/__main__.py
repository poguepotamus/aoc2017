# Day 3 of Advent of Code
# Author: Matthew Pogue
# Date: December 7th, 2017

import fileinput

### GLOBAL VARIBALES ###
DEBUG = True
DBUG = "Starting Debugging:\n#\n"
OUTPUT = 0

### FUNCTIONS ###
def findRange(num, showDBUG):
    global DBUG
    lat = 0
    x = xl = 1
    DBUG += "#\tFinding range\n" if showDBUG == True else ''
    while int(num) > x:
        lat += 1
        xl = x
        x += lat * 8
        DBUG += "#\t|\t" + str(xl) + "+" + str(lat * 8) + "=" + str(x) + "|" + str(lat) + "\n" if showDBUG == True else ''

    DBUG += "#\tRange = (" + str(xl) + " < " + line + " < " + str(x) + ") with lateral " + str(lat) + "\n#\n" if showDBUG == True else ''
    return [xl, lat]

def findSteps(xl, lat):
    global DBUG
    i = int(line) - int(xl)
    DBUG += "#\t" + line + " - " + str(xl) + " = " + str(i) + "\n"
    j = int(lat) * 2
    DBUG += "#\t" +str(lat) + " * 2 = " + str(j) + "\n"
    k = i % j
    DBUG += "#\t" +str(i) + " % " + str(j) + " = " + str(k) + "\n"
    return k

### MAIN LINE ###
for line in fileinput.input():
    OUTPUT = 1 if int(line) == 1 else findSteps( findRange(line, True)[0], findRange(line, False)[1] )

fileinput.close()

### STANDARD OUT ###
print ( DBUG + "#\nEnd of Debugging:\n\n" if DEBUG else '') + "========================\n  ANSWER = " + str(OUTPUT) + "\n========================\n"
