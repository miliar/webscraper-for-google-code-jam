#!/usr/bin/python
# -*- coding: utf-8 -*-


def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input

    f = open('round1B1.out', 'w')

    lines = input_data.split('\n')
    num_of_cases = int(lines[0])
    lines = lines[1:]

    for i in range(num_of_cases):
        tmp = lines[i].split()
        A = int(tmp[0])
        B = int(tmp[1])
        K = int(tmp[2])

        count = 0
        for z in range(A):
            for j in range(B):
                if (z & j) < K:
                    count+=1

        f.write('Case #' + str(i+1) + ': ' + str(count) + '\n')

    f.close()


    # first_line = lines[0].split()
    # node_count = int(first_line[0])
    # edge_count = int(first_line[1])

    # edges = []
    # for i in range(1, edge_count + 1):
    #     line = lines[i]
    #     parts = line.split()
    #     edges.append((int(parts[0]), int(parts[1])))

    # # build a trivial solution
    # # every node has its own color
    # solution = range(0, node_count)

    # # prepare the solution in the specified output format
    # output_data = str(node_count) + ' ' + str(0) + '\n'
    # output_data += ' '.join(map(str, solution))

    # return output_data


import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        input_data_file = open(file_location, 'r')
        input_data = ''.join(input_data_file.readlines())
        input_data_file.close()
        print solve_it(input_data)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/gc_4_1)'

