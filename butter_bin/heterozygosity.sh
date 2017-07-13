#!/bin/bash

VCF="all.raw.snps.indels.vcf"
SIZES="V1_scaffolds.sizes"
WINDOWS="V1_scaffolds.windows.bed"
WINDOW_SIZE_BP=10000
#bedtools makewindows -g ${SIZES} -w ${WINDOW_SIZE_BP} > ${WINDOWS}
for sample in $(bcftools query -l ${VCF}); do
    echo $sample
    #make heterozygous snvs
    bcftools view -s ${sample} ${VCF}  |\
        bcftools view  -c 1 -g het --types snps \
        -m 2 -M 2 > tmp
    #count heterozygous snvs in the windows in the first file
    bedtools intersect -c -a ${WINDOWS} -b tmp >\
        ${sample}.genome_heterozygosity_regions.bed
done
