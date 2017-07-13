#!/usr/bin/env python

import sys


def karindus_ancestry(v, kar, mor):
    return v=='0/0' and\
            (kar=='0/0' or kar=='0/1') and\
                mor=='1/1' or\
                 v=='0/1' and kar=='0/1' and mor=='0/0'

def morgani_ancestry(v, kar, mor):
    return v=='0/0' and\
            (mor=='0/0' or mor=='0/1') and\
                kar=='1/1' or\
                 v=='0/1' and mor=='0/1' and kar=='0/0'

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
            if karindus_ancestry(v, kar, mor):
                print chrom+'\t'+pos+'\t'+'karindus'
                #print v, kar, mor
                if chrom == prev_chr and prev_status\
                    and prev_status == 'morgani':
                    change += 1
                prev_status = 'karindus'
            if morgani_ancestry(v, kar, mor):
                print chrom+'\t'+pos+'\t'+'morgani'
                #print v, kar, mor
                if chrom == prev_chr and prev_status\
                    and prev_status == 'karindus':
                    change += 1
                prev_status = 'morgani'
            prev_chr = chrom
        ##print 'changes:', change 
