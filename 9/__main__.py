
# Day 8 part 1 of Advent of Code
# Author: Matthew Pogue
# Date: December 22nd, 2017

### LIBRARIES AND FILES #######################################################
## LIBRARIES ##########################

## FILES ##############################

class StreamProcessor:
    def __init__(self, input):
        self.line = input
        self.score = 0
        self.scoreMul = 1
        self.garbage = False
        self.erasedCharacters = 0

        if line[0] != '#':
            self.processStream()
            self.printAnswer()

    def processStream(self):
        while len(self.line) > 0:
            # Collecting the currently read bit, and also removing that bit
            # from the line information
            bit = self.bite()

            if not self.garbage:
                # If the bit is a character that we don't care about
                if bit == '}':
                    # Decrease score multiplier by 1 as a group should have just ended
                    self.scoreMul -= 1
                    # print(self.scoreMul)
                    continue

                # If the bit is starting a group
                elif bit == '{':
                    # Increase the score and the score multiplier
                    self.score += self.scoreMul
                    self.scoreMul += 1
                    continue

                # If the bite starts garbage
                elif bit == '<':
                    # Telling the object that we are in garbage territory and that we should be processing garbage
                    self.garbage = True

            else: # If we are in garbage land
                if bit == '!':
                    self.bite()
                    continue
                elif bit == '>':
                    self.garbage = False
                    continue
                else:
                    self.erasedCharacters += 1
                    continue

    def bite(self):
        bit = self.line[0]
        self.line = self.line[1:]
        return bit

    def printAnswer(self):
        print(f'{self.score}: {self.erasedCharacters}')

# def getFileData(filePath):
#     with open(filePath) as file:
#         return file.read().split('\n')

# streamProcessor = StreamProcessor(getFileData('9/testInput.txt'))
# # streamProcessor = StreamProcessor('9/input.txt')
# streamProcessor.processStream()
# print(streamProcessor.getAnswerString())


# filePath = '9/testInput2.txt'
filePath = '9/input.txt'
with open(filePath) as file:
    for line in file.read().split('\n'):
        StreamProcessor(line)