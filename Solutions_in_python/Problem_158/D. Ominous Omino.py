#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# pylint: disable=invalid-name,missing-docstring,bad-builtin
from sys import stdin

def main():
    precal = {
        (1, 1, 1): 0,
        (1, 1, 2): 0,
        (1, 1, 3): 0,
        (1, 1, 4): 0,
        (1, 2, 1): 0,
        (1, 2, 2): 0,
        (1, 2, 3): 0,
        (1, 2, 4): 0,
        (1, 3, 1): 0,
        (1, 3, 2): 0,
        (1, 3, 3): 0,
        (1, 3, 4): 0,
        (1, 4, 1): 0,
        (1, 4, 2): 0,
        (1, 4, 3): 0,
        (1, 4, 4): 0,
        (2, 1, 1): 1,
        (2, 1, 2): 0,
        (2, 1, 3): 1,
        (2, 1, 4): 0,
        (2, 2, 1): 0,
        (2, 2, 2): 0,
        (2, 2, 3): 0,
        (2, 2, 4): 0,
        (2, 3, 1): 1,
        (2, 3, 2): 0,
        (2, 3, 3): 1,
        (2, 3, 4): 0,
        (2, 4, 1): 0,
        (2, 4, 2): 0,
        (2, 4, 3): 0,
        (2, 4, 4): 0,
        (3, 1, 1): 1,
        (3, 1, 2): 1,
        (3, 1, 3): 1,
        (3, 1, 4): 1,
        (3, 2, 1): 1,
        (3, 2, 2): 1,
        (3, 2, 3): 0,
        (3, 2, 4): 1,
        (3, 3, 1): 1,
        (3, 3, 2): 0,
        (3, 3, 3): 0,
        (3, 3, 4): 0,
        (3, 4, 1): 1,
        (3, 4, 2): 1,
        (3, 4, 3): 0,
        (3, 4, 4): 1,
        (4, 1, 1): 1,
        (4, 1, 2): 1,
        (4, 1, 3): 1,
        (4, 1, 4): 1,
        (4, 2, 1): 1,
        (4, 2, 2): 1,
        (4, 2, 3): 1,
        (4, 2, 4): 1,
        (4, 3, 1): 1,
        (4, 3, 2): 1,
        (4, 3, 3): 1,
        (4, 3, 4): 0,
        (4, 4, 1): 1,
        (4, 4, 2): 1,
        (4, 4, 3): 0,
        (4, 4, 4): 0
    }
    players = ['GABRIEL', 'RICHARD']
    dstream = iter(map(int, stdin.read().split()))
    for case in xrange(next(dstream)):
        print "Case #{}: {}".format(case + 1, players[
            precal[next(dstream), next(dstream), next(dstream)]])

main()
