PREFIX=/mnt/storagesm/ksenia/butter/alignment
#goleft_linux64 indexcov --directory ${PREFIX}/coverage ${PREFIX}/Karindus.sorted.onlymapped.realigned.dedup.bam
#goleft_linux64 indexcov --directory ${PREFIX}/coverage ${PREFIX}/Morgani.sorted.onlymapped.realigned.dedup.bam
#goleft_linux64 indexcov --directory ${PREFIX}/coverage ${PREFIX}/V1.sorted.onlymapped.realigned.dedup.bam

samtools depth -a ${PREFIX}/Karindus.sorted.onlymapped.realigned.dedup.bam | awk '{sum+=$3} END { print "Average = ",sum/NR,sum}' > ${PREFIX}/coverage/Karindus.cov;
samtools depth -a ${PREFIX}/Morgani.sorted.onlymapped.realigned.dedup.bam | awk '{sum+=$3} END { print "Average = ",sum/NR,sum}' > ${PREFIX}/coverage/Morgani.cov;
samtools depth -a ${PREFIX}/V1.sorted.onlymapped.realigned.dedup.bam | awk '{sum+=$3} END { print "Average = ",sum/NR,sum}' > ${PREFIX}/coverage/V1.cov;
