'''
Created on Apr 13, 2013

@author: hwy
'''

nums =[1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004]

def init():
    w = open('ou.txt', 'w')
    f = open('C-large-1.in', 'r')
    num = int(f.readline())
    for i in range(1, num + 1):
        out = 0
        w.write('Case #' + str(i) + ': ')
        [a, b] = [int(s) for s in f.readline().split()]
        j = 0;
        while j <39 and nums[j] < a:
            j += 1
        while j <39 and nums[j] <= b:
            j += 1
            out += 1
        w.write(str(out) + '\n')

if __name__ == '__main__':
    init();