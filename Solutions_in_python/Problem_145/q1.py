import math
from fractions import Fraction
def power_two(n):
    return (math.log(n, 2))
file1 = open('input1.in')
file2 = open('output.txt','w')
a = int(file1.readline())
x = 1
while (a > 0):
    b = file1.readline()
    c = Fraction(b)
    d = float(c)
    den = c.denominator
    if (int(power_two(den)) - power_two(den) == 0.0):
        if (d < 0.5):
            lst = [0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125, 0.00390625, 0.001953125, 0.0009765625, 0.00048828125, 0.000244140625, 0.0001220703125, 6.103515625e-05, 3.0517578125e-05, 1.52587890625e-05, 7.62939453125e-06, 3.814697265625e-06, 1.9073486328125e-06, 9.5367431640625e-07, 4.76837158203125e-07, 2.384185791015625e-07, 1.1920928955078125e-07, 5.960464477539063e-08, 2.9802322387695312e-08, 1.4901161193847656e-08, 7.450580596923828e-09, 3.725290298461914e-09, 1.862645149230957e-09, 9.313225746154785e-10, 4.656612873077393e-10, 2.3283064365386963e-10, 1.1641532182693481e-10, 5.820766091346741e-11, 2.9103830456733704e-11, 1.4551915228366852e-11, 7.275957614183426e-12, 3.637978807091713e-12, 1.8189894035458565e-12, 9.094947017729282e-13]            
            i = 0
            ans = 0
            while (i < 39):
                sex = lst[i]
                sexy = lst[i+1]
                if (sexy <= d < sex):
                    ans = i+2
                    i = 40
                else:
                    i = i+1
            file2.write("Case #%s: %s\n" % (x,ans))
        if (0.5 <= d <= 1.0):
            file2.write("Case #%s: 1\n" % (x))
    else:
        file2.write("Case #%s: impossible\n" % (x))
    a = a-1
    x = x+1
file2.close()
