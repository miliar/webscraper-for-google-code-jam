import sys
d = {' ': ' ', 'a': 'y', 'c': 'e', 'b': 'h', 'e': 'o', 'd': 's', 'g': 'v', 'f': 'c', 'i': 'd', 'h': 'x', 'k': 'i', 'j': 'u', 'm': 'l', 'l': 'g', 'o': 'k', 'n': 'b', 'q': 'z', 'p': 'r', 's': 'n', 'r': 't', 'u': 'j', 't': 'w', 'w': 'f', 'v': 'p', 'y': 'a', 'x': 'm', 'z': 'q'}

x = 0
y = False
for i in open('A-small-attempt0.in', 'r'):
    if not y:
        y = True
        continue
    x+=1
    print "Case #%d: " % x, 
    for c in i.strip():
        sys.stdout.write(d[c])
    sys.stdout.write('\n')