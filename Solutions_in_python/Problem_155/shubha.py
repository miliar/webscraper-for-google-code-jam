g = open('/Users/shubham/Desktop/A-small-attempt2ans.in.txt','w+')

with open('/Users/shubham/Desktop/A-large.in', 'r+') as m:
    num_cases = int(m.readline())
    
    for i in range(num_cases):
        max_shy, crowd = m.readline().split(' ')
        crowd = list(crowd)[:-1]
        current = 0
        num_friends = 0
        
        for j, k in enumerate(crowd):
            if current >= j:
                current += int(k)
            else:
                num_friends += (j - current)
                current += (int(k) + (j - current))

        g.write('Case #' + str(i+1) + ': ' + str(num_friends) + '\n')
        
g.close()