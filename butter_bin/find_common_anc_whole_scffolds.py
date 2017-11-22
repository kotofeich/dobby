#!/usr/bin/env python
'''
find stretches of continuous ancestor
'''
import sys
from argparse import ArgumentParser
from collections import defaultdict

def parse_sizes(sizes):
    data = {}
    with open(sizes) as f:
        for line in f:
            line = line.strip().split()
            data[line[0]] = int(line[1])
    return data

def parse_anc(anc):
    data = defaultdict(list)
    with open(anc) as f:
        for line in f:
            line = line.strip().split()
            if len(line) < 3:
                continue
            data[line[0]].append((int(line[1]),line[2]))
    return data

def find_stretches(anc, sizes): 
    for scaffold in sizes:
        prev_anc = ''
        start = 0
        for snp in anc[scaffold]:
            if not prev_anc:
                end = snp[0]
                prev_anc = snp[1]
            else:
                if prev_anc != snp[1]:
                    print "\t".join(map(str,[scaffold, start, end, prev_anc]))
                    print "\t".join(map(str,[scaffold, end, snp[0], 'inter_anc_region']))
                    prev_anc = snp[1]
                    start = snp[0]
                    end = snp[0]
                else:
                    end = snp[0]
        if prev_anc:
            print "\t".join(map(str,[scaffold, start, sizes[scaffold], prev_anc]))
        else:
            print "\t".join(map(str,[scaffold, start, sizes[scaffold], 'no_anc']))
             


if __name__ == '__main__':
    #input is vcf with snvs only
    parser = ArgumentParser()
    parser.add_argument('anc')
    parser.add_argument('sizes')
    args = parser.parse_args()
    sizes = parse_sizes(args.sizes)
    anc = parse_anc(args.anc)
    find_stretches(anc, sizes)

