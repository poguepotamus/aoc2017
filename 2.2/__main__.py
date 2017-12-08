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
    exit = False
    for char1 in line:
        for char2 in line:
            if( ( float(char1) / float(char2) ).is_integer() and ( float(char1) / float(char2) > 1 ) ):
                DBUG += char1 + " " + char2 + "\n"
                OUTPUT += int(char1) / int(char2)
                exit = True
                
            if exit:
                break

        if exit:
            break

### STANDARD OUT ###

print("=======================")
print("ANSWER = " + str(OUTPUT))
print("=======================")
print(DBUG)