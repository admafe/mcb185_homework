# 62skewer.py by Adele Ferrer

import sys
import mcb185

#Command Line: python3 62skewer.py ecoli.fa.gz 1000 

w = int(sys.argv[2])

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	g = seq[0:w].count('G')
	c = seq[0:w].count('C')

for i in range(len(seq) - w):
	off = seq[i]
	on = seq[i+w]
	
	if off == 'C': c-=1
	elif on =='G': g -=1
	
	if on =='C': c +=1
	elif on == 'G': g += 1
	
	comp = (c+g)/w
	if (g+c) > 0: skew = (g-c)/(g+c)
	else:         skew = 0 
	
	print(f'{i}\t{comp:.3f}\t{skew:.3f}')