data = '''55
1 4 2
1 7 7
1 6 5
1 7 5
1 6 3
1 6 6
1 7 2
1 5 1
1 8 8
1 10 8
1 8 2
1 7 4
1 5 4
1 8 7
1 9 5
1 6 4
1 9 1
1 1 1
1 10 6
1 9 2
1 8 1
1 3 2
1 4 3
1 7 6
1 8 6
1 2 1
1 8 4
1 7 3
1 9 9
1 10 4
1 8 5
1 10 2
1 6 1
1 9 8
1 4 4
1 10 3
1 9 3
1 10 1
1 5 3
1 9 4
1 10 10
1 7 1
1 9 6
1 10 5
1 8 3
1 9 7
1 2 2
1 6 2
1 3 3
1 5 2
1 10 7
1 3 1
1 4 1
1 10 9
1 5 5'''

data = [x for x in data.split('\n') if x]

case_count,data = data[0],data[1:]
for case in range(int(case_count)):
	r,c,ship = map(int,data.pop(0).split())
	inc = 0 if not c%ship else 1
	result = 'Case #{0}: {1}'.format(case+1,(c/ship+inc)*r+ship-1)
	print result