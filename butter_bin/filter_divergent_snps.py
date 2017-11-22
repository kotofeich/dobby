#!/usr/bin/env python

import sys

def divergent_region(kar, mor):
    return not '0' in kar and not '0' in mor
    
if __name__ == '__main__':
    #input is vcf with snvs only
    vcf = sys.argv[1]
    with open(vcf) as f:
        prev_chr = ''
        prev_status = ''
        change = 0
        for line in f:
            line = line.strip()
            if line[0] == '#':
                continue
            line = line.split()
            chrom = line[0]
            if not prev_chr:
                prev_chr = chrom
            else:
                if prev_chr != chrom:
                    prev_status = ''
            pos = line[1]
            v = line[9].split(':')[0]
            kar = line[10].split(':')[0]
            mor = line[11].split(':')[0]
            #print v, kar, mor
            if divergent_region(kar, mor):
                print chrom+'\t'+pos+'\t'+kar+'\t'+mor
            prev_chr = chrom
        ##print 'changes:', change 
