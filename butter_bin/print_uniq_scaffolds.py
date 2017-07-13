#!/usr/bin/env python

import sys
from collections import defaultdict

def parse_sizes(s):
    sizes = dict()
    with open(s) as f:
        for line in f:
            line = line.strip().split()
            sizes[line[0]] = line[1]
    return sizes

if __name__ == '__main__':
    stats = sys.argv[1]
    sizes = parse_sizes(sys.argv[2])
    d = defaultdict(set)
    with open(stats) as f:
        for line in f:
            line = line.strip().split()
            d[line[0]].add(line[-1])
    for key in d:
        if len(d[key]) == 1:
            print key+'\t'+ sizes[key] + '\t' + d[key].pop()

    
