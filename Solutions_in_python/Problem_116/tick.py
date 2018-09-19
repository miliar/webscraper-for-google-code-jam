def counter(string):
    x=string.count('X')
    o=string.count('O')
    d=string.count('.')
    t=string.count('T')
    return (x,o,t,d)

def win(tupa):
    if((tupa[0]==3 and tupa[2]==1) or tupa[0]==4):
        print 'Case #'+str(i)+': X won'
        return True
    elif((tupa[1]==3 and tupa[2]==1)or tupa[1] ==4):
        print 'Case #'+str(i)+': O won'
        return True
    return False
                
t=input()
for i in range(1,t+1):
    a=[[],[],[],[]]
    status=True
    flag=False
    a[0]=raw_input()
    if(len(a[0])==0):
        a[0]=raw_input()
    a[1]=raw_input()
    a[2]=raw_input()
    a[3]=raw_input()

    for p in range(0,4):            #horizontal case
        tup=counter(a[p])
        if(tup[3]>0):
            flag=True
        if(win(tup)):
            status=False
            break
    if(not status):
            continue

    for p in range(0,4):                                            
        tup=counter(a[0][p]+a[1][p]+a[2][p]+a[3][p])
        if(tup[3]>0):
            flag=True
        if( win(counter(a[0][p]+a[1][p]+a[2][p]+a[3][p]))):
            status=False
            break
    if(not status):
            continue

    if(win(counter(a[0][0]+a[1][1]+a[2][2]+a[3][3]))):          #diagonal
        status=False
        continue
    if(win(counter(a[3][0]+a[2][1]+a[1][2]+a[0][3]))):
        status=False
        continue
    
    if(status and flag):   
        print 'Case #'+str(i)+': Game has not completed'
        continue
    print 'Case #'+str(i)+': Draw'
