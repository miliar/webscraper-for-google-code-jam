#!/usr/bin/env python

def solve(x, r, c):
	if x == 1:
		return "GABRIEL"
	if x == 2:
		if ((r * c) % 2) == 1:
			return "RICHARD"
		else:
			return "GABRIEL"
	if x == 3:
		if ((r * c) % 3) != 0 or (r * c) == 3:
			return "RICHARD"
		else:
			return "GABRIEL"
	if x == 4:
		if ((r * c) % 4) != 0 or (r * c) == 4 or (r * c) == 8:
			return "RICHARD"
		else:
			return "GABRIEL"

N = int(raw_input())
for i in range(N):
	(x, r, c) = map(int, raw_input().split())
	print 'Case #' + str(i+1) + ": " + solve(x, r, c)
