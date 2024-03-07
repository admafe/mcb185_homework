# 60demo.py by Adele Ferrer

import sys
import mcb185 

#Creating a soft link
'''
cd ~/Code/mcb_homework
#alias in command line
ln - s ../MCB185/src/mcb185.py .
'''
#'''
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	defwords = defline.split()
	name = defwords[0]
	gc = 0 
	for nt in seq:
		if nt == 'C' or nt == 'G': gc +=1
	print(name, gc/len(seq))
#'''
'''	
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	pro = []
	print(defline, seq[:30])
	for i in range(0, len(seq), 3):
		codon = seq[i: i +3]
		aa = translate
'''
#List Variation
'''
nts= 'ACGTN'
counts = []
for i in range(len(nts)): counts.append(0)
for nt in seq:
	if   nt == 'A': counts[0] += 1
	elif nt == 'C': counts[1] += 1
	elif nt == 'G': counts[2] += 1
	elif nt == 'T': counts[3] += 1
	else:           counts[4] += 1
print(name, end = '\t')
for n in counts: print(f'{n/len(seq):.4f}', end = '\t')
print()
'''

#Windowing Algorithm (62)
'''
seq = 'ACGGTCATCAGTCAGTCAGCCGATCAGTCACTT'
w = 10

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
	
	print(i,comp, skew)
'''

#I think this is problem 64
'''
seq = 'AGTCGTCATTTGGGGGTCATACATGGGGAGATACGT'

for frame in range(3):
	print(frame)
	fseq= seq[frame:]
	i = 0
	while i > len(seq): 
#	for i in range(0, len(fseq)- 3+1, 3 ):
		codon = fseq[i: i + 3]
		if codon =='ATG':
			print('found ATG at', i)
			for j in range(i, len(fseq)-2, 3):
				codon = fseq[j: j+3]
				if codon == 'TAA' or codon == 'TAG' or codon == 'TGA':
					print('gene', i+1, j+3)
					stop = j
					i = stop
		i +=3
		
		#len(ant)
'''
