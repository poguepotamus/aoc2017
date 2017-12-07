# Author: Matthew Pogue
# Date: 12/06/17                                                                                    # Asks for date
# Advent of Code day 1                                                                              # Asks for day of AOC progression

import fileinput

DEBUG = False
DBUG = ""
total = 0

for line in fileinput.input():
    line += line[0]
    last = -1
    for pos in line:
        DBUG += str(last) + str(pos)
        if pos == last:
            DBUG += " = " + str(pos)
            total += int(pos)
        last = pos
        DBUG += "\n"

print(total)

fileinput.close()

if DEBUG:
    print(DBUG)

    # i = 1
    # while( i < len(line) - 1 ):
    #     if( line[i] == line[ i + 1 ] and line[i] == line [ i - 1 ] ):
    #         DBUT += line[i-1] + line[i] + line[i+1] + "\n"
    #         total += int(line[i])
    #     i += 1






    # prev = cur = -1
    # print(line)
    # for nxt in line:
    #     print(nxt)
        # DBOUT += str(prev) + str(cur) + str(nxt) + "\n"
        # if prev == -1:
        #     prev = 0
        # elif cur == -1:
        #     cur = 0
        # elif cur == prev or cur == nxt:
        #     total += int(cur)

# def addString(string):
#     for i in string:
#         total += i




    # last = times = 0
    # line += str( int(line[0]) + 1 )
    # for pos in line:
    #     DBOUT += str(last) + " " + str(pos)
    #     if last == int(pos):
    #         if times == 0:
    #             times = 2
    #         else:
    #             times += 1
    #         DBOUT += " " + str(times)
    #     else:
    #         DBOUT += " " + str(times)
    #         total += (last * times)
    #         times = 0
    #     last = int(pos)
    #     DBOUT += " = " + str(total) + "\n"

    # if line[0] == line[ len(line) - 1 ]:
    #     total += ( int(line[0]) * 2 )



# def handleInput(datafile):
#     lineNum = 1
#     for line in open(datafile):
#         main(line, lineNum)
#         lineNum += 1
#     # map(lambda val:
#     #         sys.stdout.write(str(val) + "\n"),
#     #         (map(lambda line:
#     #                 PrefixPostfixEval(line),
#     #                 [
#     #                     str(line.rstrip('\n'))
#     #                     for line in open(datafile)
#     #                 ]
#     #         )
#     #     )
#     # )

# def toInput(argv=None):
#     if (len( sys.argv[1:]) == 0 ):
#         main('/mnt/e/matth/Dropbox/matthew/projects/aoc/day1/input.txt')                            # Asks for day of AOC progression
#     elif (len( sys.argv[1:]) == 1 ):
#         main( sys.argv[1:][0] )
#     else:
#         print >> sys.stderr, "Invalid number of paramaters, expecting only one."
#         return 2

# if __name__ == "__main__":
#     sys.exit(toInput())