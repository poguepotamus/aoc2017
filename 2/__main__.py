# Day 2 of Advent of Code
# Author: Matthew Pogue
# Date: December 7th, 2017

import fileinput

### GLOBAL VARIBALES ###

DEBUG = True
DBUG = ""
OUTPUT = 0

### FUNCTIONS ###

def getFileInfo():
    spreadsheet = []
    for line in fileinput.input():
        spreadsheet.append(line.split())

    fileinput.close()
    return spreadsheet

def findMax(list):
    max = -1
    for i in list:
        if(max == -1) or (max < int(i)):
            max = int(i)

    return max

def findMin(list):
    min = -1
    for i in list:
        if(min == -1) or (min > int(i)):
            min = int(i)

    return min

### MAIN LINE ###

for line in getFileInfo():
    # print(line)
    OUTPUT += int(findMax(line)) - int(findMin(line))
    DBUG += str(findMax(line)) + " - " + str(findMin(line)) + " = " + str( int(findMax(line)) - int(findMin(line)) ) + " = " + str(OUTPUT) + "\n"

### STANDARD OUT ###

print(OUTPUT)
print(DBUG)