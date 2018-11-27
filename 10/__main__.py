
# Day 8 part 1 of Advent of Code
# Author: Matthew Pogue
# Date: December 22nd, 2017

### LIBRARIES AND FILES #######################################################
## LIBRARIES ##########################

## FILES ##############################
filePath = '9/input.txt'
with open(filePath) as file:
    for count, line in enumerate(file.read().split('\n')):
        # Removing commented lines
        if line[0] == '#':
            break

        # Setting some variables that we will need to keep track of.
        score = 0
        scoreMul = 1
        garbage = False
        ignore = False
        erasedCharacters = 0

        # Scanning through the line
        for char in line:
            if ignore:
                ignore = False

            elif char == '!':
                ignore = True

            elif not garbage:
                if char == '<':
                    garbage = True

                elif char == '{':
                    score += scoreMul
                    scoreMul += 1

                elif char == '}':
                    scoreMul -= 1
            else:
                if char == '>':
                    garbage = False

                else:
                    erasedCharacters += 1

        print(f'Line #{count+1} had score of {score} and deleted {erasedCharacters} characters.')