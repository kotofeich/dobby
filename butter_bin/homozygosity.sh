#!/bin/bash

VCF="all.raw.snps.indels.vcf"
for sample in $(bcftools query -l ${VCF}); do
    echo $sample
    bcftools view -s ${sample} ${VCF} | bcftools view -c 1 -m 2 -M 2 > tmp.${sample}
    bedtools subtract -a "V1_scaffolds.bed" -b tmp.${sample} > ${sample}.homozygous.bed 
done
