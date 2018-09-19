#!/usr/bin/env python3.4
import sys
import math

multiplication = {
    '1': {
        '1': (1, '1'),
        'i': (1, 'i'),
        'j': (1, 'j'),
        'k': (1, 'k')
    },
    'i': {
        '1': (1, 'i'),
        'i': (-1, '1'),
        'j': (1, 'k'),
        'k': (-1, 'j')
    },
    'j': {
        '1': (1, 'j'),
        'i': (-1, 'k'),
        'j': (-1, '1'),
        'k': (1, 'i')
    },
    'k': {
        '1': (1, 'k'),
        'i': (1, 'j'),
        'j': (-1, 'i'),
        'k': (-1, '1')
    }
}

def mult(tu, l):
    sign, sym = multiplication[tu[1]][l]
    return tu[0] * sign, sym
def fileRead(filename):
    #"function_docstring"
    #except IOError:
    lines = [line.strip() for line in open(filename)]
    return lines
def lineToCompute(letterCount,repeat,loop,testCase):
    
    return 0
        
def main():
    lines = fileRead("C-large.in")
    count = 1
    #testCase = 0
    margin = int(lines[0])*2
    for testCase in range(int(lines[0])):
        #print count
        #numDiners = lines[count]
        #DinerPK = lines[count+1]
        letterCount, repeat = map(int, lines[count].split())
        #print letterCount, repeat
        loop = lines[count+1]
        count = count+2
        cur = (1, '1')
        cursor = 0
        while cursor < 4 * letterCount:
            cur = mult(cur, loop[cursor % letterCount])
            cursor += 1
            if cur[0] == 1 and cur[1] == 'i':
                break
        if 4 * letterCount == cursor:
            print('Case #%d: NO' % (testCase + 1))
        else:
            cur = (1, '1')
            while cursor < 8 * letterCount:
                cur = mult(cur, loop[cursor % letterCount])
                cursor += 1
                if cur[0] == 1 and cur[1] == 'j':
                    break
            if 8 * letterCount == cursor:
                print('Case #%d: NO' % (testCase + 1))
            else:
                cur = (1, '1')
                while cursor < 12 * letterCount:
                    cur = mult(cur, loop[cursor % letterCount])
                    cursor += 1
                    if cur[0] == 1 and cur[1] == 'k':
                        break
                if 12 * letterCount == cursor:
                    print('Case #%d: NO' % (testCase + 1))
                elif repeat <= (cursor - 1) // letterCount:
                    print('Case #%d: NO' % (testCase + 1))
                else:
                    cur = (1, '1')
                    remaining = (repeat - 1 - (cursor - 1) // letterCount) % 4
                    while cursor % letterCount != 0:
                        cur = mult(cur, loop[cursor % letterCount])
                        cursor += 1
                    for i in range(remaining * letterCount):
                        cur = mult(cur, loop[cursor % letterCount])
                        cursor += 1
                    if cur[0] == 1 and cur[1] == '1':
                        print('Case #%d: YES' % (testCase + 1))
                    else:
                        print('Case #%d: NO' % (testCase + 1))
        
        
main()
