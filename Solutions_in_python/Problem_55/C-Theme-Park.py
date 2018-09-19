#!/usr/bin/env python
# -*- coding: utf8 -*-

import sys

argc = len(sys.argv) - 1
if argc == 0:    pass
elif argc == 1:  sys.stdin = open(sys.argv[1])
else:            raise RuntimeError("too much args.")
	
def next_line(): return sys.stdin.next().strip()


"""
Theme Park
[http://code.google.com/codejam/contest/dashboard?c=433101#s=p2]

Problem

Roller coasters are so much fun! It seems like everybody who visits the theme 
park wants to ride the roller coaster. Some people go alone; other people go 
in groups, and don't want to board the roller coaster unless they can all go 
together. And everyone who rides the roller coaster wants to ride again. A 
ride costs 1 Euro per person; your job is to figure out how much money the 
roller coaster will make today.

The roller coaster can hold k people at once. People queue for it in groups. 
Groups board the roller coaster, one at a time, until there are no more groups 
left or there is no room for the next group; then the roller coaster goes, 
whether it's full or not. Once the ride is over, all of its passengers 
re-queue in the same order. The roller coaster will run R times in a day.

For example, suppose R=4, k=6, and there are four groups of people with sizes: 
1, 4, 2, 1. The first time the roller coaster goes, the first two groups 
[1, 4] will ride, leaving an empty seat (the group of 2 won't fit, and the 
group of 1 can't go ahead of them). Then they'll go to the back of the queue, 
which now looks like 2, 1, 1, 4. The second time, the coaster will hold 4 
people: [2, 1, 1]. Now the queue looks like 4, 2, 1, 1. The third time, it 
will hold 6 people: [4, 2]. Now the queue looks like [1, 1, 4, 2]. Finally, 
it will hold 6 people: [1, 1, 4]. The roller coaster has made a total of 21 
Euros!

Input

The first line of the input gives the number of test cases, T. T test cases 
follow, with each test case consisting of two lines. The first line contains 
three space-separated integers: R, k and N. The second line contains N 
space-separated integers g_i, each of which is the size of a group that wants 
to ride. g_0 is the size of the first group, g_1 is the size of the second 
group, etc.

Output

For each test case, output one line containing "Case #x: y", where x is the 
case number (starting from 1) and y is the number of Euros made by the roller 
coaster.

Limits

1 ≤ T ≤ 50.
g_i ≤ k.

Small dataset

1 ≤ R ≤ 1000.
1 ≤ k ≤ 100.
1 ≤ N ≤ 10.
1 ≤ g_i ≤ 10.

Large dataset

1 ≤ R ≤ 10^8.
1 ≤ k ≤ 10^9.
1 ≤ N ≤ 1000.
1 ≤ g_i ≤ 10^7.

Sample

Input
  	
3
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3

Output
 
Case #1: 21
Case #2: 100
Case #3: 20
"""

def euros(R, k, N, gs):
	assert len(gs) == N
	total = 0
	for trip in xrange(R):
		s = 0
		for i, g_i in enumerate(gs):
			s += g_i
			if s > k:
				s -= g_i
				break
		total += s
		gs = gs[i:] + gs[:i]
	return total

T = int(next_line())
for X in xrange(T):
	print "Case #%s:" % (X+1),
	R, k, N = [int(w) for w in next_line().split()]
	gs = [int(w) for w in next_line().split()]
	print euros(R, k, N, gs)
