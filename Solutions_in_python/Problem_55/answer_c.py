from __future__ import division, with_statement
from itertools import *
from numpy import *
from collections import defaultdict

def main():
	lines = """50
4 6 4
1 4 2 1
100 10 1
1
5 5 10
2 4 2 3 4 2 1 2 1 3
1 1 1
1
100 2 2
1 2
1000 100 10
4 3 9 1 2 5 6 9 1 10
1 10 10
4 3 4 1 2 5 6 9 1 10
1 10 9
1 1 1 1 1 1 1 1 1
1000 10 9
1 1 1 1 1 1 1 1 1
934 9 10
8 8 8 8 8 8 8 8 8 8
734 3 10
1 2 3 3 2 1 1 2 3 1
345 19 10
10 10 10 10 10 10 10 10 10 10
765 10 10
10 1 10 1 10 1 10 1 10 1
1000 100 10
10 10 10 10 10 10 10 10 10 10
734 20 10
1 2 3 4 5 6 7 8 9 10
631 16 10
10 9 8 7 6 5 4 3 2 1
2 11 9
2 8 1 7 10 4 3 5 5
3 7 6
7 4 4 7 2 2
3 14 6
10 1 3 4 9 4
4 13 9
10 10 9 10 8 9 5 2 3
538 13 9
5 6 6 7 4 4 1 3 3
889 9 10
7 1 5 5 2 5 9 2 5 1
69 8 9
4 1 3 8 2 7 1 7 2
914 11 9
8 1 8 7 5 5 10 5 10
7 23 10
6 2 10 5 3 4 9 6 8 10
8 22 10
7 6 6 4 2 10 3 2 9 1
8 22 10
5 3 1 8 8 7 1 7 1 3
9 20 10
10 10 8 2 4 7 7 1 10 10
39 13 8
8 5 9 5 6 5 9 6
174 11 9
9 8 6 8 7 7 7 6 8
214 20 10
7 8 8 6 8 8 6 6 6 6
152 13 10
7 8 6 6 9 7 7 9 9 5
239 16 9
7 6 5 7 5 8 8 8 6
596 28 10
7 6 9 6 5 9 8 5 7 6
316 64 9
6 8 5 5 6 9 7 8 6
212 10 9
5 5 6 8 9 9 7 5 5
558 82 10
6 7 8 9 9 5 7 7 8 9
100 73 5
8 7 6 5 7
372 88 7
9 5 6 8 7 9 5
963 12 9
5 6 7 9 7 9 8 6 5
983 81 7
7 8 9 9 6 8 7
869 91 6
6 9 6 5 5 8
34 79 7
8 9 7 5 8 6 8
660 82 8
6 5 5 7 6 6 8 9
241 49 7
6 6 8 9 7 8 8
861 27 5
5 8 9 7 6
292 67 8
9 9 9 7 6 6 8 8
317 56 8
5 9 7 6 7 6 5 7
552 13 5
9 8 8 8 5
413 82 8
7 8 9 6 5 6 5 8
""".strip().split("\n")
	lines.reverse()
	output = []
	num_tests = int(lines.pop())
	for test in range(1, num_tests+1):
		print "test", test
		R, k, N = map(int, lines.pop().split())
		print "runs", R, "run_size", k
		groups_waiting = map(int, lines.pop().split())
		print "groups_waiting", groups_waiting
		assert len(groups_waiting) == N
		groups_on_ride = []
		income = 0
		for r in range(R):
			while 1:
				if not groups_waiting:
					break
				if k < sum(groups_on_ride) + groups_waiting[0]:
					break
				groups_on_ride.append(groups_waiting.pop(0))
			income += sum(groups_on_ride)
			print "R", r, groups_on_ride, groups_waiting, income
			# move to back
			groups_waiting += groups_on_ride
			groups_on_ride = []
		print "income", income

		output.append("Case #%d: %s" % (test, income))

		print

	with file("C-small-out.txt", "w") as f:
		s = "\n".join(output)
		f.write(s)
		print s

if __name__ == "__main__":
	#~ main_a()
	main()
