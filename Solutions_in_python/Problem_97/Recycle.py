Ifile=open('ReInput.txt')
Ofile=open('ReOutput.txt','w')
T=int(Ifile.readline().strip())
k=1
while(k<=T):
	l=[]
	count=0
	l=Ifile.readline().strip().split()
	i1=int(l[0])
	i2=int(l[1])
	Ofile.write("Case #%d: "%(k))
	while(i1<=i2):
		a=int(i1%10)
		b=int(i1/10)
		if(b<10):
			c=(a*10)+b
		elif(10<=b<100):
			c=(a*100)+b
		else:
			c=(a*1000)+b
		if(int(l[0])<=c<=int(l[1])):
			if(i1<c):
				count=count+1
		if(10<=b<100):
			a=int(int(c)%10)
			b=int(int(c)/10)
			d=(a*100)+b
			if(int(l[0])<=d<=int(l[1])):
				if(i1<d):
					count=count+1
		else:
			a=int(int(c)%10)
			b=int(int(c)/10)
			d=(a*1000)+b
			if(int(l[0])<=d<=int(l[1])):
				if(i1<d):
					count=count+1
			a=int(int(d)%10)
			b=int(int(d)/10)
			e=(a*1000)+b
			if(int(l[0])<=e<=int(l[1])):
				if(i1<e):
					count=count+1
		i1=i1+1
	Ofile.write("%d"%(count))
	Ofile.write('\n')
	k=k+1
Ifile.close()
Ofile.close()