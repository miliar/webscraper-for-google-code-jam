import math
data="""100
222.34608 3.03001 120.80033
491.75015 1.48217 1959.10831
492.93635 1.03653 1983.72274
1.04653 3.49588 1999.26868
7.98 3.0 1196.0
150.82217 2.317 230.1
391.96548 1.51189 1965.64032
96.83581 2.47681 799.80829
500.0000 1.39 1047.38137
497.00000 2.00000 994.00000
42.27 3.25 1966.3060
110.69427 4.00 1514.8354
498.0 3.0 1608.0
274.00000 1.00000 277.00000
176.441 3.0 298.7040
231.96506 2.32297 1544.54432
1.08391 3.70950 1999.87351
496.14271 1.31165 1995.27984
360.0 1.0 533.0
85.00000 2.00000 170.00000
96.86197 1.36257 1148.02619
491.76213 1.32988 1953.36936
41.52236 3.44336 1670.59426
282.005 1.085 711.7780
442.87312 2.81878 1612.03540
1.01349 3.44688 1999.92829
20.09 1.039 134.9144
358.00000 2.00000 366.00000
495.85896 1.39279 1978.58356
60.0 3.0 1225.0
75.0 3.0 1094.0
490.83194 1.06235 1916.50826
134.97398 2.73948 794.31479
236.0 4.0 1312.0
215.0 3.0 379.0
340.00000 3.00000 355.00000
491.82126 1.29796 1941.19695
492.50370 1.29662 1986.13735
369.4 3.6927 1779.76768
332.28097 2.41729 1567.85077
490.20883 1.28698 1924.52970
493.68056 1.33732 1984.90182
493.78969 1.32374 1985.36714
1.00000 2.6035 371.18
498.09974 1.27231 1972.66785
351.403 2.43 517.0
61.23298 2.17985 800.13561
490.13869 1.04284 1970.41456
161.0 2.0 117.0
497.72443 1.49213 1982.52322
335.01193 1.88093 361.30482
258.560 3.1055 816.327
138.0 3.0 73.0
497.32311 1.29172 1927.03321
498.34732 1.42217 1936.09909
132.41535 2.99973 468.91784
496.61180 1.24516 1929.94173
272.860 1.2859 39.1438
94.45641 3.00906 1339.02588
490.68969 1.14884 1988.97750
491.96644 1.05477 1995.54390
498.73574 1.10334 1966.44826
219.094 1.918 1.0
493.47275 1.01174 1961.77687
493.69153 1.01004 1957.32455
413.0 3.0 634.0
498.43855 1.18658 1923.05139
128.62812 3.2384 1602.235
438.0 3.0 577.0
494.91326 1.23120 1954.23960
421.53780 3.53254 658.12943
1.08765 3.32577 1999.23052
1.26959 3.73139 3.17329
101.6872 1.78720 1970.0
289.0 3.0 1769.0
307.49790 1.67041 170.61940
127.59576 1.16803 930.73766
290.00000 2.00000 580.00000
323.00000 2.00000 646.00000
35.66455 3.36575 58.59066
490.95944 1.09463 1962.06117
497.48407 1.06809 1982.96592
430.00000 1.00000 468.00000
145.7518 2.6 2000.0000
63.0 3.0 701.0
496.65116 1.34972 1991.80681
353.0 3.0 1379.0
498.54956 1.35855 1976.66750
498.64319 1.06335 1912.72080
495.92072 1.00259 1990.32991
254.23425 2.37003 585.12086
495.83021 1.05572 1984.25367
473.44412 2.67602 1289.75861
187.0 1.00 1885.63
496.88616 1.28584 1968.73068
287.02615 3.37350 1966.00289
493.88642 1.42788 1929.62852
496.48899 1.16376 1939.17312
497.47743 1.46202 1905.48522
349.16601 1.0 450.42852
"""
data=data.split("\n")
testcases=int(data[0])
sol=[]
for i in xrange(1,testcases+1):
    print i
    f=[float(i) for i in data[i].split(" ")]
    #print f
    c,f,x=f[0],f[1],f[2]
    time=0.0
    cookies=0
    crate=2
    while cookies<x:
        if cookies<c:
            time+=(c-cookies)/crate
            cookies+=c
        if (c/crate)+(x)/(crate+f)<(x)/crate:
            #time+=c/crate
            crate+=f
            cookies-=c
        else:
            time+=(x-cookies)/crate
            cookies+=x-cookies
    sol.append(time)
f=open('problem2cookies.txt','w')
p=1
for i in sol:
    x=round(i,7)
    f.write('Case #')
    f.write(str(p))
    f.write(': ')
    f.write(str(x))
    f.write('\n')
    p+=1
f.close()
