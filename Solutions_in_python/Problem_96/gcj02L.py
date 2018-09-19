class Googler:
    growable=False
    maxscore=0
    def __init__(self,score):
        if(score % 3 == 0):
            self.maxscore = score /3
        else:
            self.maxscore = score /3 + 1
        
        if(score % 3 == 1):
            self.growable = False
        else:
            self.growable = True

        if(score == 0):
            self.growable = False
    def growedscore(self):
        if(self.growable):
            return self.maxscore + 1
        else:
            return self.maxscore

class GooglerTest:
    def Test(self,st):
        lines = st.splitlines()
        maxtest = int(lines[0])

        for i in range(1,maxtest+1):
            print("Case #" + str(i) + ": " + str(self.Solve(lines[i])))
            
    def Solve(self,st):
        words = st.split()
        googlersnum = int(words[0])
        supnum = int(words[1])
        minscore = int(words[2])
        
        googlers = [Googler(int(words[n+3])) for n in range(googlersnum)]
        #print str([g.maxscore for g in googlers]) + str(minscore) + ":" + str(supnum) 
        #for g in googlers:
        #    print g.maxscore
        res = [g.maxscore for g in googlers if g.maxscore >= minscore]
        res2 = [g.maxscore for g in googlers if (g.maxscore + 1 == minscore) and g.growable]
        return len(res) + min(len(res2), supnum)
gt = GooglerTest()
gt.Test("""100
6 2 8 29 20 8 18 18 21
17 1 5 26 27 11 12 27 23 11 12 24 20 12 5 12 12 16 11 12
79 12 6 29 16 14 24 13 8 26 15 3 14 14 15 15 9 14 15 15 21 2 30 16 8 15 13 14 6 30 10 14 18 14 15 21 14 14 29 14 7 15 14 6 29 4 14 11 14 14 14 15 8 15 15 15 22 15 11 15 14 15 2 14 14 15 15 15 15 3 14 17 15 26 15 15 22 6 14 15 14 14
97 41 6 14 15 20 14 15 9 14 15 15 14 14 0 23 15 14 14 15 8 8 15 1 7 2 15 1 15 10 14 1 2 15 19 30 3 14 15 23 10 15 14 14 15 9 14 15 15 9 15 6 10 14 14 9 14 14 20 25 15 23 13 8 14 19 14 14 5 7 14 8 14 15 30 14 14 23 3 4 15 16 9 15 15 14 5 14 25 15 15 0 15 24 14 2 26 14 4 25
81 0 2 20 25 5 29 4 30 27 27 16 12 26 30 17 26 8 0 1 6 28 16 28 2 13 11 8 7 0 7 14 27 8 18 25 25 8 22 20 11 13 0 5 5 15 11 18 23 15 24 0 0 9 26 21 19 5 28 10 6 22 19 17 24 20 23 9 10 11 19 15 29 24 23 8 20 16 29 28 25 25 11 12
31 31 3 21 13 20 8 6 20 11 10 20 25 28 8 17 20 9 23 8 4 26 12 19 25 18 18 15 9 18 8 14 25 27
84 44 7 29 19 30 29 7 27 7 17 13 3 24 10 23 17 29 19 18 14 21 8 28 5 23 4 26 6 4 21 19 20 20 16 1 1 20 25 26 2 28 26 18 7 14 3 5 27 4 20 10 15 28 29 17 2 4 5 8 18 22 19 7 6 1 21 22 6 23 12 14 18 16 7 4 11 4 27 4 25 7 0 21 8 10 20
97 21 7 10 17 20 17 17 18 18 4 23 12 18 18 17 3 17 14 18 17 23 24 23 17 18 27 18 17 18 17 24 29 26 17 17 0 17 17 17 17 24 18 17 3 7 18 17 17 18 16 17 18 17 9 4 18 18 27 17 13 18 13 6 17 18 18 26 26 17 18 23 18 17 7 18 18 17 0 21 24 18 29 26 24 18 18 17 22 18 11 5 3 18 12 18 29 22 12 18
70 26 7 17 18 29 18 6 18 17 17 18 18 12 17 17 18 11 11 18 18 20 17 18 28 9 18 18 28 9 18 18 18 17 18 17 17 10 18 5 3 7 18 28 25 21 18 18 18 16 18 17 18 4 17 18 17 5 17 18 17 18 12 18 17 9 17 17 9 18 20 15 17
90 0 2 25 16 6 1 24 27 16 14 28 19 9 8 10 19 5 28 27 0 20 21 28 27 19 23 19 30 20 28 17 17 29 13 14 30 0 7 10 25 18 11 4 11 1 6 21 26 25 1 16 4 8 10 7 12 11 16 25 11 6 5 17 4 25 9 14 17 17 24 9 10 15 23 6 29 6 28 0 18 26 14 17 12 15 17 30 25 13 13 10 28
91 75 8 5 2 1 23 29 9 0 24 25 7 20 22 7 0 23 6 29 3 8 16 11 2 9 19 13 22 4 19 4 3 11 18 18 25 9 2 5 26 20 17 21 8 4 13 7 16 13 1 14 4 28 17 1 17 29 28 27 13 12 4 3 11 14 20 18 13 10 5 11 25 20 10 29 8 30 27 12 26 27 20 29 0 3 5 29 21 10 10 26 15 26
56 4 10 7 13 30 22 22 25 17 20 24 28 10 22 16 21 25 17 19 30 14 3 15 0 27 17 16 1 28 24 16 19 1 10 4 5 24 7 3 19 13 5 0 23 22 11 13 20 20 12 8 6 8 10 13 19 28 18
43 13 2 2 30 15 2 3 17 14 3 16 2 4 15 2 12 2 3 2 3 26 10 3 11 2 2 22 29 2 12 2 29 3 21 29 9 2 4 2 3 21 2 3 2 2
41 0 3 15 11 10 10 16 26 16 11 13 0 13 11 16 14 25 27 15 10 20 23 8 29 30 8 23 24 9 27 0 19 19 26 8 27 3 4 26 16 27 0 12
64 38 1 30 13 28 21 24 4 13 4 26 8 16 22 6 21 26 17 9 24 3 26 10 23 15 28 18 24 21 10 16 7 19 14 21 3 28 6 5 9 14 26 12 9 15 10 11 8 22 20 4 30 24 8 19 29 2 26 20 19 28 0 3 19 11 2
15 2 8 20 20 12 5 15 28 21 7 20 17 29 28 9 21 22
88 66 6 18 2 30 22 12 16 30 4 10 29 19 11 30 20 1 20 26 7 24 3 19 17 22 1 14 22 5 7 15 4 19 28 14 20 14 13 21 5 27 9 16 1 7 18 0 28 0 0 7 21 6 21 19 15 25 29 18 28 9 20 8 11 9 28 5 17 20 10 8 14 20 7 17 20 15 25 11 28 25 2 29 17 14 14 23 7 12 5
15 8 2 2 2 2 25 3 2 2 2 2 2 2 3 3 3 2
6 0 8 14 18 21 20 14 13
26 0 10 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
67 28 8 21 21 21 20 21 21 2 21 21 20 0 20 9 21 14 0 20 20 21 21 21 21 20 20 21 5 21 20 20 14 17 25 21 21 20 2 14 21 20 19 0 21 9 20 20 20 20 16 21 12 21 20 21 2 18 0 20 20 20 17 21 20 20 21 20 17 6
29 5 5 3 11 11 11 1 9 11 26 12 10 30 12 11 11 2 12 13 11 11 14 27 12 8 13 11 20 12 12 3
43 20 3 23 5 19 18 28 5 6 11 24 5 6 5 5 5 5 6 6 5 6 5 3 5 25 4 14 8 5 27 6 11 6 29 6 20 27 11 6 12 28 25 6 6 5
22 6 10 8 26 14 26 30 27 27 16 10 11 12 26 1 7 16 7 10 29 26 9 2 26
81 81 7 23 26 28 19 26 26 5 8 15 25 2 5 8 15 10 23 7 7 12 2 5 6 13 22 10 28 24 5 26 12 23 11 8 23 13 7 22 17 16 19 25 23 17 12 21 4 22 28 14 22 5 8 13 18 17 19 4 5 20 3 22 9 4 26 8 8 8 12 12 4 13 19 27 12 24 27 2 19 3 15 13
83 11 9 20 11 18 2 2 26 9 15 28 21 5 12 19 1 10 19 2 17 22 0 28 1 11 26 25 14 2 27 28 3 7 30 9 10 4 25 10 27 6 4 0 23 1 16 2 8 27 6 6 1 8 18 22 23 17 4 12 17 25 20 1 13 23 21 27 26 16 9 18 14 3 6 29 11 8 23 7 23 14 29 8 17 26
35 0 9 9 28 8 5 3 19 22 11 3 28 12 23 7 8 14 8 7 3 6 28 6 14 15 18 7 3 0 24 8 12 10 23 24 28 2
1 1 9 19
43 13 5 8 2 2 29 26 19 9 4 25 28 1 18 12 13 24 14 10 17 25 25 7 13 30 8 18 12 9 22 21 1 18 17 26 24 6 21 28 20 2 16 30 16 29
66 19 2 3 25 3 4 2 16 16 3 2 8 11 27 2 2 22 2 3 2 3 2 25 6 2 2 2 2 2 2 2 2 27 24 3 3 18 26 4 3 6 2 3 28 21 26 0 14 10 2 3 22 28 3 5 3 3 7 8 2 3 2 18 2 2 2 2 16
97 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
90 14 9 13 1 29 27 9 28 24 0 30 0 10 22 21 3 6 30 7 9 16 12 12 21 4 7 27 14 0 1 8 20 29 12 27 14 24 1 0 1 21 14 21 15 30 25 22 3 12 6 13 25 15 4 5 7 23 18 18 9 18 1 29 23 15 24 15 8 27 19 26 0 30 6 9 27 23 13 18 12 17 6 9 25 22 11 7 3 11 12 21 4
45 25 9 10 0 3 21 26 19 20 27 15 3 12 14 6 25 3 21 6 0 10 8 14 12 4 16 14 3 17 30 27 12 18 4 22 19 17 0 19 12 27 17 4 27 29 16 27
18 0 1 17 17 12 7 16 22 20 11 22 30 5 16 7 29 14 19 4 18
74 5 8 30 11 2 20 24 28 20 23 9 23 14 14 12 11 25 2 25 25 4 16 2 4 18 26 14 14 12 19 17 16 13 4 7 28 22 21 28 18 0 5 7 13 17 6 17 24 3 23 21 24 23 9 17 14 23 10 13 29 0 6 8 9 4 22 22 11 12 20 12 17 2 3 20 30
23 19 1 19 28 28 25 28 17 9 2 12 22 16 20 4 15 18 12 25 6 4 0 9 10 21
69 9 3 12 15 5 5 20 5 15 21 15 5 6 27 5 5 16 10 6 18 6 30 6 23 6 6 14 6 6 5 0 27 5 19 6 5 15 6 28 5 2 14 5 5 6 5 19 15 2 20 5 5 6 2 16 22 23 10 5 5 27 18 6 19 1 27 6 9 7 5 18
18 0 6 15 25 22 28 9 15 30 14 2 13 30 14 15 14 15 2 11 14
45 7 10 2 15 27 27 27 30 25 20 9 27 6 27 24 21 27 27 11 26 27 25 27 11 27 26 7 16 26 26 26 26 27 26 26 26 26 27 26 25 13 27 22 14 26 8 18
2 0 9 23 5
74 74 2 21 2 8 27 27 3 8 19 15 25 19 15 22 4 23 27 19 21 10 3 26 20 13 25 16 24 5 14 4 22 14 28 23 22 4 10 9 7 7 5 16 6 3 13 28 20 3 11 27 9 25 21 17 21 14 20 7 11 15 15 7 21 7 3 25 20 24 28 12 19 11 8 27 2
32 23 5 21 6 11 11 16 22 26 14 12 14 7 21 16 14 18 27 0 11 17 13 26 16 3 28 13 30 1 3 7 16 29 21
56 56 0 23 13 27 11 8 20 8 15 28 21 26 26 12 7 9 8 7 5 27 19 28 3 20 28 22 27 28 11 2 24 25 12 27 24 25 24 23 5 25 8 21 18 27 16 3 6 17 7 8 25 7 2 6 19 27 25
33 33 7 6 8 6 22 17 7 15 25 12 22 11 27 11 18 7 6 26 2 5 23 15 28 23 11 4 12 7 28 7 28 19 4 14
60 50 2 26 14 20 2 0 17 22 4 4 16 14 29 1 2 20 29 17 26 20 19 23 6 0 18 11 29 13 10 21 14 11 19 9 14 23 9 14 30 0 9 0 11 11 10 4 15 9 27 18 7 27 10 19 19 7 29 13 5 26 28
74 2 5 11 21 3 12 11 16 26 1 15 7 15 11 11 12 8 6 26 11 12 11 11 11 26 24 14 19 12 16 16 4 12 12 11 11 19 26 6 17 25 29 30 12 11 8 11 11 12 11 12 11 11 21 24 19 11 22 11 11 12 11 1 24 12 11 12 16 12 12 10 30 25 12 21 4
77 41 9 25 13 27 29 22 7 30 7 0 16 12 1 28 9 9 2 28 1 8 28 27 0 3 11 4 16 23 20 13 8 30 19 17 22 27 7 30 0 2 22 4 13 29 28 21 21 24 25 29 5 30 30 3 11 15 2 6 17 27 23 22 12 7 3 5 3 13 2 22 29 26 5 28 12 9 19 26
18 0 7 23 20 27 26 10 30 7 10 2 5 20 7 23 8 27 18 10 25
43 0 3 8 5 13 6 5 5 22 11 6 11 8 9 1 6 28 5 5 5 21 30 6 5 17 6 6 14 5 5 6 6 4 2 11 3 5 5 6 6 5 6 6 6 18
25 17 0 22 2 19 4 12 25 29 30 4 26 19 20 1 10 10 10 15 8 0 17 3 28 30 29 27
71 9 3 5 29 5 6 8 10 6 5 6 7 25 5 6 6 30 5 6 10 11 5 6 20 8 5 13 5 6 15 5 5 6 2 6 6 22 5 6 14 6 6 15 6 10 5 10 6 5 5 5 5 5 5 5 6 4 27 6 26 5 6 6 5 6 17 5 10 6 5 1 5 5
40 16 8 11 30 27 1 28 30 20 19 4 10 17 22 9 1 4 1 20 8 21 13 22 21 28 29 16 1 7 10 22 28 9 20 24 24 22 5 23 10 21 5
51 51 8 27 12 18 20 10 6 10 21 25 4 5 16 8 19 22 10 5 20 13 16 2 28 4 7 15 19 27 3 25 20 27 12 7 14 18 14 26 24 20 28 27 13 27 18 21 20 28 7 5 19 8
24 0 4 8 26 9 25 12 8 23 8 4 9 6 21 25 25 9 9 8 9 9 8 9 9 9 18
3 1 9 7 30 7
71 56 0 1 22 0 20 14 5 17 15 29 24 24 0 7 11 1 3 28 28 21 29 14 28 11 18 22 0 21 8 6 15 30 28 2 9 12 18 3 22 7 6 10 3 8 4 20 26 4 3 22 27 4 12 21 9 22 3 24 12 8 10 14 0 29 2 30 1 19 27 29 12 5
72 29 8 21 25 21 16 30 21 21 20 12 20 21 17 20 21 13 16 13 20 21 20 20 20 7 19 20 20 21 20 21 17 20 28 21 28 20 29 20 21 16 20 25 20 20 25 20 20 7 21 23 18 20 21 21 12 20 20 14 9 18 21 17 20 6 19 9 3 28 20 19 20 9 21
37 6 10 27 11 27 15 13 19 27 9 26 28 26 26 4 26 27 26 22 27 28 25 26 7 27 26 26 27 26 27 20 25 27 7 26 27 19 18 27
31 14 7 17 17 24 17 18 18 18 22 21 16 24 17 18 18 29 14 16 20 18 18 18 18 17 5 30 18 18 18 18 18 0
38 0 10 24 14 2 30 7 28 1 25 15 24 5 10 11 11 26 18 10 29 2 28 26 23 12 25 5 12 24 27 18 1 21 13 11 18 7 1 27 29
54 10 1 2 27 28 19 11 16 30 29 10 0 3 4 11 15 18 18 7 2 9 3 14 20 29 6 15 16 18 11 24 5 12 13 26 20 13 6 11 11 19 14 14 16 27 13 13 1 13 6 18 19 4 2 15 21
28 8 3 6 24 5 5 6 5 6 5 18 5 25 5 6 6 5 5 6 5 3 6 5 22 5 26 2 5 6 15
77 6 0 0 6 6 7 16 5 26 25 5 23 29 14 0 5 1 12 0 5 12 27 26 11 18 19 24 18 9 21 22 26 1 29 15 1 12 5 24 9 9 8 29 16 15 23 17 19 25 18 10 20 19 26 0 5 5 8 4 22 30 29 15 24 23 26 25 9 21 11 27 27 17 18 14 23 22 18 27
100 79 4 1 30 18 14 30 8 12 19 10 22 6 21 24 13 16 1 23 1 10 1 3 1 5 21 2 2 7 19 26 4 7 8 27 6 21 22 6 9 14 24 5 3 7 27 25 27 2 23 11 21 7 4 12 21 29 25 29 24 20 16 6 0 30 20 19 11 22 14 9 19 14 26 18 20 13 21 15 27 12 4 5 17 16 9 25 8 1 14 21 3 15 20 1 12 28 14 2 0 4 0
100 14 5 11 11 20 20 28 14 11 11 12 4 12 28 12 11 15 20 11 12 12 11 17 12 24 12 12 12 11 12 17 12 2 11 11 20 11 18 4 12 12 13 22 28 11 11 11 8 11 11 11 11 28 11 11 12 12 30 23 17 5 26 19 3 25 19 2 8 11 11 7 12 9 7 0 3 12 14 20 12 11 12 11 17 28 9 11 11 16 5 12 12 12 5 11 12 11 12 12 12 12 13
97 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
45 11 3 24 4 0 15 5 26 9 24 3 4 18 10 4 11 25 8 5 0 21 17 5 22 12 4 2 19 30 9 24 27 25 3 17 7 14 29 8 16 27 28 14 19 13 9 7
21 10 6 14 15 30 15 6 15 14 20 15 15 26 3 14 4 14 23 14 22 9 15 14
84 53 8 2 26 9 17 13 10 30 27 12 26 28 3 18 9 21 4 20 7 18 9 1 25 18 28 29 13 20 30 30 26 29 16 26 23 0 12 4 2 1 16 28 27 26 2 12 1 20 7 29 9 16 22 29 13 17 2 10 2 18 24 27 29 15 28 23 5 24 17 25 29 27 15 1 8 5 0 1 23 24 29 22 25 16 28
55 2 9 30 27 26 10 8 27 6 26 22 1 30 4 17 6 25 3 24 8 27 3 28 14 11 7 5 2 28 3 17 7 2 6 21 30 6 28 0 7 0 10 23 22 3 2 20 6 22 5 17 3 3 0 5 28 28
67 46 5 19 22 25 23 20 28 4 22 0 25 21 10 16 10 2 24 16 7 3 11 30 1 5 21 2 21 11 0 18 26 2 3 8 23 23 22 15 24 6 24 7 26 26 30 22 19 21 3 20 30 6 22 4 1 20 28 27 29 2 18 12 26 7 7 18 29 24
88 88 7 18 27 6 7 25 19 17 2 14 6 21 24 23 6 17 22 24 20 21 21 28 5 16 11 15 25 4 23 6 8 10 2 8 13 25 14 15 3 12 23 11 12 27 3 28 3 3 20 10 10 24 19 9 5 7 23 24 14 26 9 21 12 8 2 17 4 13 18 24 8 5 21 13 16 14 4 27 20 23 12 13 11 7 16 20 17 25 24
100 69 2 30 26 23 30 1 19 15 21 2 27 26 6 14 12 15 23 12 19 25 22 4 25 1 2 18 26 12 16 15 18 27 27 23 6 12 27 27 30 7 19 7 29 27 11 8 1 23 20 15 1 24 12 22 28 0 21 23 14 23 5 26 22 14 11 7 10 5 14 4 3 20 10 6 14 4 26 9 2 4 18 20 24 24 25 15 24 10 30 7 16 4 20 16 2 2 10 6 28 15 15
7 0 8 9 0 30 5 0 17 26
20 2 3 30 2 24 6 5 6 6 6 6 20 6 13 5 5 30 5 6 15 6 23
64 24 6 14 19 9 15 15 4 14 14 15 14 18 15 2 14 11 18 16 15 30 27 8 26 14 15 15 18 14 14 14 14 14 15 29 15 25 2 15 11 17 15 14 14 5 15 26 15 24 10 14 21 14 6 15 14 15 14 3 15 2 14 14 15 10 14
13 0 5 17 10 11 3 17 17 14 18 11 7 12 20 16
68 0 0 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30 30
38 38 9 6 16 6 19 18 12 21 25 17 21 25 6 17 24 2 4 25 19 26 22 9 24 18 13 22 21 14 27 5 2 25 28 2 20 26 28 9 11
38 17 1 19 6 9 29 13 15 3 17 7 22 0 2 28 23 11 16 25 26 4 26 29 13 15 17 20 23 3 3 18 12 17 3 12 6 7 0 18 6
2 0 5 1 14
93 40 9 23 11 23 3 9 23 24 24 6 23 2 24 6 24 4 25 0 16 0 24 4 7 5 23 23 16 24 18 16 23 24 24 14 13 11 24 21 24 8 23 24 15 24 23 29 12 23 18 14 30 6 15 28 24 23 23 23 18 24 23 11 23 23 24 2 24 23 2 23 24 24 24 23 27 19 23 28 16 23 30 23 0 0 18 23 30 24 23 24 24 24 13 15
13 12 1 5 15 13 16 20 0 22 13 23 22 4 6 28
41 11 6 1 15 15 14 29 25 14 14 24 15 23 14 14 22 15 15 14 12 14 14 14 15 15 23 23 26 14 6 14 19 1 2 15 20 12 15 20 14 14 6 14
21 8 3 9 6 25 29 19 25 1 4 24 1 29 18 27 29 15 4 28 18 5 0 22
39 39 0 4 18 19 6 19 25 26 6 4 6 27 19 18 17 27 17 18 25 19 21 15 11 26 4 25 27 17 19 25 15 12 16 19 24 17 13 18 3 26
68 2 10 27 29 21 27 26 26 11 24 21 26 0 9 28 26 27 26 1 27 13 12 26 26 27 29 26 27 27 3 27 26 26 4 16 19 21 2 27 16 4 26 26 16 27 20 26 10 5 27 28 6 26 24 27 12 0 26 23 22 17 27 27 26 27 28 27 26 29 26
12 12 5 11 3 16 24 6 19 11 18 19 2 24 7
27 12 3 6 5 5 27 7 29 6 6 18 29 5 4 30 5 6 9 6 17 5 13 0 5 6 19 5 9 28
92 29 2 3 15 15 24 26 17 8 21 21 18 28 0 12 30 19 14 3 20 18 10 13 24 12 27 13 30 27 25 18 9 5 3 20 6 18 19 22 26 7 26 8 26 5 2 10 3 23 2 16 25 6 24 6 9 7 24 30 19 19 28 21 20 27 7 5 27 3 0 17 11 30 20 18 25 11 11 30 25 20 2 14 19 5 2 17 12 3 25 13 0 8 7
62 30 6 6 1 15 3 0 22 5 12 10 18 22 22 1 7 2 9 23 19 0 25 10 8 9 7 25 24 20 29 1 13 20 30 21 11 16 10 15 24 27 16 28 3 9 19 0 0 9 29 7 30 18 14 2 10 15 13 8 17 24 15 4 26
2 1 6 15 14
47 47 10 20 6 11 9 17 4 12 5 20 4 22 24 15 17 25 6 11 8 23 27 15 15 18 7 16 25 10 17 4 11 23 27 10 11 26 21 28 16 27 5 27 24 26 20 4 9 20
30 1 9 24 12 18 23 24 21 24 30 20 22 23 1 24 4 23 19 26 24 24 7 12 12 24 24 26 23 0 19 18 9
73 10 4 2 6 9 9 11 8 9 9 9 9 9 9 8 2 8 8 8 9 25 9 6 24 3 8 12 8 9 9 9 8 6 9 5 29 29 29 24 18 8 28 11 8 9 22 26 8 20 24 23 11 19 8 5 9 9 8 13 3 9 8 8 8 10 8 9 9 23 10 12 9 8 21 23
56 7 7 1 1 16 2 14 0 28 3 4 5 6 1 3 11 25 21 26 9 19 24 3 29 4 3 1 21 20 21 20 4 6 21 24 24 29 11 27 15 13 27 7 27 19 6 18 26 24 7 13 0 10 27 15 16 13 13
21 4 4 16 20 8 0 9 8 9 19 10 24 22 6 9 21 11 28 21 8 8 20 2
74 74 4 7 8 3 14 25 13 15 4 23 21 22 11 15 27 16 9 16 3 23 14 11 25 21 14 3 23 19 11 9 15 24 18 2 12 17 17 28 28 11 2 27 5 20 16 13 23 22 10 10 16 9 11 7 9 26 17 18 27 4 21 10 17 10 6 22 8 27 10 2 2 20 27 19 2
89 0 3 17 25 2 15 8 27 22 5 5 19 8 28 5 14 27 18 23 26 21 8 15 12 19 14 5 30 1 14 8 29 16 25 26 27 29 28 18 19 20 5 19 3 28 0 30 13 13 21 21 19 23 26 17 6 10 13 22 25 15 1 14 0 26 26 5 20 30 8 29 13 6 25 8 15 28 23 3 3 25 1 23 2 4 30 1 16 29 30 18
12 12 10 21 13 22 11 7 17 16 19 9 28 16 15
""")
