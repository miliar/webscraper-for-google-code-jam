tc = int(input())for c in range(tc):    print('Case #', end="")    print(c+1,end="")    print(": ", end="")    a,b,k = map(int,input().split())    w = 0    for i in range(a):        for j in range(b):            if i & j < k:                w = w + 1    print(w)