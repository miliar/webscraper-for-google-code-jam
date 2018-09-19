# -*- coding: utf-8 -*-
'''
Problem D. Deceitful War

Small input
14 points

Large input
16 points

Problem

Naomi and Ken sometimes play games together. Before they play, each of
them gets N identical-looking blocks of wood with masses between 0.0kg
and 1.0kg (exclusive). All of the blocks have different weights. There
are lots of games they could play with those blocks, but they usually
play something they call War. Here is how War works:

Each player weighs each of his or her own blocks, so each player knows
the weights of all of his or her own blocks, but not the weights of
the other player's blocks.

They repeat the following process N times:

Naomi chooses one of her own blocks, with mass ChosenNaomi.

Naomi tells Ken the mass of the block she chose.

Ken chooses one of his own blocks, with mass ChosenKen.

They each put their block on one side of a balance scale, and the
person whose block is heavier gets one point.

Both blocks are destroyed in a fire.

Naomi has realized three things about War. First, she has realized
that she loses a lot. Second, she has realized that there is a unique
strategy that Ken can follow to maximize his points without assuming
anything about Naomi's strategy, and that Ken always uses it. Third,
she has realized that she hates to lose. Naomi has decided that
instead of playing War, she will play a game she calls Deceitful War.
The great thing about Deceitful War is that Ken will think they're
playing War!

Here is how Deceitful War works, with differences between Deceitful
War and War in bold:

Each player weighs each of his or her own blocks. NAOMI ALSO WEIGHS
KEN'S BLOCKS WHILE HE ISN'T LOOKING, SO NAOMI KNOWS THE WEIGHTS OF
ALL BLOCKS and Ken only knows the weights of his own blocks.

They repeat the following process N times:

Naomi chooses one of her own blocks, with mass ChosenNaomi.

Naomi tells Ken A NUMBER, ToldNaomi, BETWEEN 0.0kg AND 1.0kg
EXCLUSIVE. Ken, who thinks they're playing War, thinks the number
Naomi just told him is ChosenNaomi.

Ken chooses one of his own blocks, with mass ChosenKen.

They each put their block on one side of a balance scale, and the
person whose block is heavier gets one point.

Both blocks are destroyed in a fire.

Naomi doesn't want Ken to know that she isn't playing War; so when she
is choosing which block to play, and what mass to tell Ken, she must
make sure that the balance scale won't reveal that
ChosenNaomi != ToldNaomi. In other words, she must make decisions so
that:

ChosenNaomi > ChosenKen if, and only if, ToldNaomi > ChosenKen, and

ToldNaomi is not equal to the mass of any of Ken's blocks, because he
knows that isn't possible.

It might seem like Naomi won't win any extra points by being
deceitful, because Ken might discover that she wasn't playing War; but
Naomi knows Ken thinks both players are playing War, and she knows
what he knows, and she knows Ken will always follow his unique optimal
strategy for War, so she can always predict what he will play.

You'll be given the masses of the blocks Naomi and Ken started with.
Naomi will play Deceitful War optimally to gain the maximum number of
points. Ken will play War optimally to gain the maximum number of
points assuming that both players are playing War. What will Naomi's
score be? What would it have been if she had played War optimally
instead?

Examples

If each player has a single block left, where Naomi has 0.5kg and Ken
has 0.6kg, then Ken is guaranteed to score the point. Naomi can't say
her number is >= 0.6kg, or Ken will know she isn't playing War when
the balance scale shows his block was heavier.

If each player has two blocks left, where Naomi has [0.7kg, 0.2kg] and
Ken has [0.8kg, 0.3kg], then Naomi could choose her 0.2kg block, and
deceive Ken by telling him that she chose a block that was 0.6kg. Ken
assumes Naomi is telling the truth (as in how the War game works) and
will play his 0.8kg block to score a point. Ken was just deceived, but
he will never realize it because the balance scale shows that his
0.8kg block is, like he expected, heavier than the block Naomi played.
Now Naomi can play her 0.7kg block, tell Ken it is 0.7kg, and score a
point. If Naomi had played War instead of Deceitful War, then Ken
would have scored two points and Naomi would have scored zero.

Input

The first line of the input gives the number of test cases, T. T test
cases follow. Each test case starts with a line containing a single
integer N, the number of blocks each player has. Next follows a line
containing N space-separated real numbers: the masses of Naomi's
blocks, in kg. Finally there will be a line containing N
space-separated real numbers: the masses of Ken's blocks, in kg.

Each of the masses given to Ken and Naomi will be represented as a 0,
followed by a decimal point, followed by 1-5 digits. Even though all
the numbers in the input have 1-5 digits after the decimal point, Ken
and Naomi don't know that; so Naomi can still tell Ken that she played
a block with mass 0.5000001kg, and Ken has no reason not to believe
her.

Output

For each test case, output one line containing "Case #x: y z", where
x is the test case number (starting from 1), y is the number of points
Naomi will score if she plays Deceitful War optimally, and z is the
number of points Naomi will score if she plays War optimally.

Limits

1 <= T <= 50.
All the masses given to Ken and Naomi are distinct, and between
0.0 and 1.0 exclusive.

Small dataset

1 <= N <= 10.

Large dataset

1 <= N <= 1000.

Sample

Input

4
1
0.5
0.6
2
0.7 0.2
0.8 0.3
3
0.5 0.1 0.9
0.6 0.4 0.3
9
0.186 0.389 0.907 0.832 0.959 0.557 0.300 0.992 0.899
0.916 0.728 0.271 0.520 0.700 0.521 0.215 0.341 0.458

Output

Case #1: 0 0
Case #2: 1 0
Case #3: 2 1
Case #4: 8 4
'''

from collections import deque
#from decimal import Decimal
from sys import stdin, stderr
import copy
import fractions
import heapq
import itertools
import math
#import networkx as nx
import random
import re
import sys

sys.setrecursionlimit(100)

isa = isinstance
INF = 1 << 66

def solve_honest(A,B):
    A = sorted(A,reverse=True)
    B = sorted(B,reverse=True)
    D = dict()
    D[0,0] =0
    def next_one(i,j):
        yield (i+1,j),D[i,j]
        if A[i] < B[j]:
            yield (i+1,j+1),D[i,j]+1
    n = len(A)
    for _ in range(n):
        T = dict()
        for i,j in D:
            for k,v in next_one(i,j):
                if k in T:
                    T[k] = max(T[k],v)
                else:
                    T[k] = v
        D = T
    ans = 0
    for k in D:
        ans = max(ans,D[k])
    return ans
def solve_deceitful(A,B):
    A = sorted(A)
    B = sorted(B)
    n = len(A)
    D = dict()
    D[(),0] = 0
    def next_one(mask,j):
        used = set(mask)
        can_cheat = False
        for i in range(n):
            if i not in used and A[i] > B[j]:
                can_cheat = True
                break
        if can_cheat:
            # We can lie to a huge value that make Ken think he cannot
            # win this one, so that he will pick his smallest one to
            # lose.
            used.add(i)
            m = tuple(sorted(used))
            yield (m,j+1),D[mask,j]
        else:
            for i in range(n):
                if i not in used:
                    break
            used.add(i)
            m = tuple(sorted(used))
            yield (m,j+1),D[mask,j]+1
    for x in range(n):
        T = dict()
        for mask,j in D:
            for k,v in next_one(mask,j):
                if k in T:
                    T[k] = max(T[k],v)
                else:
                    T[k] = v
        D = T
    ans = 0
    for k in D:
        ans = max(ans,D[k])
    return ans
def solve(A,B):
    n = len(A)
    h = solve_honest(A,B)
    d = solve_deceitful(A,B)
    return n-h,n-d

def check_test(A, B, data='', case=[0]):
    print
    print "test %d:" % case[0]
    print A
    print B
    # if abs(A-B) > 1e-9:
    if A != B:
        if data:
            print data
        print '>>>', A
        print '<<<', B
        print "!!!!!!!! FAIL !!!!!!!!"
    else:
        print ":::::::) OK"
        case[0] += 1

def unit_test():
    print
    A,B, ans = [0.5],[0.6],(0,0)
    check_test(ans, solve(A,B))

    # A,B, ans = (0.5,0.1,0.9),(0.6,0.4,0.3), (2,1)
    # check_test(ans, solve(A,B))

    # A,B, ans = (
    #     (0.186,0.389,0.907,0.832,0.959,0.557,0.300,0.992,0.899),
    #     (0.916,0.728,0.271,0.520,0.700,0.521,0.215,0.341,0.458),
    #     (8,4)
    # )
    # check_test(ans, solve(A,B))

def output():
    for case in xrange(1, int(stdin.next()) + 1):
        stdin.next()
        A = [float(i) for i in stdin.next().split()]
        B = [float(i) for i in stdin.next().split()]
        # print >>stderr, '--', case
        # if case in [1]:
        #     print >>stderr, A
        #     print >>stderr, B
        h,d = solve(A,B)
        print 'Case #%d:' % case, d,h

if __name__ == '__main__':
#    unit_test()
    output()
