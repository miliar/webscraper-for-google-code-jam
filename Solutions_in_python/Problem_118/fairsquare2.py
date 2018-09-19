#Fairsquare in Python?
#Mainly to deal with da big numbers
import math

fin = open('fairsquare.in','r')
fout = open('fairsquare.out','w')

N = int(fin.readline())

fairsquares = [1,4,9,121,484,10201,12321,14641,40804,44944,1002001,1234321,4008004,100020001,102030201,104060401,121242121,123454321,125686521,400080004,404090404,10000200001,10221412201,12102420121,12345654321,40000800004,1000002000001,1002003002001,1004006004001,1020304030201,1022325232201,1024348434201,1210024200121,1212225222121,1214428244121,1232346432321,1234567654321,4000008000004,4004009004004,100000020000001]

def fairSquares(a, b):
	begin = 0
	end = 0
	for i in range(len(fairsquares)):
		if a <= fairsquares[i]:
			begin = i
			break
	for i in range(len(fairsquares)):
		if b <= fairsquares[i]:
			end = i
			break
			
	return end - begin

for count in range(N):
	A, B = fin.readline().split()
	A = int(A)
	B = int(B) + 1#This way it also checks B
	#print(str(A) + " " + str(B))
	#print(A + B)
	
	fout.write("Case #" + str(count + 1) + ": " + str(fairSquares(A, B)) + "\n")

fin.close()
fout.close()
