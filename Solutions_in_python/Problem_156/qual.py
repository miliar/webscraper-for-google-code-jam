import math

def standing_ovation():
    inputs = open('standing-ovation.txt', 'r')
    output = open('standing-ovation-ans.txt', 'w')
    cases = int(inputs.readline())

    for case in range(0, cases):
        info = inputs.readline().split(' ')

        max_shyness = int(info[0])
        num_standing = 0
        num_needed = 0
        for i in range(0, max_shyness+1):
            if num_standing < i:
                num_needed += (i - num_standing)
                num_standing = i
            num_standing += int(info[1][i])
        result = 'Case #%d: %d\n' % (case+1, num_needed)
        output.write(result)

def pancakes():
    inputs = open('B-large.in', 'r')
    output = open('B-small-ans.txt', 'w')
    cases = int(inputs.readline())

    for case in range(0, cases):
        num_diners = int(inputs.readline())
        pancakes = inputs.readline().split(' ')

        count = [0] * 1001
        maxi = 0
        for pancake in pancakes:
            if int(pancake) > maxi:
                maxi = int(pancake)
            count[int(pancake)] += 1

        mini = maxi

        for i in range(1, maxi):
            turns = i
            for j in range(i+1, len(count)):
                if count[j] > 0:
                    turns += count[j] * int(math.ceil(j/float(i))-1)
                if turns >= mini:
                    break
            if turns < mini:
                mini = turns

        result = 'Case #%d: %d\n' % (case+1, mini)

        output.write(result)


def dominos():
    inputs = open('D-small-attempt2.in', 'r')
    output = open('D-small-ans.txt', 'w')
    cases = int(inputs.readline())

    for case in range(0, cases):
        variables = inputs.readline().split(' ')
        X = int(variables[0])
        R = int(variables[1])
        C = int(variables[2])
        possible = True

        smaller = min(R,C)
        larger = max(R,C)

        if (R * C) % X != 0:
            possible = False
        elif X > larger:
            possible = False
        elif X >= 2 * smaller + 1:
            possible = False
        elif X >= 7:
            possible = False
        elif X == 4 and smaller == 2:
            possible = False
        elif X == 6 and smaller == 3:
            possible = False
        elif X == 6 and smaller == 4 and larger == 6:
            possible = False


        result = ''

        if possible:
            result = 'Case #%d: %s\n' % (case+1, 'GABRIEL')
        else:
            result = 'Case #%d: %s\n' % (case+1, 'RICHARD')

        output.write(result)

pancakes()