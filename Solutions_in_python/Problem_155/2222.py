#!/usr/bin/python4.9.2
g = open('/home/yoo/Downloads/A-small-attempt1.out','w+')
f = open('/home/yoo/Downloads/A-large.in' , 'r+') 
num_cases = int(f.readline())
for i in range(num_cases):
	max_shy, crowd = f.readline().split(' ')
        crowd = list(crowd)[:-1]
        current_standing = 0
        num_friends = 0
        for j, k in enumerate(crowd):
            if current_standing >= j:
                current_standing += int(k)
            else:
                num_friends += (j - current_standing)
                current_standing += (int(k) + (j - current_standing))
        g.write('Case #' + str(i+1) + ': ' + str(num_friends) + '\n')
g.close()
