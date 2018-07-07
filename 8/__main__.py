
# Day 8 part 1 of Advent of Code
# Author: Matthew Pogue
# Date: December 22nd, 2017

### LIBRARIES AND FILES #######################################################
## LIBRARIES ##########################
import os

## FILES ##############################

print('Libraries have been imported')

class JumpHelper:
    def __init__(self, filePath):
        # Creating useful object variables
        self.fileData = self.getFileInfo(filePath)
        self.answer = ''
        self.memory = {}
        self.memoryMax = None

    def process(self):
        for line in self.fileData:
            print(f'Evaluating {line}')

            # Splitting the line by spaces and placing them in an array
            piece = line.split()

            # Checking the if statement
            if self.checkStatement( *piece[-3:] ):
                self.alterRegister( *piece[:3] )

    def getAnswer(self):
        # Creating a answer spot for the maximum value
        maxValue = None
        maxReg = None
        print(f'Current registers')
        for key, value in self.memory.items():
            print(f'    {key}: {value}')
            if maxValue is None:
                maxValue = int(value)
                maxReg = key
            elif int(value) > maxValue:
                maxValue = value
                maxReg = key

        ### STANDARD OUT ##############################################################
        print(f'Register with highest value:')
        print(f'    {maxReg}: {maxValue}')
        print(f'    And the highest number EVER was: {self.memoryMax}')

    ### GENERAL FUNCTIONS #########################################################
    def getFileInfo(self, filePath):
        # Collecting the file information in variable fileData
        with open(filePath) as file:
            fileData = file.read().split('\n')

        return fileData

    def checkStatement(self, reg, op, num):
        # Creating the register if it doesn't exist
        self.touchReg(reg)
        num = int(num)

        # Checking each of the operators, then returning the answer of an if
        # statement depending on if its correct
        if op == '==':
            return True if self.memory[reg] == num else False
        elif op == '!=':
            return True if self.memory[reg] != num else False
        elif op == '>':
            return True if self.memory[reg] > num else False
        elif op == '>=':
            return True if self.memory[reg] >= num else False
        elif op == '<':
            return True if self.memory[reg] < num else False
        elif op == '<=':
            return True if self.memory[reg] <= num else False
        else:
            raise Error('Unknown operator {op} in checkStatement(reg, op, num)')

    def touchReg(self, register):
        # CHecking to see if register exists in virtual memory
        if register not in self.memory.keys():
            # If not, then we initialize it here
            self.memory[register] = 0

    def alterRegister(self, reg, op, num):
        # Creating a register if it doesn't exist
        self.touchReg(reg)
        num = int(num)

        if self.memoryMax is None:
            self.memoryMax = self.memory[reg]
        elif self.memoryMax < self.memory[reg]:
            self.memoryMax = self.memory[reg]

        # Checking each operators, then altering the register
        if op == 'inc':
            self.memory[reg] += num
        elif op == 'dec':
            self.memory[reg] -= num
        else:
            raise Error('Unknown operator {op} in alterRegister(reg, op, num)')

        print(f'    {reg} = {self.memory[reg]}')

jumpHelper = JumpHelper('8/input.txt')
jumpHelper.process()
jumpHelper.getAnswer()