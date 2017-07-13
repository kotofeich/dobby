#!/usr/bin/env python

import sys


if __name__ == '__main__':
    #input is vcf with snvs only
    stats = sys.argv[1]
    with open(stats) as f:
        prev_anc = ''
        prev_chrom = ''
        start = 0
        end = 0
        cur_end = 0
        for line in f:
            line = line.strip().split()
            if prev_anc:
                if line[0] == prev_chrom and\
                     prev_anc == line[2]:
                    cur_end = line[1]
                else:
                    end = cur_end
                    if start != end:
                        print "\t".join([prev_chrom, start, end, prev_anc])
                    prev_chrom = line[0]
                    start = line[1]
                    cur_end = start
                    prev_anc = line[2]
            if not prev_anc:
                prev_anc = line[2]
                prev_chrom = line[0]
                start = line[1]
                cur_end = start
